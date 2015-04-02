import sys,string,random,getopt


def show_help():
	print './MixString.py <AmountOfNamesRequired> <emailAddress> <password> <OrgStartNumber>'
	print './MixString.py 2 @something.com passw0rd 6000'
	print 'Outputs: Num:0 MickFLannery,MickFLannery@something.com,passw0rd,6000\n Num:1 JoeJose,JoeJose@something.com,passw0rd,6000'
	print 'Outputs: int,"text","text","text","text","int"'
	

	
	
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
	OrgStartNumber = int(sys.argv[5])
	
	#with open("TestMembers.txt") as f:
	with open("yob1998.txt") as f:
		FileToRead = f.read().split('\n')

	rows = int(sys.argv[1])
	Org = int(OrgStartNumber)
	for num in range(0,rows):
		
		#Some Ratio Things
		#Check if every nth value is equal to 25 Assign role
		if (int(num+1) % 25 == 0 or int(num+1) == 1):
			position = "Manager"
		else:
			position = "Student"
		#Check if every nth value is modulus one-hundred assign increment value by one
		if (int(num+1) % 100 == 0):
			Org +=1
		
		#read in 2 values from file
		RandoName = ''.join(random.sample((FileToRead),2))
		print ("Number:%s,%s,%s%s,%s,%s,%s" % (num+1, RandoName, RandoName, emailAddress, password, position, Org))
		#
		
if __name__ == "__main__":
	main(sys.argv[1:])
