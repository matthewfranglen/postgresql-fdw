##  Foreign Data Wrappers

Data in Postgres comes from Tables

Queries get data from Tables

Foreign Data Wrappers are Tables that call methods

---

##  Postgres is written in C

The core Foreign Data Wrapper API is written in C

http://www.postgresql.org/docs/current/static/fdwhandler.html

---

##  Read a Table

![Scan Flow Chart](resources/fdw-scan.png)

WHERE clauses can tell you how to filter

You can compute joins remotely

---

##  Alter a Table

![Alter Flow Chart](resources/fdw-alter.png)

---

##  Import Foreign Schema

Can get the CREATE FOREIGN TABLE statements required

---

##  Analyzing Foreign Tables

Sample remote tables and return statistics

Relation Size method can use the estimates

[Example of using estimated size](https://github.com/laurenz/oracle_fdw/blob/master/oracle_fdw.c#L801-L803)

---

##  Writing in C is hard work

There are APIs written in other languages

C will always be capable of the best performance

---

##  Python Multicorn



Methods Invoked and Flow
Query Planning
Using WHERE as a filter
Languages supported
Python Example / Multicorn
C Example
Existing FDW implementations
