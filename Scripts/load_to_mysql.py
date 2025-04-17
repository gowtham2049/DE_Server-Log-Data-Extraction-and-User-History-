import mysql.connector
from pymongo import MongoClient
from config import MYSQL_CONFIG,MONGO_URL
import logging

def load_mysql():
    logging.info("Mongo connection")
    myclient = MongoClient(MONGO_URL)
    mydb = myclient["guvi_db"]
    mycollection=mydb['user_history']
    logging.info("getting data from mongo db")

    data = list(mycollection.find({}, {"_id": 0, "email": 1, "date": 1}))


    cnx= mysql.connector.connect(**MYSQL_CONFIG)
    mycursor = cnx.cursor()
    mycursor.execute("DROP TABLE IF EXISTS user_history")
    logging.info("loading data to mysql")
    mycursor.execute("""CREATE TABLE user_history ( Personid int AUTO_INCREMENT primary key,
    email VARCHAR(255), date timestamp)""")

    insert_query="Insert into user_history (email,date) values(%s,%s) "
    mycursor.executemany(insert_query, [(d["email"], d["date"]) for d in data])

    cnx.commit()
    mycursor.close()
    cnx.close()