import os, shutil

root_dir = r'C:\Users\caesa\Documents\Codex\2026-09-27\files-pasted-by-the-user-sites'
dist_dir = os.path.join(root_dir, 'alrased', 'dist')

# Files to copy from dist to root
files_to_copy = [
    'index.html',
    'style.css',
    'chapters.css',
    'refinements.css',
    'mobile-fixes.css',
    'app.js',
    'content.js'
]

for fname in files_to_copy:
    src = os.path.join(dist_dir, fname)
    dst = os.path.join(root_dir, fname)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {fname} to repo root.")

# Copy assets folder to root
src_assets = os.path.join(dist_dir, 'assets')
dst_assets = os.path.join(root_dir, 'assets')
if os.path.exists(dst_assets):
    shutil.rmtree(dst_assets)
shutil.copytree(src_assets, dst_assets)
print("Copied assets directory to repo root.")
