#!/usr/bin/python

from PIL import Image
import requests
import json
from pprint import pprint
import io
import sys

class AvatarCanvas:
	
	canvas_height =3307
	canvas_width =4677
	bleed = 45	
	avatar_height =720
	avatar_width = 720
	avatar_img_url=""
	canvas_bg ="white"
	canvas_orientation="landscape"
	file_name=""
	username = ""
	canvas=None
	avatar=None
	file_format="PDF"
	file_extension="."+file_format.lower()

	def get_avatar_image_url(self):

		try:
			r= requests.get('https://api.github.com/users/'+self.username)
		except requests.exceptions.RequestException as e:    
			print e
			sys.exit(1)	
		
		print r.status_code
		if r.status_code == 200:
			github_json = r.json()
			# avartar url 
			avatar_img_url = github_json["avatar_url"]
			
			self.avatar_img_url = avatar_img_url
		else:
			#print r.status_code
			print "\n\tPlease check username"
			sys.exit()

		#return self.avatar_img_url
 

	def get_avatar_image(self):

		try:
			fd = requests.get(self.avatar_img_url, stream=True)

		except requests.exceptions.RequestException as e:    
			print e
			sys.exit(1)

		if fd.status_code is 200:

			image_file = io.BytesIO(fd.raw.read())

			im = Image.open(image_file)

			# Avatar image resolution being scaled down here
			resized_avatar = im.resize((self.avatar_width, self.avatar_height))

			self.avatar = resized_avatar
		else:
			print "URL Image not found"
			print fd.status_code

	


	def create_canvas(self):

		if self.canvas_orientation=="landscape":
			self.canvas = Image.new("RGB", (self.canvas_width, self.canvas_height), self.canvas_bg)
		else :
			self.canvas = Image.new("RGB", (self.canvas_height, self.canvas_width), self.canvas_bg)

		#return self.canvas

	def create_avatar_sheet(self):
		
		#avatar_width =720
		#avatar_height = 720
		x_pos_original = 45
		x_pos = 45
		y_pos = 45


		#canvas_width = 4677
		#canvas_height = 3307

		width_pos = self.canvas_width
		height_pos = self.canvas_height


		for y in range(self.canvas_height/(self.avatar_height+self.bleed)):
			
			for x in range(self.canvas_width/(self.avatar_width+self.bleed)):
				self.canvas.paste(self.avatar, (x_pos,y_pos))
				x_pos = x_pos + (self.avatar_width+self.bleed)	

			
			x_pos = x_pos_original
			y_pos = y_pos + (self.avatar_height+self.bleed)

		self.canvas.save(self.username+self.file_extension,self.file_format)
		#bg.save("out_A4_xy_fill.pdf","PDF")
