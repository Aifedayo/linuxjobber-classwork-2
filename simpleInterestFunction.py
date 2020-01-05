def main():
	simpleInterest(principal=int(input("Enter the Principal: ")), rate = float(input("Enter the rate: ")), time = int(input("Enter the time: ")))
	
def simpleInterest(principal,rate,time):
	interest = principal * time * rate
	print('The simple interest is', interest)
	
main()