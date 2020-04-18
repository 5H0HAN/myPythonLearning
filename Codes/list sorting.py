case = int (input("case no :"))
arr = []
for a in range(0,case,1):
	print("Case",a+1)
	ele_n = int (input("Element no for case:"))
	
	for i in range (0,ele_n,1):
		i = int (input("Elements : "))
		arr.append (i)
	arr.sort()
	print (arr)
	arr.clear()