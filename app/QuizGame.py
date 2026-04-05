from Quiz import Quiz

# QuizGame 클래스
class QuizGame:
    def __init__(self):
        self._quizzes = self._default_quizzes()
        self._top_score = -1

    # ------------ utils ------------ 
    # 구분선 출력
    def print_double_line(self):
        print("=" * 30 + "\n")

    def print_line(self):
        print("-" * 30 + "\n")

    # 입력 유효성 검사
    def get_valid_input(self, min_val, max_val, prompt):
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

    # ------------ value 관련 메서드 ------------
    # 퀴즈 기본 데이터
    def _default_quizzes(self):
        return [
            Quiz(
                "피평가자의 이름은?",
                ["이종석", "김현석", "김태환", "이태민"],
                1,
            ),
            Quiz(
                "이종석의 출생 연도는?",
                ["1998년", "2000년", "2002년", "2004년"],
                3,
            ),
            Quiz(
                "이종석의 mdti는?",
                ["INTJ", "INTP", "ESTP", "ISFP"],
                1,
            ),
            Quiz(
                "이종석의 취미는?",
                ["음악 감상", "게임", "운동", "독서"],
                4,
            ),
            Quiz(
                "이종석의 키는?",
                ["175cm", "180cm", "185cm", "190cm"],
                3,
            ),
        ]

    # 최고 점수 저장
    def top_score(self):
        return self._top_score

    # 퀴즈 길이
    def get_quiz_len(self):
        return len(self._quizzes)


    # ------------ 게임 실행 ------------
    # 게임 실행
    def run(self):
        self.print_menu()
        while True:
            option = self.choose_option()
            if option == 5 :
                print("게임을 종료합니다.")
                break
            elif option == EOFError:
                break

            self.handle_option(option)

    # 1. 퀴즈 플레이
    def play(self): 
        self.print_line()
        print(f"퀴즈를 시작합니다!(총 {self.get_quiz_len()}문제)")
        self.print_line()

        score = 0
        for quiz in self._quizzes:
            self.print_quiz(quiz)                        # 퀴즈 출력
            score = self.player_score(quiz, score)       # 플레이어 점수 계산
        self.print_score(self.get_quiz_len(), score)      # 최종 점수 출력


    # ------------ 메뉴 관련 메서드 ------------
    # 메뉴 출력
    def print_menu(self):
        self.print_double_line()
        print("   퀴즈 게임\n")
        self.print_double_line()
        print("1. 퀴즈 풀기\n")
        print("2. 퀴즈 추가\n")
        print("3. 퀴즈 목록\n")
        print("4. 점수 확인\n")
        print("5. 종료\n")
        self.print_double_line()

    # 메뉴 선택
    def choose_option(self):
        option = self.get_valid_input(1, 5, "옵션 선택: ")
        return option

    # 메뉴 옵션 처리
    def handle_option(self, option):
        if(option == 1) :
            self.play()
        elif(option == 2):
            self.add_quiz()
        elif(option == 3):
            self.print_quiz_list()
        elif(option == 4):
            self.print_top_score()
        elif(option == 5):
            print("종료")
        return True     



    # ------------ 퀴즈 관련 메서드 ------------
    # 퀴즈 출력
    def print_quiz(self, quiz):
        print(quiz.question + "\n")

        for i, choice in enumerate(quiz.choices):
            print(f"{i+1}. {choice}")
        print() 

    # 2. 퀴즈 추가 
    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.\n")
        # question 
        question = input("문제를 입력하세요: ")         

        # choices
        choices = []                                
        for i in range(4):                          
            choice = input(f"선택지 {i+1}: ")
            choices.append(choice)

        # answer
        answer = self.get_valid_input(1, 4, "정답 번호 (1-4): ")    

        new_quiz = Quiz(question, choices, answer) # Quiz 클래스의 인스턴스로 퀴즈 생성
        self._quizzes.append(new_quiz)
        print("퀴즈가 추가되었습니다!\n")

    #  3. 퀴즈 목록 
    def print_quiz_list(self):
        self.print_line()
        print(f"등록된 퀴즈 목록 (총 {self.get_quiz_len()}문제):\n")
        self.print_line()

        for i, quiz in enumerate(self._quizzes):
            print(f"[{i+1}] {quiz.question}")
        print()


    # ------------ 점수 관련 메서드 ------------
    # 플레이어 점수 계산
    def player_score(self, quiz, score):
        player_answer = self.get_valid_input(1, len(quiz.choices), "정답 입력: ")
        
        if quiz.check_answer(player_answer):
            print("정답입니다!\n")
            score += 1
        else:
            print(f"틀렸습니다! 정답은 {quiz.answer}번입니다.\n")
        self.print_line()
        return score

    # 최종 점수 출력
    def print_score(self, quiz_len, score):
        self.print_double_line()

        point = int(score / self.get_quiz_len() * 100)     # 개수 환산
        print(f"결과: {self.get_quiz_len()}문제 중 {score}문제 정답! ({point}점)\n")

        if self.is_top_score(point):
            print("새로운 최고 점수입니다!\n")

        self.print_double_line()

    # 최고 점수 갱신
    def is_top_score(self, score):
        if self._top_score < score:
            self._top_score = score
            return 1
        return 0

    # 4. 점수 확인
    def print_top_score(self):
        if self._top_score == -1:
            print("EMPTY SCORE ERROR: 점수가 없습니다.\n")
            return
        score = int((self._top_score / 100) * self.get_quiz_len())  # 점수 환산
        print(f"최고 점수: {self._top_score} 점 ({self.get_quiz_len()}문제 중 {score}문제 정답)\n")

