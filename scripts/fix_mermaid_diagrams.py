import os, glob, re

md_files = glob.glob('docs/**/*.md', recursive=True) + glob.glob('wiki/**/*.md', recursive=True)

def fix_mermaid_block(match):
    block = match.group(1)
    
    # 1. Switch 'graph TD' / 'graph LR' to 'flowchart TD' / 'flowchart LR'
    block = re.sub(r'^[ \t]*graph (TD|TB|LR|RL|BT)', r'flowchart \1', block, flags=re.MULTILINE)
    
    # 2. In node labels enclosed in ["..."] or [...] or (...), replace literal \n with <br/>
    # We do a pattern match for ["..."]
    def replace_newlines(m):
        content = m.group(1)
        # replace literal \n
        content = content.replace(r'\n', '<br/>')
        # format bullets if "- " follows <br/>
        content = content.replace('<br/>- ', '<br/>• ')
        return f'["{content}"]'
    
    # Replace labels
    block = re.sub(r'\["([^"]+)"\]', replace_newlines, block)
    
    return f'```mermaid\n{block}```'

total_fixed = 0
for filepath in md_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '```mermaid' in content:
        new_content = re.sub(r'```mermaid\n(.*?)```', fix_mermaid_block, content, flags=re.DOTALL)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Diagramas actualizados en: {filepath}')
            total_fixed += 1

print(f'\nTotal archivos con diagramas optimizados: {total_fixed}')
