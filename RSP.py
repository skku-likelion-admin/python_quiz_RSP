
#### 가위바위보 게임 ####

"""
게임 조건
1. 컴퓨터와 1 대 1 상황
2. 3판 선승제
3. 간단한 인터페이스 구성 (ex. "가위, 바위, 보!"와 같은 말)
4. 함수 하나 이상 정의하여 사용
Hint) 'random' 라이브러리
"""

import random
import time         # 시간지연효과 sleep 함수 사용 위함.

# 함수 선언부
def RSPConverter(n) :
    if n == 1 :
        return "가위"
    elif n == 2 :
        return "바위"
    else:
        return "보"

def getRSPResult(user, com):
    # 전역변수 사용 위한 global 키워드
    global user_life
    global com_life

    diff = user - com
    if diff == 0:
        print("무승부")
    elif diff == -2 or diff == 1:
        user_life -= 1
        print("승리")
    else:
        com_life -= 1
        print("패배")

def showWinner(user_life, com_life):
    if user_life < com_life:
        print('당신의 승리!\n')
    else:
        print('당신의 패배!\n')


# 시작
user_life = 3
com_life = 3

print('가위바위보 게임을 시작합니다.')

while user_life > 0 and com_life > 0 :
    user_choice = int(input("당신의 선택은?\n1. 가위  2. 바위  3. 보\n>>"))
    com_choice = random.choice([1, 2, 3])

    print('가위, 바위, 보!')
    time.sleep(1)   # 1초 텀

    print(f'당신: {RSPConverter(user_choice)}\n상대: {RSPConverter(com_choice)}')
    time.sleep(1)   # 1초 텀
    
    getRSPResult(user_choice, com_choice)

showWinner(user_life, com_life)