"""
inject_vortex.py — adds neural-vortex.js to all HTML pages (idempotent).
Run from the SITE\ directory.
"""
import os, re

SCRIPT_TAG = '<script src="neural-vortex.js"></script>'
MARKER     = 'neural-vortex.js'
SITE_DIR   = os.path.dirname(os.path.abspath(__file__))

html_files = [f for f in os.listdir(SITE_DIR) if f.endswith('.html')]
patched = skipped = 0

for fname in sorted(html_files):
    path = os.path.join(SITE_DIR, fname)
    with open(path, 'r', encoding='utf-8') as fh:
        src = fh.read()

    if MARKER in src:
        print(f'  skip  {fname}  (already has vortex)')
        skipped += 1
        continue

    if '</body>' not in src:
        print(f'  WARN  {fname}  (no </body> tag — skipped)')
        continue

    # Inject just before </body>
    new_src = src.replace('</body>', f'  {SCRIPT_TAG}\n</body>', 1)

    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(new_src)

    print(f'  patch {fname}')
    patched += 1

print(f'\nDone. {patched} patched, {skipped} already done.')
