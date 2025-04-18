use db_guvi;

#Total Count
SELECT COUNT(*) AS total_logs FROM user_history;

#Number of unique users (emails)
SELECT COUNT(DISTINCT email) AS unique_users FROM user_history;

# First log entry (earliest timestamp)
SELECT *
FROM user_history
ORDER BY date ASC
LIMIT 1;

#Last log entry (latest date)
SELECT *
FROM user_history
ORDER BY date DESC
LIMIT 1;

#Log count per user
SELECT email, COUNT(*) AS total_logs
FROM user_history
GROUP BY email
ORDER BY total_logs DESC;

#Logins grouped by day
SELECT DATE(date) AS log_day, COUNT(*) AS total_logs
FROM user_history
GROUP BY DATE(date)
ORDER BY log_day;

#Users with more than one login
SELECT email, COUNT(*) AS login_count
FROM user_history
GROUP BY email
HAVING COUNT(*) > 1;

# Logs between two specific dates
SELECT *
FROM user_history
WHERE date BETWEEN '2008-01-04 00:00:00' AND '2008-01-04 23:59:59';

# Most frequent timestamp (date with the most logins)
SELECT date, COUNT(*) AS occurrence
FROM user_history
GROUP BY date
ORDER BY occurrence DESC
LIMIT 1;





