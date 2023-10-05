# password = input("enter your password:")
# hidden_password = len(password) * "*"
# print(hidden_password)
#
#
# num1 = 1
# num2 = 2
# print(num1 + num2)
#
# num1 = float(1)
# num2 = 2
# print(num1 + num2)
#
# print(2 +3 * 4 / 2 ** 4)

# message1 = 'hello'
# message1 = 'welcome'
# message1 = 'xplorers'
# msg = f'{message1 + "how are you"}\n{message2}\n{message3}'
#
# print(message1 + ' ' + message2 + ' ' + message3, end='\t')

# MULTI LINE STRING
# long_string = """
#                   alfred and joy
#                   ope and qudus
#                   dike and melody"""
# print(long_string)
#
# print(f"""
#                   alfred and joy
#                   ope and qudus
#                   dike and melody""")
#
# age = int(input("Enter an age:"))
# if age < 18:
#     print("you are not eligible to enter our club...")
# if age >= 18:
#     print("you are eligible to our club...")
# if age > 65:
#     print("stay home...")
#
# age = int(input("Enter an age:"))
# if age < 18:
#     print("you are not eligible to enter our club...")
# if age >= 18 and  age <= 65:
#     print("you are eligible to our club...")
# if age > 65:
#     print("stay home..."

# number1 = int(input("Enter a number:"))
# number2 = int(input("Enter a number:"))
# number3 = int(input("Enter a number:"))
#
# if number1 > number2 and number3:
#     print(number1)
# if number2 > number1 and number3:
#     print(number2)
# if number3 > number1 and number2:
#     print(number3)


number_one = int(input("Enter first number:"))
number_two = int(input("Enter second number"))
number_three = int(input("Enter third number"))

if number_one > number_two and number_one > number_three:
    print("Number_one is the highest!")
if number_two > number_one and number_two > number_three:
    print("Number_two is highest!")
if number_three > number_one and number_three > number_two:
    print("Number_three is highest!")