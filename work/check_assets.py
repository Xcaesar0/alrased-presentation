import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dist = r'C:\Users\caesa\Documents\Codex\2026-09-27\files-pasted-by-the-user-sites\alrased\dist'
content_js = open(os.path.join(dist, 'content.js'), encoding='utf-8').read()
index_html = open(os.path.join(dist, 'index.html'), encoding='utf-8').read()

assets_on_disk = set(os.listdir(os.path.join(dist, 'assets')))

# Extract every asset reference in sets and HTML
referenced = set()
for m in re.findall(r"\'([207|206|209|210|211|home|alexandria|review][^\']+)\'", content_js):
    name = m if any(m.endswith(x) for x in ['.webp', '.ttf', '.png', '.jpg']) else m + '.webp'
    referenced.add(name)

for m in re.findall(r'assets/([^\'"]+)', index_html):
    referenced.add(m)

for m in re.findall(r'screen\(\'([^\']+)\'', content_js):
    name = m if m.endswith('.webp') else m + '.webp'
    referenced.add(name)

for m in re.findall(r'A\(\'([^\']+)\'\)', content_js):
    name = m if m.endswith('.webp') else m + '.webp'
    referenced.add(name)

missing = [f for f in referenced if f not in assets_on_disk]

print(f'Total referenced assets: {len(referenced)}')
print(f'Missing assets: {missing}')
unref = sorted(assets_on_disk - referenced)
print(f'Unreferenced on disk ({len(unref)}): {unref}')
