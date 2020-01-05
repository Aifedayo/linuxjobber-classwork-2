#Creating a prime number

def isPrime(n):

		for i in range (2, n):
			if n%i== 0:
				print(n, 'is not a prime number')
				break
		else:
			print(n, 'is a prime number')

prime = isPrime(int(input("Enter a number to verify if it is prime or Not: ")))

print(prime)