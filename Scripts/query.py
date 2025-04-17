import mysql.connector
from config import MYSQL_CONFIG
import logging
queries = {
        "List all unique email address": "SELECT DISTINCT email FROM user_history;",
        "Count emails per day": "SELECT DATE(date) AS day, COUNT(email) FROM user_history GROUP BY day;",
        "First and last email date per email": """
         SELECT email, MIN(date) as first_email, MAX(date) as last_email
         FROM user_history GROUP BY email;
        """,
        "Count emails per domain" : """
         SELECT SUBSTRING_INDEX(email, '@', -1) AS domain, COUNT(email)
         FROM user_history GROUP BY domain; 
        """
    }

def execute_queries():
    cnx = mysql.connector.connect(**MYSQL_CONFIG)
    mycursor = cnx.cursor(buffered=True)

    for title, query in queries.items():
        print(f"\n{title}:")
        mycursor.execute(query)
        rows = mycursor.fetchall()
        
        if rows:
            for row in rows:
                print(row)
        else:
            print("No results found.")
        
        # Ensure the results are consumed before running another query
        mycursor.nextset()

    # Close the cursor and connection
    logging.info("running query")
    mycursor.close()
    cnx.close()



