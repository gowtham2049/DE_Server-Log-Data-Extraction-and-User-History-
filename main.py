from config import FILE_PATH
from Scripts.extraction import email_date_extract
from Scripts.transformation import transform_data
from Scripts.load_to_mongo import load_mongo
from Scripts.load_to_mysql import load_mysql
from Scripts.load_to_mysql import load_mysql
from Scripts.query import execute_queries
import logging
from log import set_log
import os

def main():
    set_log()
    extracted_data=email_date_extract(FILE_PATH)
    logging.info("data extraction")

    transformed_data=transform_data(extracted_data)
    logging.info("Transforming extracted data")

    load_mongo(transformed_data)
    logging.info("loading data to mongo_db")
    load_mysql()
    logging.info("loading data to mysql")

    execute_queries()
    logging.info("Query execution")
    logging.info("server log extraction completed")
    logging.info("******************************************************************")
if __name__=="__main__":
    main()

