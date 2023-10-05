def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[ ::-1]

num = 12321
result =is_palindrome(num)
print(f"{num} is a palindrome :{result}")
