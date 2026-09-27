import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dist = r'C:\Users\caesa\Documents\Codex\2026-09-27\files-pasted-by-the-user-sites\alrased\dist'
assets_dir = os.path.join(dist, 'assets')
assets_on_disk = set(os.listdir(assets_dir))

content_js = open(os.path.join(dist, 'content.js'), encoding='utf-8').read()
index_html = open(os.path.join(dist, 'index.html'), encoding='utf-8').read()
app_js = open(os.path.join(dist, 'app.js'), encoding='utf-8').read()

# Check font-face files in CSS
css_files = [f for f in os.listdir(dist) if f.endswith('.css')]
css_refs = set()
for cf in css_files:
    txt = open(os.path.join(dist, cf), encoding='utf-8').read()
    for m in re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', txt):
        if not m.startswith('data:'):
            css_refs.add(m)

print("CSS references:", css_refs)

# Check assets in HTML src/href
html_refs = set(re.findall(r'(?:src|href|data-open)=["\']([^"\']+)["\']', index_html))
print("HTML references:", html_refs)

# Check all sets in content.js
# sets = { key: [ [title, asset_id, ...], ... ] }
asset_ids_in_sets = set()
# regex for 2nd element of array: ['...', 'asset_id', ...]
for match in re.findall(r"\[\s*\'[^\']+\'\s*,\s*\'([^\']+)\'", content_js):
    asset_ids_in_sets.add(match)

print(f"Total asset IDs in presentationSets: {len(asset_ids_in_sets)}")

missing_assets = []
for aid in asset_ids_in_sets:
    fname = aid + '.webp'
    if fname not in assets_on_disk:
        missing_assets.append(fname)

print("Missing assets in presentationSets:", missing_assets)

# Check explicitly called screen('...', ...) or A('...') or img src
explicit_js_assets = set()
for m in re.findall(r"screen\(\s*\'([^\']+)\'", content_js):
    explicit_js_assets.add(m + '.webp' if not m.endswith('.webp') else m)
for m in re.findall(r"A\(\s*\'([^\']+)\'", content_js):
    explicit_js_assets.add(m + '.webp' if not m.endswith('.webp') else m)
for m in re.findall(r"src=\"\$\{A\(\'([^\']+)\'\)\}\"", content_js):
    explicit_js_assets.add(m + '.webp' if not m.endswith('.webp') else m)

print(f"Explicit JS assets: {len(explicit_js_assets)}")
missing_explicit = [f for f in explicit_js_assets if f not in assets_on_disk]
print("Missing explicit JS assets:", missing_explicit)
