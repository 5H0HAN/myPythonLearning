#User Input Of How many numbers
n = int (input ("How many numbers : "))
sum = 0
#Loop for taking input
for i in range (0,n,1):
	num = float (input ("Enter number : " ))
	sum+=num
#Output
print ("The average is : ", sum/n)
