
# 📬 Server Log Email Extractor & Analyzer

## 📝 Project Overview

This project processes a server log file (`mbox.txt`) to extract email addresses and timestamps, stores them in both **MongoDB** and a **relational SQL database (e.g., mysql-connector-python)**, and performs various SQL queries for analysis.

The goal is to build a clean, structured, and queryable user history dataset from raw log data.

---

## 📂 Dataset

- **File Name**: `mbox.txt`
- **Source**: Server log containing email activity
- **Format**: Raw text with embedded email and timestamp information

---

## 📌 Problem Statement

> Extract and analyze email-related activity from a server log file by storing structured information in both MongoDB and a SQL database for further historical tracking and analysis.

---

## ✅ Tasks Completed

### **Task 1: Extract Email Addresses and Dates**
- Parsed `mbox.txt` using Python
- Extracted email addresses
- Captured corresponding timestamps

### **Task 2: Data Transformation**
- Structured data into dictionary format for insertion
- Converted timestamps into standard format: `YYYY-MM-DD HH:MM:SS`

### **Task 3: Save Data to MongoDB**
- Connected to MongoDB using `pymongo`
- Inserted structured records into a collection named `user_history`

### **Task 4: Database Connection and Data Upload**
- Retrieved data from MongoDB
- Inserted into an SQL database (SQLite used)
- Created `user_history` table with:
  - `personid` (Primary Key)
  - `email`
  - `date`

### **Task 5: Run Queries on the SQL Database**
Executed various SQL queries including:

- List all unique email addresses
- Count of emails per day
- First and last email date for each address
- Domain-based email counts

---

## 🧠 SQL Queries Used

1. List all unique email addresses
2. Count emails per day
3. First email date for each user
4. Last email date for each user
5. Total number of emails by domain
6. Most active users
7. Users with more than one email
8. Total number of emails
9. Logs grouped by date
10. Most frequent timestamp

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Database**: MongoDB, mysql-connector-python
- **Libraries**:
  - `re` for regex parsing
  - `datetime` for timestamp formatting
  - `pymongo` for MongoDB interaction
  - `mysql-connector-python` for relational DB storage

---

## 📊 Output

- `MongoDB`: Raw structured data in `user_history` collection
- `mysql-connector-python`: Clean and queryable SQL table `user_history`
- Insightful SQL reports and data summaries

---

## 🧪 How to Run

```bash
# Clone the repo
git clone https://github.com/gowtham2049/DE_Server-Log-Data-Extraction-and-User-History-.git
cd server-log-email-analyzer


# Install dependencies
pip install pymongo

# Run the script
python main.py
```
```
server-log-email-analyzer/
│
├─ mbox.txt                 # Raw server log file
├── main.py                  # Main script to process and insert data
├── queries.sql              # SQL queries for analysis
└── README.md                # Project documentation
```
