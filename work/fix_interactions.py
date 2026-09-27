from pathlib import Path
p=Path(__file__).resolve().parent.parent/'alrased'/'dist'/'app.js'
s=p.read_text(encoding='utf-8')
s=s.replace("const visual=$('.walk-visual',el);const mobile=innerWidth<=800;", "const visual=$('.walk-visual',el);const mobile=innerWidth<=800;if(mobile)return;")
s=s.replace('function syncWalks(){walks.forEach', 'function syncWalks(){if(innerWidth<=800)return;walks.forEach')
s=s.replace("if(el.dataset.set==='manager'){", "if(el.dataset.set==='decisions'&&index>0){surface.scrollTop=surface.clientWidth*((index===2||index===3)?0.25:0.35);}if(el.dataset.set==='manager'){")
p.write_text(s,encoding='utf-8')
print('Updated mobile selection and decision focus')
