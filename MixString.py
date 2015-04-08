import sys,string,random,getopt,re


def show_help():
	print './MixString.py <AmountOfNamesRequired> <emailAddress> <password> <OrgStartNumber> <personManager>'
	print './MixString.py 2 @something.com passw0rd 6000'
	print 'Outputs: Num:1 MickFlannery,MickFlannery@something.com,Student,passw0rd,6000,Root\n Num:2 JoeJose,JoeJose@something.com,Student,passw0rd,6000,MickFlannery'
	print 'Outputs: int,"text","text","text","text", int,"text"'
	

	
	
def main(argv):
	try:
		opts, args = getopt.getopt(argv,"h",["help"])
	except getopt.GetoptError, e:
		print e
		sys.exit(2)
	for opt, arg in opts:
		if (opt == '-h') or (opt == '--help'):
			show_help()
			sys.exit()
	if (len(sys.argv) == 1):
		show_help()
		sys.exit(0)
	emailAddress = str(sys.argv[2])
	password = str(sys.argv[3])
	OrgStartNumber = int(sys.argv[4])
	EmailCount = 0
	
	#with open("TestMembers.txt") as f:
	with open("yob1880.txt") as f:
		FileToRead = f.read().split('\n')

	rows = int(sys.argv[1])
	Org = int(OrgStartNumber)
	for num in range(0,rows):
		
		#Some Ratio Things
		#Check if every nth value is equal to 25 Assign position + Manager
		if (int(num+1) % 25 == 0 or int(num+1) == 1):
			position = "Manager"
			personManager = "Root"
		else:
			position = "Student"
		#Check if every nth value is modulus one-hundred assign increment value by one
		if (int(num+1) % 100 == 0):
			Org +=1
		
		#read in 2 values from file
		RandoName = ''.join(random.sample((FileToRead),2))
		if len(RandoName+emailAddress) and emailAddress != None and len(RandoName+emailAddress) <254:
			if re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", RandoName+emailAddress):
				EmailCount +=1
			else:
				print ("Invalid E-mail -- :%s" % (emailAddress))
				sys.exit(0)
		else:
			print ("Invalid E-mail - :%s" % (RandoName+emailAddress))
			sys.exit(0)
		print ("Number:%s,%s,%s%s,%s,%s,%s,%s" % (num+1, RandoName, RandoName, emailAddress, password, position, Org, personManager))
		#Reset Manager to current name if assigned "Root"
		if (position == ("Manager")):
			personManager = RandoName
if __name__ == "__main__":
	main(sys.argv[1:])
