import os
import glob
import re

RULES = [
    ("docs/inicio-rapido.md", 3.8),
    ("docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/*.md", 3.2),
    ("docs/02_PROCESOS_CLAVE/*.md", 2.5),
    ("docs/01_ROLES/*.md", 2.0),
    ("docs/00_INICIO_Y_MOCS/*.md", 1.8),
    ("docs/04_GLOSARIO_Y_CONCEPTOS/*.md", 1.8),
    ("docs/05_MARCO_NORMATIVO/*.md", 1.3),
    ("docs/archivo_maestro/*.md", 0.35),
    ("docs/archivo_maestro/legalidad/*.md", 0.35),
]

def apply_boost(filepath: str, boost: float) -> bool:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if YAML frontmatter exists
    if content.startswith("---\n") or content.startswith("---\r\n"):
        match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", content, flags=re.DOTALL)
        if match:
            fm = match.group(1)
            body = content[match.end():]
            if re.search(r"(?m)^search:\s*$", fm):
                # Already has search block; update boost if present or insert
                if re.search(r"(?m)^\s+boost:\s*[0-9.]+", fm):
                    fm_new = re.sub(r"(?m)^(\s+boost:\s*)[0-9.]+", rf"\g<1>{boost}", fm)
                else:
                    fm_new = re.sub(r"(?m)^(search:\s*)$", rf"\g<1>\n  boost: {boost}", fm)
            else:
                fm_new = fm.rstrip() + f"\nsearch:\n  boost: {boost}"
            new_content = f"---\n{fm_new}\n---\n{body}"
        else:
            return False
    else:
        new_content = f"---\nsearch:\n  boost: {boost}\n---\n\n{content}"

    if new_content != content:
        with open(filepath, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_content)
        return True
    return False

updated = 0
for pattern, boost in RULES:
    for path in sorted(glob.glob(pattern)):
        if os.path.basename(path) == "index.md" and "archivo_maestro" in path:
            continue
        if apply_boost(path, boost):
            updated += 1

print(f"Archivos actualizados con search.boost: {updated}")
