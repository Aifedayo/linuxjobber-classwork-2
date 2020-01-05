def getGrade(score):

	if score <= 39:
		print('F')
	elif score >= 40 and score <= 44:
		print('E')
	elif score >= 45 and score <= 49:
		print ('D')
	elif score >=50 and score <= 59:
		print('C')
	elif score >= 60 and score <= 69:
		print('B')
	elif score >= 70 and score <= 100:
		print('A')
	else:
		print('Your input is more than the required score')
	
getGrade( int(input("Enter your score to know your grade: ")))