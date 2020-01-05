#Creating a prime number

my_list=  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in (my_list):
	if num>1:
		for i in range (2, num):
			if num%i== 0:
				print(num, 'is not a prime')
				break
		else:
			print(num, 'is a prime number')