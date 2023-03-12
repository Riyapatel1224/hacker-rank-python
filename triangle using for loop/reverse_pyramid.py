height=int(input("enter height: "))
for row in range(1, height+1):
	print(" " * (row) +"* " * (height-row+1))
	