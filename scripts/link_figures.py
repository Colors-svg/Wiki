import os
import re

TARGET_DIRS = ["docs/archivo_maestro", "archivo_maestro"]

replaced_count = 0

for target_dir in TARGET_DIRS:
    if not os.path.exists(target_dir):
        continue
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                with open(file_path, "r", encoding="utf-8") as fp:
                    content = fp.read()

                # Pattern: ![[VI-XX-YY-figura-ZZ.png]]
                # Replacement in docs/archivo_maestro/ : ![Figura ZZ](../assets/figuras/VI-XX-YY/figura-ZZ.png)
                def replace_placeholder(match):
                    global replaced_count
                    doc_code = match.group(1) # e.g. VI-GU-01
                    fig_num = match.group(2)  # e.g. 01
                    rel_prefix = "../assets/figuras" if "docs" in root else "docs/assets/figuras"
                    replaced_count += 1
                    return f"![Figura {int(fig_num)}]({rel_prefix}/{doc_code}/figura-{fig_num}.png)"

                new_content = re.sub(r"!\[\[(VI-[A-Z]{2}-\d{2})-figura-(\d+)\.png\]\]", replace_placeholder, content)

                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)

print(f"Total de referencias a figuras vinculadas con éxito: {replaced_count}")
