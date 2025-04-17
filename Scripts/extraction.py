import re
import logging

def email_date_extract(file_path):
    email = re.compile(r"From: (\S+@\S+)")
    date= re.compile(r"^Date: (.*)$")
    extracted_data = []
    current_email, current_date = None, None
    logging.info(f"extracting data from {file_path}")
    with open(f'{file_path}','r',encoding="UTF 8") as file:
        for line in file:
            email_matching=email.search(line)
            date_matching=date.search(line)
            if email_matching:
                current_email = email_matching.group(1)
            if date_matching: 
                current_date = date_matching.group(1)
            if current_email and current_date:
                extracted_data.append((current_email, current_date))
                current_email, current_date = None, None
    return extracted_data