def percent():
	""" This is used to find percentage by getting full marks
	Make this function to be applicable to find pecentage of every subject"""
	percentage=(int(marks)/int(total))*100
	print("\nYour percentage is",percentage)

print("Percentage Finder\n")
while True:
	print("Enter ! for quit\n")
	marks=input("Enter total marks you obtained\n")

	if marks == '!':
		break
	
	total=input("\nEnter Total marks of exam\n")
	
	percent()		
	
