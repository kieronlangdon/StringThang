import sys,string,random,getopt

def show_help():
	print './RandomString.py <AmountOfNamesRequired> <emailAddress> <password>'
	print './RandomString.py 2 @something.com passw0rd'
	print 'Outputs: Num:0 pkthzjFirstgvdxjxLasthyx,pkthzjFirstgvdxjxLasthyx@something.com,passw0rd\n Num:1 akghqpFirsthkorcpLastibm,akghqpFirsthkorcpLastibm@something.com,passw0rd'
	print 'Outputs: int,"text","text","text","text","text","text","text","text"'

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

	rows = int(sys.argv[1])
		
	for num in range(0,rows):
		#Set 2 variables to contain random string length 6 to lowercase
		set =string.letters
		length = 6
		name1 = ''.join( [ random.SystemRandom().choice( set).lower() for _ in range( length) ] )
		name2 = ''.join( [ random.SystemRandom().choice( set).lower() for _ in range( length) ] )
		#Set 1 variables to contain random string length 3 to lowercase
		set =string.letters
		length = 3
		name3 = ''.join( [ random.SystemRandom().choice( set).lower() for _ in range( length) ] )
		print( "Num:%s %sFirst%sLast%s,%sFirst%sLast%s%s,%s" % (num +1, name1, name2, name3, name1, name2, name3, emailAddress, password ))
		
if __name__ == "__main__":
	main(sys.argv[1:])
