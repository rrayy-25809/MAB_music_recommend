from selenium import webdriver # selenium의 webdriver를 사용하기 위한 import
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait # 웹 페이지 로딩 대기
from selenium.webdriver.support import expected_conditions as EC # 특정 조건을 만족할 때까지 대기하기 위한 import
from selenium.webdriver.common.by import By # 요소를 찾기 위한 import
import random # 랜덤한 수를 생성하기 위한 import
import time # 시간 관련 기능을 사용하기 위한 import

chrome_options = Options() # 크롬 옵션 설정
chrome_options.add_argument("--no-sandbox")  # 샌드박스 비활성화
chrome_options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
chrome_options.add_argument("--disable-dev-shm-usage") # 메모리 사용량 최적화

def get_soundcloud_links(tag:str) -> str:
    driver = webdriver.Chrome(options=chrome_options) # 크롬드라이버 실행

    # 사용자로부터 요약할 웹사이트의 URL을 입력받음
    url = f"https://soundcloud.com/tags/{tag}/popular-tracks" # 가장 인기 있는 트랙을 가져오기 위한 URL
    print(url) # URL 출력

    driver.get(url) # 입력받은 URL로 이동
    time.sleep(5) # 페이지 로딩 대기

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sound__coverArt"))
    ) # 'sound__coverArt' 클래스가 로드될 때까지 최대 5초 대기

    Links = driver.find_elements(By.CLASS_NAME, "sound__coverArt") # 'sound__coverArt' 클래스를 가진 요소들을 찾음
    randidx = len(Links) if len(Links) < 10 else 10
    href = Links[random.randint(0,randidx)].get_attribute("href") # 랜덤 요소의 href 속성값을 가져옴

    driver.quit() # 드라이버 종료
    return href # 링크 반환
