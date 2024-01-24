from os import write
from PIL import Image, ImageDraw, ImageFont
from calculateBrightness import getCharList


def resize(image,resizing_factor):
	width,height = image.size
	resized_image = image.resize((int(width/resizing_factor/1), int(height/resizing_factor/1)))
	return resized_image

def grayify(image):
	grayscale_image = image.convert("L")
	return grayscale_image

def convertToAscii(image,charlist):
	pixels = image.getdata()
	ascii_chars = "".join(charlist[int(pixel/2.8)]['char'] for pixel in pixels)
	return ascii_chars

def writeToImage(ascii_chars,width,height,resizing_factor,font_size, font_size_offset):
	txt = Image.new("RGBA", (width*font_size_offset,height*font_size_offset), (0,0,0))
	fnt = ImageFont.truetype("arial.ttf", font_size)
	d = ImageDraw.Draw(txt)

	rowStart = 0
	resized_width = int(width/resizing_factor)
	for i in range(0,len(ascii_chars), resized_width):
		arr = ascii_chars[i:(i+resized_width)]
		j=0
		print("row number: ", rowStart)
		for char in arr:
			d.text((j*resizing_factor*font_size_offset,rowStart), char, font=fnt, fill=(255,255,255))
			j += 1
		
		rowStart += resizing_factor*font_size_offset

	txt.save('./output/asciiImage.png')
	return


def convert_to_ascii_image():
	try:
		image = Image.open('./input/image.jpg')

	except:
		print("image could not be accessed")

	##################################################################################
	# these 3 variables control the output image
	
	# this controls how much the original image is resized before each pixel is replaced by a character
	# each pixel of the resized image is represented by a character in the final image
	# keep this number low for more detail
	resizing_factor = 4

	# font size of the ascii characters
	font_size = 16

	# increases the size of the image while keeping the number of ascii characters same
	# change this if the characters overlap or are too spaced out.
	font_size_offset = int(font_size / 3)
	###################################################################################

	width,height = image.size	
	
	#get the list of characters. we will draw our image with these characters. 
	charlist = getCharList()

	resizedImage = resize(image,resizing_factor)
	grayscaleImage = grayify(resizedImage)

	ascii_chars = convertToAscii(grayscaleImage,charlist)
	writeToImage(ascii_chars,width,height,resizing_factor,font_size, font_size_offset)
convert_to_ascii_image()