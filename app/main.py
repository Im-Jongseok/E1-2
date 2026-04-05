
def main():
    print_menu()
    while True:
        option = choose_option()
        if option == 5 :
            print("게임을 종료합니다.")
            break
        elif option == EOFError:
            break

        handle_option(option)

    return 0

def print_menu():
    print("==============================\n")
    print("   퀴즈 게임\n")
    print("==============================")
    print("1. 퀴즈 풀기\n")
    print("2. 퀴즈 추가\n")
    print("3. 퀴즈 목록\n")
    print("4. 점수 확인\n")
    print("5. 종료\n")
    print("==============================\n")

def choose_option():
    option = get_valid_input(1, 5, "옵션 선택: ")
    return option

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
    
def handle_option(option):
    if(option == 1) :
        print("퀴즈 풀기")
    elif(option == 2):
        print("퀴즈 추가")
    elif(option == 3):
        print("퀴즈 목록")
    elif(option == 4):
        print("점수 확인")
    elif(option == 5):
        print("종료")
    return True

if __name__ == "__main__":
    main()