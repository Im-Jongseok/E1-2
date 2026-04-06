# log.py
from datetime import datetime

class Logger:
    def __init__(self, player_name):
        self._player_name = player_name
        self._logs = []
        self._session_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._log(f"=== 게임 시작 [{self._session_start}] ===")

    def _log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        record = f"[{timestamp}] {message}"
        self._logs.append(record)

    # 메뉴 선택 로그
    def log_menu(self, option_name):
        self._log(f"{self._player_name} → 메뉴 선택: {option_name}")

    # 퀴즈 추가 로그
    def log_add_quiz(self, question):
        self._log(f"{self._player_name} → 퀴즈 추가: [{question}]")

    # 퀴즈 삭제 로그
    def log_remove_quiz(self, question):
        self._log(f"{self._player_name} → 퀴즈 삭제: [{question}]")

    # 퀴즈 풀기 시작 로그
    def log_play_start(self, quiz_cnt):
        self._log(f"{self._player_name} → 퀴즈 풀기 시작 ({quiz_cnt}문제 선택)")

    # 문제 풀기 로그
    def log_quiz_answer(self, question, user_answer, correct_answer, is_correct):
        result = "정답" if is_correct else "오답"
        self._log(f"{self._player_name} → [{question}] 선택: {user_answer}번 / 정답: {correct_answer}번 → {result}")

    # 힌트 사용 로그
    def log_hint(self, hint):
        self._log(f"{self._player_name} → 힌트 사용: [{hint}]")

    # 최고 점수 로그
    def log_top_point(self, top_point):
        self._log(f"{self._player_name} → 현재 최고 점수: {top_point}")

    # 결과 로그
    def log_result(self, quiz_cnt, score, point, is_top):
        top = "최고 점수 갱신!" if is_top else ""
        self._log(f"{self._player_name} → 결과: {quiz_cnt}문제 중 {score}문제 정답 ({point}점) {top}")

    # 게임 종료 로그
    def log_exit(self):
        self._log(f"=== 게임 종료 [{self._player_name}] ===")

    # 전체 로그 반환
    def get_logs(self):
        return self._logs