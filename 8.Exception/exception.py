def execption_numbers():
    try:
        # 사용자로부터 숫자 입력
        numerator = float(input("분자를 입력하세요: "))
        denominator = float(input("분모를 입력하세요: "))

        # 나누기 연산
        result = numerator / denominator

    except ValueError:
        # 입력 값이 숫자가 아닐 경우 처리
        print("유효한 숫자가 아닙니다.");
    except ZeroDivisionError:
        # 분모가 0일 경우 처리
        print("0으로 나눌 수 없습니다.");
    else:
        # 예외가 발생하지 않을 경우
        print(f"결과: {result}");
    finally:
        # 항상 실행되는 코드
        print("계산 완료!.");
# 함수 호출
execption_numbers()