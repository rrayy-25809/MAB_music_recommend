from sklearn.linear_model import SGDRegressor # 확률적 경사 하강법 선형회귀 모델 (사용 가능성이 높은 모델)
from sklearn.multioutput import MultiOutputRegressor # 다중 출력 회귀 모델 (사용 가능성이 높은 모델)
import numpy as np # 배열 계산을 위한 넘파이

class MAB: #멀티 암드 밴딧 알고리즘을 담은 클래스 생성
    def __init__(self, arms, epsilon = 0.1): # 생성자
        self.model = MultiOutputRegressor(SGDRegressor()) # 다중 출력 회귀 모델 생성
        self.arms = arms # 팔을 담을 리스트 생성
        self.epsilon = epsilon # 탐색 비율
        self.counts = np.zeros(len(arms)) # 각 팔이 선택된 횟수
        self.values = np.zeros(len(arms)) # 각 팔의 평균 보상

    def select_arn():
        print("test") # 테스트 용 코드

    def update():
        print("test") # 테스트 용 코드