height=int(input("Enter height you want: "))
for row in range(1, height+ 1):
	print(" " * (height - row) +"*" * row)

