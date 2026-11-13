import os, glob

files = glob.glob('docs/**/*.md', recursive=True)

mojibake_chars = ['Ã³', 'Ã¡', 'Ã©', 'Ã­', 'Ãº', 'Ã±', 'â€”', 'â€¢', 'Â¿', 'Â«', 'Â»']

affected = []
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    found = [m for m in mojibake_chars if m in c]
    if found:
        affected.append((f, found))

print(f"Total archivos con caracteres alterados (mojibake): {len(affected)}")
for f, fnd in affected[:10]:
    print(f, fnd[:3])
