# 두 수의 합을 반환하는 함수
def calculate_sum(a, b):
    return a + b

# 메인 함수
def main():
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    
    result = calculate_sum(num1, num2)
    print("두 수의 합은:", result)
 
   original_string = "Hello, World!"
   uppercase_string = to_uppercase(original_string)
   print(uppercase_string)


def to_uppercase(input_string):
    return input_string.upper()

