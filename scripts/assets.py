from PIL import Image, ImageDraw, ImageFont
import os
os.makedirs('public', exist_ok=True)
def font(sz, serif=True):
    for p in (["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf","/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"] if serif else ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf","/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"]):
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    return ImageFont.load_default()
PAPER='#f7f5f1'; INK='#1c1b1a'; CORAL='#d9480f'; OLIVE='#4d6a3a'
im=Image.new('RGB',(1200,630),PAPER); d=ImageDraw.Draw(im)
d.rectangle((0,0,1200,10),fill=CORAL)
d.text((80,70),'BestRecruitmentTools.com',font=font(34),fill=INK)
d.text((80,125),'RANKED, NOT LISTED',font=font(18,False),fill=OLIVE)
d.text((80,210),'The best recruitment tools of 2026,',font=font(62),fill=INK)
d.text((80,290),'ranked by the problem',font=font(62),fill=INK)
d.text((80,370),'you are trying to solve.',font=font(62),fill=CORAL)
d.text((80,490),'35 tools rated · 11 use-case rankings · no vendor pays for position',font=font(26,False),fill='#4a4745')
im.save('public/og.png')
for sz,name in [(512,'icon-512.png'),(192,'icon-192.png'),(180,'apple-touch-icon.png'),(96,'favicon-96.png')]:
    ic=Image.new('RGB',(sz,sz),PAPER); dd=ImageDraw.Draw(ic); dd.rectangle((0,0,sz,int(sz*0.06)),fill=CORAL); dd.text((sz/2,sz/2+sz*0.04),'B',font=font(int(sz*0.62)),fill=INK,anchor='mm'); ic.save('public/'+name)
Image.open('public/favicon-96.png').resize((48,48)).save('public/favicon.ico',sizes=[(48,48)])
open('public/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="#f7f5f1"/><rect width="64" height="5" fill="#d9480f"/><text x="32" y="48" font-family="Georgia,serif" font-weight="700" font-size="44" text-anchor="middle" fill="#1c1b1a">B</text></svg>')
print('assets ok')
