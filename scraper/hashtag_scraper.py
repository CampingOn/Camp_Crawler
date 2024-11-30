import requests
from bs4 import BeautifulSoup
from database.mongo_client import get_mongo_collection
import time

DETAIL_URL = "https://gocamping.or.kr/bsite/camp/info/read.do?c_no={camp_id}"


def scrape_and_update_hashtags_for_refined_data(refined_data):
  collection = get_mongo_collection()

  for camp in refined_data:
    camp_id = camp["_id"]
    url = DETAIL_URL.format(camp_id=camp_id)

    try:
      response = requests.get(url, timeout=10)

      if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        tag_list = soup.select("ul.tag_list li")
        hashtags = [tag.get_text(strip=True) for tag in tag_list]

        # 해시태그 추가하여 저장
        camp["hashtags"] = hashtags
        collection.update_one({"_id": camp_id}, {"$set": camp}, upsert=True)
        print(f"Updated hashtags for camp ID: {camp_id}")
      else:
        print(f"Failed to fetch hashtags for camp ID: {camp_id}, Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
      print(f"Error fetching hashtags for camp ID: {camp_id}, Error: {e}")

    # 요청 간의 지연 추가 (서버 부하 방지)
    time.sleep(0.2)  # 200ms 지연