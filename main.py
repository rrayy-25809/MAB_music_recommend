from sklearn.neighbors import NearestNeighbors # 최근접 이웃 알고리즘을 위한 sklearn
import numpy as np # 배열 계산을 위한 넘파이
import json # json 파일을 불러오기 위한 json

class Music_MAB: #멀티 암드 밴딧 알고리즘을 담은 클래스 생성
    def __init__(self, epsilon:float = 1): # 생성자
        self.epsilon = epsilon # 탐색 비율
        self.user_status = [0, 0, 0, 0, 0] # 사용자 선호 상태 (bpm, danceability, classical, chill, bass)
        self.arms = json.load(open("genre.json", "r")) # 장르 리스트 (json 파일에서 불러옴)
        print(f"장르 리스트 : {self.arms}") # 장르 리스트 출력

        self.model = NearestNeighbors(n_neighbors=1, metric='euclidean') # 최근접 이웃 모델 생성
        
        print("모델 학습 완료")
            

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

    def update(self, reward_vector:list[float], user_input:int):
        self.epsilon *= 0.9  # 탐색 비율 점진적으로 줄이기
        self.user_status += user_input/10 * np.array(reward_vector)  # 사용자 상태 업데이트

model = Music_MAB() # 모델 생성

while True: # 무한 반복
    print("아래 추천 장르에 대해 점수를 매겨주세요")

    recommanded_genre:dict = model.select_arm() # 추천 장르 선택
    print(f"추천 장르 : {recommanded_genre["Genre"]}") # 추천 장르 출력
    user_input = int(input("점수 (1~10) : ")) # 사용자 점수 가져오기
    wanna_break = input("종료하시겠습니까? (y/n) : ")
    if wanna_break == "y":
        break # 사용자가 종료를 원하면 반복문 종료
    else:
        model.update(list(recommanded_genre.values())[1:],user_input) # 모델 업데이트

#TODO: 모델 업데이트 함수 구현하기, 모델 예측하기(거의 다 완성)