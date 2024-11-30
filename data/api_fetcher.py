import requests
from config.settings import API_BASE_URL, SERVICE_KEY

def fetch_campsite_data(page_no):
    params = {
        "numOfRows": 100,
        "pageNo": page_no,
        "MobileOS": "ETC",
        "MobileApp": "campingApp",
        "serviceKey": SERVICE_KEY,
        "_type": "json"
    }
    response = requests.get(API_BASE_URL, params=params)
    if response.status_code == 200:
        print("Response Text:", response.text)  # 응답 내용 출력
        data = response.json()
        return data["response"]["body"]["items"]["item"]
    else:
        print(f"API 요청 실패: {response.status_code}")
        return []

def refine_campsite_data(raw_data):
    refined_data = []

    for camp in raw_data:
        # 캠핑지 수량을 합산
        total_sites = sum(int(camp.get(field, "0")) for field in [
            "gnrlSiteCo", "autoSiteCo", "glampSiteCo", "caravSiteCo", "indvdlCaravSiteCo"
        ])

        # 합산 결과가 0이면 건너뛰기
        if total_sites == 0:
            continue


        refined_data.append({
            "_id": camp["contentId"],
            "name": camp["facltNm"],
            "intro": camp.get("intro", ""),
            "address": {
                "city": camp["doNm"],
                "state": camp["sigunguNm"],
                "zipcode": camp["zipcode"],
                "street_addr": camp["addr1"],
                "detailed_addr": camp.get("addr2", "")
            },
            "hashtags": [],
            "animal_friendly": camp.get("animalCmgCl", ""),
            "latitude": camp["mapY"],
            "longitude": camp["mapX"],
            "image_url": camp.get("firstImageUrl", "")
        })
    return refined_data