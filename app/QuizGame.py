from Quiz import Quiz
from random import shuffle
import json
import os

# QuizGame 클래스
class QuizGame:
    def __init__(self):
        self._top_score = -1
        self._file_path = "./state.json"    # JSON 파일 경로
        self._quizzes = self.load_json()    # JSON 파일에서 퀴즈 데이터 로드
        self.save_json()                    # JSON 파일에 퀴즈 데이터 저장 (최초 실행 시 기본 퀴즈로 초기화)

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

    # ------------ JSON ------------
    # read JSON 
    def load_json(self):
        if not os.path.exists(self._file_path):
            print(f"FILE NOT FOUND ERROR: '{self._file_path}' 파일이 존재하지 않아 읽을 수 없습니다. 기본 퀴즈로 복구합니다.")
            return self._default_quizzes()
        try:
            with open(self._file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._top_score = data.get("top_score", -1)  # 최고 점수 로드
                quizzes = data.get("quizzes", [])

            # quizzes가 비어있으면 기본 퀴즈 반환
            if not quizzes:
                return self._default_quizzes()

            return [Quiz(**quiz) for quiz in quizzes]  # JSON -> **quiz 딕셔너리 -> Quiz() 객체로 변환
    
        except json.JSONDecodeError:
            print(f"JSON DECODE ERROR: '{self._file_path}' 파일이 손상되어 읽을 수 없습니다. 기본 퀴즈로 복구합니다.")
            return self._default_quizzes()
        except PermissionError:
            print(f"PERMISSION ERROR: '{self._file_path}' 파일에 접근 권한이 없어 읽을 수 없습니다. 기본 퀴즈로 복구합니다.")
            return self._default_quizzes()  
        except IsADirectoryError:
            print(f"IS A DIRECTORY ERROR: '{self._file_path}' 경로가 디렉토리임으로 읽을 수 없습니다. 기본 퀴즈로 복구합니다.")
            return self._default_quizzes()

    # write JSON
    def save_json(self):
        try:
            with open(self._file_path, 'w', encoding='utf-8') as f:
                data = {
                    "quizzes": [quiz.__dict__ for quiz in self._quizzes],  # Quiz 객체를 딕셔너리로 변환
                    "top_score": self._top_score  # 최고 점수 저장
                }
                json.dump(data, f, ensure_ascii=False, indent=4) # JSON 파일로 저장

        except json.JSONDecodeError:
            print(f"JSON DECODE ERROR: '{self._file_path}' 파일이 손상되어 저장할 수 없습니다.")
            return self._default_quizzes()
        except PermissionError:
            print(f"PERMISSION ERROR: '{self._file_path}' 파일에 접근 권한이 없어 저장할 수 없습니다.")
            return self._default_quizzes()  
        except IsADirectoryError:
            print(f"IS A DIRECTORY ERROR: '{self._file_path}' 경로가 디렉토리임으로 저장할 수 없습니다.")
            return self._default_quizzes()
        
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
        quiz_cnt = self.choose_quiz_cnt()                # 플레이할 퀴즈 개수 선택 (보너스 과제)

        self.print_line()
        print(f"퀴즈를 시작합니다!(총 {quiz_cnt}문제)")
        self.print_line()

        score = 0
        shuffle(self._quizzes)                           # 퀴즈 순서 섞기 (보너스 과제)
        for quiz in self._quizzes[:quiz_cnt]:            # 선택한 개수만큼 퀴즈 풀기
            self.print_quiz(quiz)                        # 퀴즈 출력
            score = self.player_score(quiz, score)       # 플레이어 점수 계산
        self.print_score(self.get_quiz_len(), quiz_cnt, score)     # 최종 점수 출력



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
        self.save_json()                           # JSON 파일에 퀴즈 저장
        print("퀴즈가 추가되었습니다!\n")

    #  3. 퀴즈 목록 
    def print_quiz_list(self):
        self.print_line()
        print(f"등록된 퀴즈 목록 (총 {self.get_quiz_len()}문제):\n")
        self.print_line()

        for i, quiz in enumerate(self._quizzes):
            print(f"[{i+1}] {quiz.question}")
        print()

    # 퀴즈 개수 선택
    def choose_quiz_cnt(self):
        return self.get_valid_input(1, self.get_quiz_len(), "플레이할 퀴즈 개수를 입력하세요: ")
    

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
    def print_score(self, quiz_len, quiz_cnt, score):
        self.print_double_line()

        point = self.calculate_score(quiz_len, quiz_cnt, score)   # 점수 계산
        print(f"[ 결과 ]\n {self.get_quiz_len()} 문제 중 {quiz_cnt} 문제 풀기!\n\n {score} 문제 정답! ({point} 점)\n")

        if self.is_top_score(point):
            print("새로운 최고 점수입니다!\n")

        self.print_double_line()

    # 최종 점수 계산
    def calculate_score(self, max_total, total, score):
        # 정답 비율
        ratio = score / total

        # 문제 수 가중치
        weight = total / max_total

        return int(ratio * weight * 100)

    # 최고 점수 갱신
    def is_top_score(self, score):
        if self._top_score < score:
            self._top_score = score
            self.save_json()            # JSON 파일에 최고 점수 저장
            return 1
        return 0

    # 4. 점수 확인
    def print_top_score(self):
        if self._top_score == -1:
            print("EMPTY SCORE ERROR: 점수가 없습니다.\n")
            return
        score = int((self._top_score / 100) * self.get_quiz_len())  # 점수 환산
        print(f"최고 점수: {self._top_score} 점 총 ({self.get_quiz_len()} 문제 중 {score} 문제 정답)\n")

