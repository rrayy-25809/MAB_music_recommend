from sklearn.linear_model import SGDRegressor # 확률적 경사 하강법 선형회귀 모델 (사용 가능성이 높은 모델)
from sklearn.multioutput import MultiOutputRegressor # 다중 출력 회귀 모델 (사용 가능성이 높은 모델)
import numpy as np # 배열 계산을 위한 넘파이

class Music_MAB: #멀티 암드 밴딧 알고리즘을 담은 클래스 생성
    def __init__(self, epsilon:float = 1): # 생성자
        self.epsilon = epsilon # 탐색 비율
        self.user_status = [0, 0, 0, 0, 0] # 사용자 선호 상태 (bpm, danceability, classical, chill, bass)
        self.arms = ["pop", "rock", "hiphop", "jazz", "classic", "dubstep", "mainstage", "house", "metal"] # 장르 리스트 (추가 예정)

        x = np.array([[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]) # 사용자 선호 상태에 대한 예시 데이터
        y = np.random.rand(3, len(self.arms)) # 장르 보상값에 대한 예시 데이터

        self.model:MultiOutputRegressor = MultiOutputRegressor(SGDRegressor()) # 다중 출력 회귀 모델 생성
        self.model.fit(x, y) # 모델 학습

    def select_arm(self):
        print(f"현재 탐색 비율 : {self.epsilon}") # 현재 탐색 비율 출력
        print(f"현재 사용자 상태 : {self.user_status}")

        if np.random.rand() < self.epsilon:
            # 탐색: 랜덤 arm 선택
            return np.random.choice(self.arms)
        else:
            # 활용: 보상 예측 기반 arm 선택
            prediction = self.model.predict([self.user_status])[0]  # 1D로 반환됨
            print(f"예측된 보상 : {prediction}")
            return self.arms[np.argmax(prediction)]

    def update(self, reward_vector:list[float]):
        self.epsilon *= 0.9  # 탐색 비율 점진적으로 줄이기
        # for i, reg in enumerate(self.model.estimators_):
        #     reg.partial_fit([self.user_status], [reward_vector[i]])  # 2D 형태로 전달

model = Music_MAB() # 모델 생성

while True: # 무한 반복
    print("아래 추천 장르에 대해 점수를 매겨주세요")

    recommanded_genre = model.select_arm() # 추천 장르 선택
    print(f"추천 장르 : {recommanded_genre}") # 추천 장르 출력
    user_input = int(input("점수 (1~10) : ")) # 사용자 점수 가져오기
    wanna_break = input("종료하시겠습니까? (y/n) : ")
    if wanna_break == "y":
        break # 사용자가 종료를 원하면 반복문 종료
    else:
        model.update([0.1,0.1,0.1,0.1,0.1]) # 모델 업데이트

#TODO: 모델 업데이트 함수 구현하기, 모델 학습하기, 모델 예측하기(거의 다 완성)