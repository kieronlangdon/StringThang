import sys,string,random,getopt


def show_help():
	print './MixString.py <AmountOfNamesRequired> <emailAddress> <password>'
	print './MixString.py 2 @something.com passw0rd'
	print 'Outputs: Num:0 MickFLannery,MickFLannery@something.com,passw0rd\n Num:1 JoeJose,JoeJose@something.com,passw0rd'
	print 'Outputs: int,"text","text","text","text"'

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
	
	#with open("TestMembers.txt") as f:
	with open("yob1998.txt") as f:
		FileToRead = f.read().split('\n')

	rows = int(sys.argv[1])
	
	for num in range(0,rows):
		#read in 2 values from file
		RandoName = ''.join(random.sample((FileToRead),2))
		
		print ("Number:%s,%s,%s%s,%s" % (num+1, RandoName, RandoName, emailAddress, password))

if __name__ == "__main__":
	main(sys.argv[1:])
