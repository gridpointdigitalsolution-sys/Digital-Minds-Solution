#!/usr/bin/env python3
"""
inject_scroll_top.py
Run from the SITE directory.
Injects <script src="scroll-top.js"></script> before </body> in every .html file.
Idempotent — skips files that already contain the reference.
"""

import os
import glob

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_TAG = '  <script src="scroll-top.js"></script>'
MARKER = 'scroll-top.js'
TARGET = '</body>'

html_files = sorted(glob.glob(os.path.join(SITE_DIR, '*.html')))

patched = 0
skipped = 0

for path in html_files:
    fname = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if MARKER in content:
        print(f'  SKIP  {fname}  (already injected)')
        skipped += 1
        continue

    if TARGET not in content:
        print(f'  WARN  {fname}  (no </body> found — skipped)')
        skipped += 1
        continue

    # Inject once, before the first </body>
    new_content = content.replace(TARGET, SCRIPT_TAG + '\n' + TARGET, 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'  PATCH {fname}')
    patched += 1

print()
print(f'Done. Patched: {patched}  |  Skipped/warned: {skipped}  |  Total: {len(html_files)}')
