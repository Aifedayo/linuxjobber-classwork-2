# Checking for Palindrome

var = input('Enter a string here to check if it is a palindrome: ')
reverse = str(var)[::-1]

if var == reverse:
	print('String entered is a palindrome')

else:
	print("String entered is NOT a palindrome")