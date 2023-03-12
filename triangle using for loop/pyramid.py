height=int(input("enter height: "))
for row in range(1, height+1):
	print(" " * (height - row) +"* " * (row))