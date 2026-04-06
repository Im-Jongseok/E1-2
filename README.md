# Git과 함께하는 Python 첫 발자국

## 프로젝트 개요

파이썬을 사용해 터미널에서 동작하는 나만의 퀴즈 게임 만들기.
  
### 프로젝트 목표

- Python 기초 및 OOP 이해
- 파일 I/O와 JSON 처리
- 예외 처리
- Git 기본 워크플로우 이해 및 사용

### 기능 목록

- 주요 기능: 퀴즈 출제/ 등록/ 목록/ 점수 확인/ 종료 
- 추가 기능: 랜덤 출제/ 문제 수 선택/ 힌트 기능/ 퀴즈 삭제 기능/ 점수 기록 히스토리

- 저장 방식: `state.json` 파일에 퀴즈 데이터와 최고 점수를 저장 (UTF-8)

### 퀴즈 주제 및 선정 이유

#### 주제
* 인간-이종석

#### 선정 이유
* 퀴즈를 푼 사람들이 "이종석"이라는 인간을 조금 더 알아가고 친해지는 기회가 되길 희망.

---

### 실행 환경

| 항목 | 내용 |
| --- | --- |
| Shell | bash |
| Python 버전 | 3.11 |
| 인코딩 | UTF-8 |
| Git | 2.53.0 |
| Docker | 28.5.2 |
| 실행 커맨드 | `python main.py` |

### 실행 방법

1. 리포지터리 루트로 이동
2. Python 실행

```bash
python main.py
```

---

### 파일 구조

프로젝트 구조 예시:

필요 시 다음과 같이 패키지 구조도 확장 가능합니다:

```
E1-2/
├─ app/
│  ├─ main.py       # 프로그램진입점
│  ├─ Quiz.py       # Quiz 클래스
│  ├─ QuizGame.py   # QuizGame 클래스
│  ├─ Logger.py     # Logger 클래스
│  └─ state.json    # 저장된 퀴즈 + 최고 점수 + 기록
├─ img/             # README 이미지 폴더
├─ docker-compose.yml 
├─ .gitignore 
└─ README.md
```

### 클래스 구조

#### Quiz class -> 퀴즈 구성 내용
* 퀴즈 문제
* 퀴즈 선택지
* 퀴즈 정답 및 확인 

#### QuizGame class -> 게임 작동 필요한 기능
* 메뉴 출력 및 선택 기능
* 퀴즈 풀기/ 추가/ 목록
* Json 읽고/ 쓰기 (퀴즈 불러오기, 점수 확인/ 저장)

#### Logger class -> 로그 기록에 필요한 기능
* 로그 기록 저장 메소드

### 데이터 파일 설명(state.json)

저장 경로: 프로젝트 루트 `state.json`

스키마 예시:

```json
{
  "player_cnt": 0
  "quizzes": [
    {
      "question": "예제 질문",
      "choices": ["선택1", "선택2", "선택3", "선택4"],
      "answer": 1
    }
  ],
  "top_point": 0,
  "history" : [
    {
        "player": "플레이어 이름",
        "logs": [
            "[19:07:17] === 게임 시작 [2026-04-06 19:07:17] ===",
            "[19:08:14] Player 1 → 메뉴 선택: 점수 확인",
            "[19:08:16] Player 1 → 메뉴 선택: 퀴즈 목록",
            "[19:08:57] Player 1 → 메뉴 선택: 퀴즈 추가",
            "[19:10:07] Player 1 → 퀴즈 추가: [이종석의 직업은?]",
            "[19:12:10] Player 1 → 메뉴 선택: 퀴즈 목록"
        ]
    }
  ]
}
```

경로: /E1-2/app/state.json

- `quizzes`: quiz 리스트 (문제, 선택지 4개, 정답 1~4)
- `top_point`: 이전 최고 점수
- `history`: 게임 기록

---

### 프로그램 실행 결과 스크린샷

<img src="img/menu.png" width="300" height="500" alt="퀴즈 게임 실행">
<img src="img/1.png" width="300" height="500" alt="퀴즈 게임 실행">
<img src="img/1-2.png" width="300" height="500" alt="퀴즈 게임 실행">
<img src="img/2.png" width="300" height="500" alt="퀴즈 게임 실행">
<img src="img/3-5.png" width="300" height="500" alt="퀴즈 게임 실행">
<img src="img/4.png" width="300" height="500" alt="퀴즈 게임 실행">

### git log --oneline --graph  결과

<img src="img/git.png" width="500" height="300" alt="git log --oneline --graph">

### 체크리스트

- [x] 메뉴 표시
- [x] 퀴즈 풀기/ 추가/ 목록 (기본 퀴즈 5개 이상 포함)

- [x] 메뉴 입력 검증 (숫자, 범위, 빈 입력 등)
- [x] `KeyboardInterrupt`, `EOFError` 처리
- [x] 파일 없음/손상 시 기본 데이터 복원

- [x] 퀴즈 데이터 json 파일에 저장 및 불러오기

- [x] Git 10회 이상 커밋
- [x] 브랜치 작업 (git log --oneline --graph)
- [x] 기초 명령어 7종( init ,  add ,  commit ,  push ,  pull ,  checkout ,  clone )을 각각 한 번 이상 사용
- [x] clone, pull 실습