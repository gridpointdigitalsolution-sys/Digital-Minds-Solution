"""
inject_buttons_css.py — adds <link rel="stylesheet" href="buttons.css"> to all HTML pages.
Idempotent. Injects just before </head>.
Run from SITE directory.
"""
import os

LINK_TAG = '<link rel="stylesheet" href="buttons.css">'
MARKER   = 'buttons.css'
SITE_DIR = os.path.dirname(os.path.abspath(__file__))

html_files = [f for f in os.listdir(SITE_DIR) if f.endswith('.html')]
patched = skipped = 0

for fname in sorted(html_files):
    path = os.path.join(SITE_DIR, fname)
    with open(path, 'r', encoding='utf-8') as fh:
        src = fh.read()

    if MARKER in src:
        print(f'  skip  {fname}')
        skipped += 1
        continue

    if '</head>' not in src:
        print(f'  WARN  {fname}  (no </head>)')
        continue

    new_src = src.replace('</head>', f'  {LINK_TAG}\n</head>', 1)

    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(new_src)

    print(f'  patch {fname}')
    patched += 1

print(f'\nDone. {patched} patched, {skipped} skipped.')
