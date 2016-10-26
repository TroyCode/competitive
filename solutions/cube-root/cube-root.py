def cubeRootNR(x):
	guess = 1
	epsilon = 0.01
	global ctr 
	ctr = 1
	while (abs(guess**3 - x) >= epsilon):
		guess = (x/guess**2 + 2*guess)/3
 		ctr += 1
 	return guess
 
number = float(raw_input("Enter a number: "))
ans = cubeRootNR(number)
print 'Cube root of', number , 'is about', ans, 'try', ctr, 'times' 