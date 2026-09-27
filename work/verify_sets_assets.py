import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

dist = r'C:\Users\caesa\Documents\Codex\2026-09-27\files-pasted-by-the-user-sites\alrased\dist'
assets_dir = os.path.join(dist, 'assets')
assets_on_disk = set(os.listdir(assets_dir))

content_js = open(os.path.join(dist, 'content.js'), encoding='utf-8').read()

# Sets are structured like:
# category: [ ['title', 'asset-name', 'heading', 'text'], ... ]
all_set_assets = set()
for m in re.findall(r"\[\s*\'[^\']+\'\s*,\s*\'([a-z0-9\-]+)\'", content_js):
    all_set_assets.add(m + '.webp')

missing = [f for f in all_set_assets if f not in assets_on_disk]

print(f"Total set assets checked: {len(all_set_assets)}")
print(f"Missing set assets: {missing}")

if not missing:
    print("SUCCESS: 100% of set assets exist in dist/assets!")
