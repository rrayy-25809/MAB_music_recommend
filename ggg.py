import json
# 데이터 전처리
data = json.load(open("genre.json", "r")) # 장르 리스트 (json 파일에서 불러옴)
print(data) # 장르 리스트 출력
ddfe = []
for i in data:
    Danceability = int(i["Danceability"][0:-1])
    Classical = int(i["Classical"][0:-1])
    Chill = int(i["Chill"][0:-1])
    Bass = int(i["Bass"][0:-1])
    ddfe.append({"Genre": i["Genre"], "BPM": i["BPM"],"Danceability": Danceability,"Classical":  Classical,"Chill":  Chill,"Bass":  Bass})
json.dump(ddfe, open("genre.json", "w"), indent=4) # json 파일로 저장
print(ddfe) # 장르 리스트 출력