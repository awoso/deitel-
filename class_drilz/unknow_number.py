total = 0
count = 0
score = int(input("Enter student score or -1 to stop: "))
while score != -1:
    total += score
    count += 1
    score = int(input("Enter student score or -1 to stop: "))
average = total / count
print(f"{average:.2f}")