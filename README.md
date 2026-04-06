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

주제: 인간-이종석

선정 이유: 퀴즈를 푼 사람들이 "이종석"이라는 인간을 조금 더 알아가고 친해지는 기회가 되길 희망.

## 실행 환경

| 항목 | 내용 |
| --- | --- |
| OS |  |
| Shell | bash |
| Python 버전 | 3.11 |
| 인코딩 | UTF-8 |
| Git | 2.53.0 |
| Docker | 28.5.2 |
| 실행 커맨드 | `python main.py` |

## 실행 방법

1. 리포지터리 루트로 이동
2. Python 실행

```bash
python main.py
```

## 파일 구조

프로젝트 구조 예시:

필요 시 다음과 같이 패키지 구조도 확장 가능합니다:

```
E1-2/├
├─ app/
│  ├─ __init__.py
│  ├─ main.py       # 프로그램진입점
│  ├─ quiz.py       # Quiz, QuizGame 클래스
│  └─ game.py
├─ data/
│  └─ state.json    # 저장된 퀴즈 + 최고 점수
├─ docker-compose.yml 
└─ README.md
```


## 데이터 파일 설명(state.json)

저장 경로: 프로젝트 루트 `state.json`

스키마 예시:

```json
{
  "quizzes": [
    {
      "question": "예제 질문",
      "choices": ["선택1", "선택2", "선택3", "선택4"],
      "answer": 1
    }
  ],
  "best_score": 0
}
```

- `quizzes`: quiz 리스트 (문제, 선택지 4개, 정답 1~4)
- `best_score`: 이전 최고 점수



## 프로그램 실행 결과 스크린샷


## git log --oneline --graph  결과



## 체크리스트

- [ ] 기본 퀴즈 5개 이상 포함
- [ ] 메뉴 입력 검증 (숫자, 범위, 빈 입력 등)
- [ ] 파일 없음/손상 시 기본 데이터 복원
- [ ] `KeyboardInterrupt`, `EOFError` 처리
- [ ] Git 커밋 & 브랜치 활용 (10회 이상 커밋, 브랜치 작업 포함)
- [ ] 기초 명령어 7종( init ,  add ,  commit ,  push ,  pull ,  checkout ,  clone )을
각각 한 번 이상 사용