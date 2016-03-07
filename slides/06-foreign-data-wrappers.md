##  Foreign Data Wrappers

Data in Postgres comes from Tables

Queries get data from Tables

Foreign Data Wrappers are Tables that call methods

---

##  Postgres is written in C

The core Foreign Data Wrapper API is written in C

---

##  Query a Table

![Query Flow Chart](resources/fdw-query.png)

WHERE clauses tell you how to filter

Can constrain virtual columns to pass data

Postgres validates the WHERE clause by default

---

##  Query Planning

![Plan Flow Chart](resources/fdw-plan.png)

You can compute joins remotely

DELETE and UPDATE read the rows before altering

---

##  Scanning a Table

![Scan Flow Chart](resources/fdw-scan.png)

Can batch the requests to be made

Trade off first row speed for all row speed?

---

##  Alter a Table

![Alter Flow Chart](resources/fdw-alter.png)

---

##  Import Foreign Schema

Just return CREATE FOREIGN TABLE statements

---

##  Analyzing Foreign Tables

Sample remote tables and return statistics

Relation Size method can use the estimates

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
