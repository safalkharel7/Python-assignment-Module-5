numbers = []
num = input("Enter a number: ")
while num != "":
    numbers.append(int(num))
    num = input("Enter another number: ")
numbers.sort(reverse=True)
top5 = numbers[:5]
print("The five highest numbers are: ", top5