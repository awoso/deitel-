f = int(input("Enter number of series: "))
first = 0
second = 1
for f in range(f):
    print(first)
time = first
first = second
second = time + second
print(first)

number1 = 0
number2 = 1
count = 0

print("result: ", end=" ")
while count < 10:
    print(number1, end=" ")
    l = number1 + number2
    number1 = number2
    number2 = l
    count += 1
