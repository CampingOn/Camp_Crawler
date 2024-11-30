import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, "camping_on.env")
print(f"Trying to load .env from: {env_path}")


# 환경 변수 로드
load_dotenv(dotenv_path=env_path)

# 공공 데이터 API 설정
SERVICE_KEY = os.getenv("SERVICE_KEY")
print(f"API_KEY = {SERVICE_KEY}")


# DB Setting 환경변수
DB_USER = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URI = os.getenv("DB_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
DB_PORT = os.getenv("DB_PORT")

# MongoDB 설정
MONGO_URI = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_URI}:{DB_PORT}/{MONGO_DB_NAME}?authSource={MONGO_DB_NAME}"
MONGO_COLLECTION_NAME = "camp_info"

API_BASE_URL="http://apis.data.go.kr/B551011/GoCamping/basedList"

if not SERVICE_KEY:
    print("SERVICE_KEY가 로드되지 않았습니다. .env 파일과 경로를 확인하세요.")
if not MONGO_URI:
    print("MONGO_URI가 로드되지 않았습니다. .env 파일과 경로를 확인하세요.")