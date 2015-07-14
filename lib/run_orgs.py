from orgs import *
import time


def phase2(org):

	#
	# Verifies organisation name 
	#
	org_name = org_exits(org)			
	print org_name

	while(len(str(org_name)) is 0 ):
		print type(org_name)
		print "Waiting for org verification..."
		time.sleep(5)

	#
	# Obtains users user token 
	#
	access_token= get_user_token()			

	while(len(str(access_token)) is  0 ):
		print access_token
		print "Waiting for access token retrieval ..."
		time.sleep(5)


	member_list = []

	# Retrieve memeber list
	member_list= get_org_users(org_name,access_token)	

	while(len(member_list) is  0 ):
		print member_list
		print "Bringing org members ..."
		time.sleep(5)

	#
	# Print Organisation avatars
	#
	print_org_avatars(member_list,org_name)			


