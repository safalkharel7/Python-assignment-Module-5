integer = int(input("Enter a positive integer: "))
if integer < 2:
    print("The integer is not a prime number")
else:
    for i in range(2, integer):
        if integer % i == 0:
            print("The integer is not a prime number")
            break
    else:
        print("The integer is  a prime number"