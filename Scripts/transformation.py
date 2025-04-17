import datetime as dt
import logging 
def transform_data(data):
    transformed=[]
    logging.info("transforming data")
    for email,date in data:
        formatted_date=dt.datetime.strptime('Fri, 4 Jan 2008 18:08:57 -0500',"%a, %d %b %Y %H:%M:%S %z") \
        .strftime("%Y-%m-%d %H:%M:%S")
        transformed.append((email,formatted_date))

    return transformed