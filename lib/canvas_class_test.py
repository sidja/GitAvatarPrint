#!/usr/bin/python

from Canvas import AvatarCanvas
import sys


def print_avatar_sheet(username="octocat"):
	octocat = AvatarCanvas()
	octocat.username=username
	octocat.get_avatar_image_url()
	octocat.get_avatar_image()
	octocat.create_canvas()
	octocat.create_avatar_sheet()

def org_avatar_print():
	app_auth_url = "https://github.com/login/oauth/authorize?client_id=a4c0f8ffe97e36b2f91e&scope=read:org"
	
	return


#print_avatar_sheet("sidja")

#print sys.argv[1]

#print_avatar_sheet(sys.argv[1])

