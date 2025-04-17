import streamlit as st #UI 개발을 위한 streamlit 라이브러리
from main import Music_MAB# main.py에서 작성한 함수들을 가져오기 위한 import문

st.title('음악 추천 시스템') # 제목 설정
st.write('당신의 음악 취향을 분석하여 맞춤형 음악을 추천합니다.') # 설명 추가

st.write('아래 추천 장르에 대해 점수를 매겨주세요') # 설명 추가
st.write('점수는 1부터 10까지 입력해주세요.') # 설명 추가

# 세션 상태 초기화
if 'model' not in st.session_state:
    st.session_state.model = Music_MAB()  # 모델 생성
if 'recommended_genre' not in st.session_state:
    st.session_state.recommended_genre = None

# 버튼 클릭 이벤트 처리
if st.button('추천 장르 받기'):
    st.session_state.recommended_genre = st.session_state.model.select_arm() # 추천 장르 선택

if st.session_state.recommended_genre is not None:
    st.write(f"추천 장르 : {st.session_state.recommended_genre['Genre']}") # 추천 장르 출력
    user_input = st.slider("점수 (1~10)", 1, 10) # 사용자 점수 가져오기
    if st.button('점수 제출'):
        st.session_state.model.update(list(st.session_state.recommended_genre.values())[1:], user_input)
        st.write("점수가 제출되었습니다.") # 점수 제출 완료 메시지 출력