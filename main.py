from data.api_fetcher import fetch_campsite_data, refine_campsite_data
from database.storage import save_to_mongo
from scraper.hashtag_scraper import scrape_and_update_hashtags_for_refined_data
from utils.logger import logger


def main():
  logger.info("캠핑장 데이터 수집 시작")

  page_no = 1  # 시작 페이지 번호
  while True:
    logger.info(f"페이지 {page_no} 데이터 가져오는 중...")

    # API 데이터 가져오기
    raw_data = fetch_campsite_data(page_no)

    # 데이터가 없으면 종료
    if not raw_data:
      logger.info(f"페이지 {page_no}에 데이터가 없습니다. 작업 종료.")
      break

    # 데이터 정제
    refined_data = refine_campsite_data(raw_data)

    # 해시태그 크롤링 및 MongoDB 저장
    logger.info(f"페이지 {page_no} 해시태그 크롤링 및 데이터 저장 시작")
    scrape_and_update_hashtags_for_refined_data(refined_data)
    logger.info(f"페이지 {page_no} 처리 완료")

    # 다음 페이지로 이동
    page_no += 1

  logger.info("모든 데이터 수집 및 저장 작업 완료")

if __name__ == "__main__":
  main()