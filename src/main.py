import logging
import os
import config

from data_scrapper import get_all_articles
from content_gen import generate_summary

os.makedirs(config.OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    filename=config.LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Starting Renewable Market Intelligence Pipeline")

    all_articles = get_all_articles()

    generate_summary(all_articles)

    logging.info("Pipeline execution completed")