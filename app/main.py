
def main():
    print_menu()
    while True:
        option = choose_option()
        if option == 5:
            print("게임을 종료합니다.")
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
    option = int(input("선택: "))
    return option

def handle_option(option):
    if(option == 1) :
        print("퀴즈 풀기\n")
    elif(option == 2):
        print("퀴즈 추가\n")
    elif(option == 3):
        print("퀴즈 목록\n")
    elif(option == 4):
        print("점수 확인\n")
    elif(option == 5):
        print("종료\n")
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.\n")
        return False
    return True

if __name__ == "__main__":
    main()