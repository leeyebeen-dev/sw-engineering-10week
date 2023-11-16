# 두 수의 합을 반환하는 함수
def calculate_sum(a, b):
    return a + b

# 메인 함수
def main():
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    
    result = calculate_sum(num1, num2)
    print("두 수의 합은:", result)

# 메인 함수 실행
if __name__ == "__main__":
    main()

