from PIL import Image
import pathlib,json
root=pathlib.Path(__file__).resolve().parent.parent
src=root/'work'/'figma'; dest=root/'alrased'/'dist'/'assets'
manifest={}
for f in src.glob('*.png'):
    if f.stem=='detail':continue
    im=Image.open(f).convert('RGB')
    # Retain natural design resolution; high-density exports are limited to 1800 pixels wide.
    if im.width>1800:im.resize((1800,round(im.height*1800/im.width)),Image.Resampling.LANCZOS).save(dest/(f.stem+'.webp'),quality=92,method=6)
    else:im.save(dest/(f.stem+'.webp'),quality=92,method=6)
    manifest[f.stem]={'width':im.width,'height':im.height}
im=Image.open(src/'2021-2.png').convert('RGB');scale=im.width/1440
for name,y,h in [('home-hero',0,1180),('home-care',1180,840),('home-process',2020,551),('home-proof',2571,630),('home-packages',3201,1098),('home-services',4299,996),('home-faq',5295,836),('home-end',6131,733)]:
    im.crop((0,round(y*scale),im.width,round((y+h)*scale))).save(dest/(name+'.webp'),quality=94)
(src/'dimensions.json').write_text(json.dumps(manifest),encoding='utf-8')
print('Prepared',len(list(dest.glob('*.webp'))),'assets; source homepage:',im.size)
