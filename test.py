def getinput() :

	# Prompt user for input
#	print("Enter numbers (Ctrl+D to stop):")
	
#	cont = []
	
	# Read from input and store to the array cont[]
#	while True:
#		try:
#			line = raw_input("")
#		except EOFError :
#			break
#		cont.append(line)

	print("Enter filename then press Ctrl+D:")
	filename = []

	while True:
		try:
			line = raw_input("")
		except EOFError :
			break
		filename.append(line)

	rawContents = open(filename[0],"r")
	cont =  rawContents.read().split("\n")
	cont.remove("")	
	rawContents.close()
	
	return cont
	
# main	
	
contents = getinput()

# convert all elements from string to int	
contents = [int(i) for i in contents]

#transfer contents to arrays a, b and k
a = contents[1::3]
b = contents[2::3]
k = contents[3::3]

# create results array with size equal to number of cases and initialize it to 0
results = [0 for c in xrange(contents[0])]

# check range of a to b. if there's a number divisible by k, results is incremented
for i in xrange(contents[0]) :
	for j in xrange(a[i],(b[i]+1)) :
		if (j%k[i]) == 0 :
			results[i] += 1

writeout = open("output.out","w")				
#ryt = open("out.out","w")
				
#print results				
for l in xrange(len(results)) :
	print("Case %d: %d") % ((l+1),results[l])
	writeout.write(("Case %d: %d") % ((l+1),results[l]) + "\n")
#	ryt.write(str(results[l]) + "\n")
	
writeout.close()	
#ryt.close()

	
	
	
