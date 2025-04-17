import logging
import os

def set_log():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    with open('logs\\log.txt','a') as log_file:
        log_file.write('\n \n etl process starting  \n')

    logging.basicConfig(
        filename='logs\\log.txt',  # Log file location
        level=logging.INFO,  
        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging