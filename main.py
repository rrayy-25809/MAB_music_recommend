from sklearn.neighbors import NearestNeighbors # 최근접 이웃 알고리즘을 위한 sklearn
import numpy as np # 배열 계산을 위한 넘파이
import json # json 파일을 불러오기 위한 json

class Music_MAB: #멀티 암드 밴딧 알고리즘을 담은 클래스 생성
    def __init__(self, epsilon:float = 1): # 생성자
        self.epsilon = epsilon # 탐색 비율
        self.user_status = np.array([0.0, 0.0, 0.0, 0.0, 0.0]) # 사용자 선호 상태
        self.arms = json.load(open("genre.json", "r")) # 장르 리스트 (json 파일에서 불러옴)

        self.model = NearestNeighbors(n_neighbors=1, metric='euclidean') # 최근접 이웃 모델 생성
        x = [] # 장르 특성을 담을 리스트
        for i in self.arms:
            x.append([i["BPM"], i["Danceability"], i["Classical"], i["Chill"], i["Bass"]]) # 장르 특성 추가
        x = np.array(x) # 리스트를 넘파이 배열로 변환
        self.model.fit(x) # 모델 학습
        print("모델 학습 완료")

    def select_arm(self):
        print(f"현재 탐색 비율 : {self.epsilon}") # 현재 탐색 비율 출력
        print(f"현재 사용자 상태 : {self.user_status}")

        if np.random.rand() < self.epsilon: # 탐색 비율이 랜덤값보다 크다면
            return np.random.choice(self.arms) # 랜덤으로 장르 선택
        else:
            distances, indices = self.model.kneighbors([self.user_status]) # 가장 가까운 이웃 찾기
            print(f"가까운 장르와의 거리 : {distances}") # 가까운 장르와의 거리 출력
            return self.arms[indices[0][0]] # 가장 가까운 이웃의 장르 반환

    def update(self, reward_vector:list[float], user_input:int):
        if self.epsilon == 1: # 처음 탐색 비율이 1일 때
            self.user_status = np.array([float(i) for i in reward_vector]) # 사용자 상태를 reward_vector로 초기화
        else:
            self.user_status += (np.array(reward_vector) - self.user_status) * (user_input/20) # 현재 상태와 reward_vector 간의 차이를 user_input/10 비율만큼 반영
        self.epsilon *= 0.95  # 탐색 비율 점진적으로 줄이기

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