import sys

try:
	fout = open("/etc/apt/apt.conf",'w')
except IOError:
	print "Bro! you can't access it"
	sys.exit()

try:
	fin = open("university_proxy.in",'r')
except IOError:
	print "university_proxy.in doesnot exist"
	sys.exit()

if sys.argv[1] == "on":
	arr = fin.read().split("\n")

	for proxies in arr:
		fout.write(proxies + "\n")

elif sys.argv[1] == "off":
	fout.write("")

else:
	print "invalid operation"
