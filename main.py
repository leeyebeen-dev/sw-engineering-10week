def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # 출력: True
print(is_even(7))  # 출력: False

def to_uppercase(input_string):
    return input_string.upper()

original_string = "Hello, World!"
uppercase_string = to_uppercase(original_string)
print(uppercase_string)
