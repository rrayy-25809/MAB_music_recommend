from sklearn.linear_model import SGDRegressor # 확률적 경사 하강법 선형회귀 모델 (사용 가능성이 높은 모델)
from sklearn.multioutput import MultiOutputRegressor # 다중 출력 회귀 모델 (사용 가능성이 높은 모델)
import numpy as np # 배열 계산을 위한 넘파이

class MAB: #멀티 암드 밴딧 알고리즘을 담은 클래스 생성
    def __init__(self, arms, epsilon:float = 1): # 생성자
        self.model = MultiOutputRegressor(SGDRegressor()) # 다중 출력 회귀 모델 생성
        self.arms = arms # 팔을 담을 리스트 생성
        self.epsilon = epsilon # 탐색 비율
        self.counts = np.zeros(len(arms)) # 각 팔이 선택된 횟수
        self.values = np.zeros(len(arms)) # 각 팔의 평균 보상

    def select_arn(self):
        if self.epsilon >= np.random.rand:
            return np.random.choice(self.arms) # 탐색 비율이 랜덤값보다 크면 랜덤으로 선택
        else:
            return "모듈을 만들어서 값 예측하기"

    def update(self):
        self.epsilon = self.epsilon * 0.99 #탐색 비율 감소
        # self.model.fit()

model = MAB([1, 2, 3]) # MAB 클래스의 인스턴스 생성

while True: # 무한 반복
    print("아래 추천 장르에 대해 점수를 매겨주세요")
    print(model.select_arn()) # 추천 장르 출력
    user_input = int(input("점수 : ")) # 사용자 점수 가져오기
    wanna_break = input("종료하시겠습니까? (y/n) : ")
    if wanna_break == "y":
        break # 사용자가 종료를 원하면 반복문 종료
    else:
        model.update() # 모델 업데이트

#TODO: 모델 업데이트 함수 구현하기, 모델 학습하기, 모델 예측하기