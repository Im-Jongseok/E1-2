def print_double_line():
    print("=" * 30 + "\n")

def print_line():
    print("-" * 30 + "\n")

def get_valid_input(min_val, max_val, prompt):
     while True:
        try:
            raw = input(prompt)

            # 빈 입력 처리
            if raw.strip() == "":
                print("EMPTY INPUT ERROR: 값을 입력해주세요.")
                continue

            # 앞뒤 공백 제거 후 숫자 변환
            value = int(raw.strip())

            # 허용 범위 검사
            if not (min_val <= value <= max_val):
                print(f"RANGE ERROR: {min_val}~{max_val} 사이의 숫자를 입력해주세요.")
                continue

            return value

        except ValueError:
            print("TYPE ERROR: 숫자만 입력해주세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n EOF ERROR: 프로그램을 안전하게 종료합니다.")
            return EOFError
    