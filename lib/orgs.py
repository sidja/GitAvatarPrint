import os
import requests
import webbrowser
import json
from pprint import pprint
from canvas_class_test import print_avatar_sheet 
from PyPDF2 import PdfFileReader, PdfFileMerger
import sys



# returns a list of all public members of 
# of an organisation 

def get_org_users(org_name,access_token):

	# Requests organisation members from this url
	url = 'https://api.github.com/orgs/'+org_name+'/members'
	# authorisation performed from here 
	headers = {'Authorization': 'token '+access_token}

	# http GET request
	try:
		r = requests.get(url, headers=headers)
	except requests.exceptions.RequestException as e:    
	    print e
	    sys.exit(1)

	#  http request fails exit program
	if r.status_code is not 200:

		print "\n\t Authrisation issue "
		print "\tPlease try again"
		sys.exit(1)


	print r.url
	print r.text.encode('UTF8')
	
	# convert http request to JSON object
	js = r.json()

	# append members in a list
	memeber_list =[i["login"]for i in js]

	# check if members exist
	# exit if no public members exist in an organistaion
	if len(memeber_list) == 0:
		print "\n\t No memebers in this organistaion"
		print "\t Please try again"
		sys.exit(1)


	return memeber_list

#
# Prints orgnisation users avatars into
# a single pdf
#

def print_org_avatars(member_list,org_name):

	# remove last pdf version of the organisation
	if os.path.isfile(org_name+".pdf"):
		os.remove(org_name+".pdf")

	# print individual avatar pdfs
	for member in member_list:
		print_avatar_sheet(member)

	# merge org memebers avatar pdfs
	merger = PdfFileMerger()

	for member in member_list:
		merger.append(PdfFileReader(member+".pdf"),"rb") 

	# create merged pdf
	merger.write(org_name+".pdf")

	# clean up pdfs
	# remove org members pdfs
	for member in member_list:
		os.remove(member+".pdf")



#
# Returns users git hub access token 
#

def get_user_token():

	# app authorisation url
	app_auth_url = "https://github.com/login/oauth/authorize?client_id=a4c0f8ffe97e36b2f91e&scope=read:org"
	var = ""
	code = None
	access_token=None

	# opens web browser
	# opens app authorisation url 
	webbrowser.open_new(app_auth_url)

	print "\n\n\n\tIf a browser window does not appear please "
	print "\tcopy paste the the below URL into a browser "
	print "\twindow manually\n\n\n"

	# prints app authorisation url if browser window does not open
	print app_auth_url
	print""



	


	# Waits till user confirms app authorisation on github
	while(var is not "y"):
		print "\n\tPlease type 'y' to confirm application "
		print "\tauthorisation on your Github account\n"
		var = raw_input("Press (y): ")
		print "\n\n"

	
	# Retreives app "code" token  from web application
	# "code" is an intermediary token required prior to requesting
	# github api access token
	#
	# Web application flow sends code to a URI defined in 
	# app authorisation 
	# 
	# web last authorised web app code is retrieved from the below URL
	# 
	# 	http://sidvija.pythonanywhere.com/getcode

	try:
		code_request= requests.get("http://sidvija.pythonanywhere.com/getcode")

	except requests.exceptions.RequestException as e:    
	    print e
	    sys.exit(1)

	# Check web apps response
	# App fails if response is invalid
	if code_request.status_code is not 200:
		print "Check pythonanywhere app seems to be down"
		sys.exit(1)
	elif code_request.status_code is 200:

		j = code_request.json()
		print j["code"]

		code = j["code"]

	#
	#
	# Requests git hub access token with "code" token 
	#
	#
	#

	payload={
		
		'client_id':'a4c0f8ffe97e36b2f91e',
		'client_secret':'2adb66f715901686696204e3214fbb3b07dd8b22',
		'code':code
	}

	

	try:
		token_request = requests.post("https://github.com/login/oauth/access_token", data=payload)

	except requests.exceptions.RequestException as e:    
	    print e
	    sys.exit(1)


	print " Token request "+ str(token_request.status_code)

	
	# Execution fails if no access token is found 

	if token_request.status_code is not 200:
		print "Access token not found"
		sys.exit(2)

	elif token_request.status_code is 200:
		
		print token_request.text
		
		access_token = token_request.text.split("&")[0].split("=")[1]
		
		

	return access_token

#
#	Check if organisation exits
#	returns organisation name if valid 
#

def org_exits(org_name):

	get_org_url = "https://api.github.com/orgs/"
	#org_name ="shshsfh"

	try:
		get_org = requests.get(get_org_url+org_name)

	except requests.exceptions.RequestException as e:    
		    print e
		    sys.exit(1)

	if get_org.status_code is not 200:
		print "\n\t Organisation not found"
		print "\t Please try again\n\n"
		sys.exit(1)
	
	return org_name

