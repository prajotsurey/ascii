from os import access
from PIL import Image, ImageDraw, ImageFont
from ast import literal_eval

def getCharList():
	file = open("chars.txt","r")
	string_array = file.readlines()[0] # this will get the character array but as a string
	chars_array = literal_eval(string_array) # convert the string to an actual array

	#use the chars to create file name for opening the images and assign brightness to the character

	char_list = []

	for char in chars_array:
		try:
			image = Image.open('./chars/ascii-'+char+'-.png')
		except:
			image = Image.open('./chars/ascii-forwardslash-.png')
		
		pixels = image.getdata()
		brightness_sum = 0
		width,height = image.size
		for pixel in pixels:	#average brightness of all pixels
			brightness_sum += (pixel[0] + pixel[1] + pixel[2])/3
		avg_brightness = brightness_sum/(width*height)
		char_dict = {
			'char': char,
			'brightness': avg_brightness
		}
		char_list.append(char_dict.copy())

	for i in range(0,len(char_list)-1):
		for j in range(0,(len(char_list)-1-i)):
			if (char_list[j]['brightness'] > char_list[j+1]['brightness']):
				char_list[j], char_list[j+1] = char_list[j+1], char_list[j]

	return char_list

