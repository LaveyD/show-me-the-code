from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('0000.png').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
# fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((70,0), "1", fill=(255,0,0,255))
# draw text, full opacity

out = Image.alpha_composite(base, txt)

out.save('0000a.png', 'PNG')