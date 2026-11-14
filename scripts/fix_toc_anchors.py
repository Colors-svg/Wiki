import os, glob, re, unicodedata

def slugify(title):
    title = re.sub(r'<[^>]+>', '', title)
    text = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', text)

md_files = glob.glob('docs/**/*.md', recursive=True)

total_fixed = 0

for filepath in md_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all actual headings in the file
    headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
    # Build map of normalized text to slug
    valid_slugs = {slugify(h[1]) for h in headings}

    # Function to replace anchor links
    def fix_link(match):
        text = match.group(1)
        href = match.group(2)
        if href.startswith('#'):
            anchor = href[1:]
            # Compute slugified version
            target_slug = slugify(anchor)
            # If target_slug is a valid heading slug
            if target_slug in valid_slugs:
                return f'[{text}](#{target_slug})'
            # Also try slugifying the text itself
            text_slug = slugify(text)
            if text_slug in valid_slugs:
                return f'[{text}](#{text_slug})'
        return match.group(0)

    # Replace markdown links: [text](#anchor)
    new_content = re.sub(r'\[([^\]]+)\]\((\#[^\)]+)\)', fix_link, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total_fixed += 1
        print(f"Enlaces corregidos en: {filepath}")

print(f"\nProceso finalizado: {total_fixed} archivos con enlaces a secciones corregidos.")
