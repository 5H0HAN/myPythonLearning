def digit(num):
	cout = 0
	while num > 0:
		num = num//10
		cout +=1
	print ("Total Digit number is ",cout)



z = int (input ("Enter total check points : "))	
	
for i in range (0,z,1):
 
	x = int (input ("Enter a number : "))

	digit (x)
	
