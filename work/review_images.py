from PIL import Image, ImageOps, ImageDraw
import json, pathlib
p=pathlib.Path(__file__).parent/'figma'
items=json.loads((p/'exports.json').read_text('utf-8'))
for start in range(0,len(items),8):
    canvas=Image.new('RGB',(1600,1200),'#ddd')
    d=ImageDraw.Draw(canvas)
    for j,item in enumerate(items[start:start+8]):
        f=p/(item['id'].replace(':','-')+'.png')
        if not f.exists(): continue
        im=Image.open(f).convert('RGB');im.thumbnail((390,550))
        x=(j%4)*400;y=(j//4)*600
        canvas.paste(im,(x,y+30));d.text((x+5,y+5),item['id'],fill='black')
    canvas.save(p/f'review-{start}.jpg')
