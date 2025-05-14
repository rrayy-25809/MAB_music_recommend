# 베이스 이미지
FROM python:3.10-slim

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    wget unzip gnupg \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libatk1.0-0 libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 \
    libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libxshmfence1 \
    libxss1 xdg-utils libglu1-mesa --no-install-recommends \
 && rm -rf /var/lib/apt/lists/*

# Chrome 설치
RUN wget -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./chrome.deb && rm chrome.deb

# Python 패키지 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 코드 복사
COPY . /app
WORKDIR /app

# Streamlit 실행
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
