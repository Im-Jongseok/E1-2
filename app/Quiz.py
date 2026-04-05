class Quiz:
    def __init__(self, question, choices, answer):  # 퀴즈 클래스 초기화
        self.question = question    # 퀴즈 질문
        self.choices = choices      # 리스트 선택지 ["선택지1", "선택지2", "선택지3", "선택지4"]
        self.answer = answer        # 퀴즈 정답

    def __str__(self):  # 퀴즈 객체를 문자열로 표현하는 메소드
        choices_str = "\n".join(
            [f"{i+1}. {choice}" for i, choice in enumerate(self.choices)])
        return f"{self.question}\n{choices_str}"

    def check_answer(self, user_answer): # 사용자가 입력한 답이 정답과 일치하는지 확인하는 메소드
        return user_answer == self.answer
