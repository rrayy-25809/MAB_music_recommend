from selenium import webdriver # selenium의 webdriver를 사용하기 위한 import
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys # selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.by import By # 요소를 찾기 위한 import
import time # 시간 관련 기능을 사용하기 위한 import

chrome_options = Options() # 크롬 옵션 설정
chrome_options.add_argument("--no-sandbox")  # 샌드박스 비활성화
chrome_options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
chrome_options.add_argument("--no-sandbox")

def get_soundcloud_links(tag:str) -> str:
    driver = webdriver.Chrome(options=chrome_options) # 크롬드라이버 실행

    # 사용자로부터 요약할 웹사이트의 URL을 입력받음
    url = f"https://soundcloud.com/tags/{tag}/popular-tracks"
    print(url) # URL 출력

    driver.get(url) # 입력받은 URL로 이동
    time.sleep(5) # 페이지 로딩 대기

    Links = driver.find_elements(By.CLASS_NAME, "sound__coverArt")
    href = Links[0].get_attribute("href")

    driver.quit() # 드라이버 종료
    return href # 링크 반환
