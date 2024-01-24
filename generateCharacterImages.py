from PIL import Image, ImageDraw, ImageFont
from ast import literal_eval
# get an image

file = open("chars.txt","r")
string_array = file.readlines()[0] # this will get the character array but as a string
chars_array = literal_eval(string_array) # convert the string to an actual array

for char in chars_array:

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", (16,16), (0,0,0))

    # get a font
    fnt = ImageFont.truetype("arial.ttf", 16)

    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((0,0), char, font=fnt, fill=(255,255,255))
    # draw text, full opacity
    try :
        txt.save('./chars/ascii-'+char+'-.png')
    except:
        txt.save('./chars/ascii-forwardslash-.png')
        