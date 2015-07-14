import os
import getopt 
import sys
from bin.canvas_class_test import print_avatar_sheet
from bin.run_orgs import phase2 

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hu:o:",["user=","org="])
	except getopt.GetoptError:
		print '\n Usage \n'
		print '	get_avatars.py -u <username> '
		print '	get_avatars.py -o <organisation_name>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'get_avatars.py -u <username> '
			print 'get_avatars.py -o <organisation_name>'
			sys.exit()

		elif opt in ("-u","--user"):
			user = arg
			print_avatar_sheet(user)
			print ' Your Github avatar sheet is ready'
			sys.exit(2)
		elif opt in ("-o","--org"):
			org = arg
			phase2(org)
			print 'Your organisation avatar sheet is ready'
			sys.exit(2)
	
	print "\n Useage\n"
	print "\tgit_print.py [option] [argument] \n"
	print " Options \n"
	print "\t -u 	: Print Github user's avatar sheet"
	print "\t -o 	: Prints Github users orginasation members"
	print "\t\t  in avatar sheet"
	print "\t\t  (authorisation required)"

if __name__ == "__main__":
   main(sys.argv[1:])