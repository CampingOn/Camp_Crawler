# 캠핑장 정보 MongoDB 저장 프로그램

## 개요
이 프로젝트는 추천 및 향상된 검색 서비스를 위해  Python을 사용해 공공 API로부터 캠핑장 정보를 가져오고, 해시태그를 크롤링하여 MongoDB에 저장하는 프로그램입니다.
![스크린샷 2024-11-30 오후 4 29 40](https://github.com/user-attachments/assets/71721a38-7025-41f7-89e1-9668c8f6b51b)

- 공공 API: https://www.data.go.kr/data/15101933/openapi.do
- 캠핑장 상세 페이지: https://gocamping.or.kr/bsite/camp/info/read.do?c_no=3186
## 설치 및 실행 방법

### 1. 환경 설정
1. Python 3.8 이상 설치
2. 가상환경(venv) 설정:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows의 경우: venv\Scripts\activate
   ```
3. 필요 라이브러리 설치:
    ```bash
    pip install -r requirements.txt
    ```
   

### 2. 환경 변수 설정
```
# camping-on.env
SERVICE_KEY=고캠핑 공공 API 접근을 위한 서비스 키(디코딩 된 키를 사용하셔야 합니다.)
DB_USERNAME=MongoDB 접속 사용자명
DB_PASSWORD=MongoDB 접속 비밀번호
DB_URI=MongoDB 접속 URI
MONGO_DB_NAME=사용할 MongoDB 데이터베이스 이름
DB_PORT=MongoDB 포트 번호
```
- 환경변수 파일은 `/config/camping-on.env`에 저장해주세요.


### 3. 실행
```bash
python main.py
```
- 각 페이지별로 공공데이터 API를 통해 데이터를 가져옵니다.
- 캠핑장의 id를 사용해서 상세 페이지를 크롤링 해 해시태그 값을 가져옵니다.
- MongoDB에 저장합니다.


### 4. 결과 확인
```sql
db.camp_site.find().pretty()
```
![스크린샷 2024-11-30 오후 4 31 21](https://github.com/user-attachments/assets/51c55148-6e36-428c-a656-b09adfab67f1)


## 주요 파일
- main.py: 프로그램 진입점.
- settings.py: 환경 변수 및 설정 관리.
- api_fetcher.py: 공공 API 데이터 가져오기.
- hashtag_scraper.py: 캠핑장 해시태그 크롤링.
- mongo_client.py: MongoDB 연동 및 데이터 저장.
- storage.py: 데이터 파일 저장 관련 유틸리티.
- logger.py: 로그 관리.


## 주의사항
- .env 파일에는 민감한 정보(API 키, DB 정보)가 포함되어 있으므로, 절대로 깃허브에 업로드하지 마세요.
