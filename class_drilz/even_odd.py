even_count = 0

odd_count = 0
#
# for i in range(8):
#
#   while i < 8:
#
#     print("i")
#
#     print(i, end=" \t")
#
#      count += 1:

# while odd_count >8:

#     print("i")


# even_count = 0
# odd_count = 0
#
# numbers = input("Enter a series of numbers: ")
#
# number_list = numbers.split()
#
# for num in number_list:
#
#
#     num = int(num)
#
#     if num % 2 != 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
#     print(f"Even numbers: {even_count}")
#     print(f"Odd numbers: {odd_count}")


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = 0
odd = 0

for num in num:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers:", even)
print("Number of odd numbers:", odd)