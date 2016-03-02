##  Foreign Data Wrappers

Data in Postgres comes from Tables

Queries get data from Tables

Foreign Data Wrappers are Tables that call methods

---

##  Postgres is written in C

The core Foreign Data Wrapper API is written in C

---

##  Read a Table

![Scan Flow Chart](resources/fdw-scan.png)

WHERE clauses can tell you how to filter

You can compute joins remotely

---

##  Alter a Table

---

Methods Invoked and Flow
Query Planning
Using WHERE as a filter
Languages supported
Python Example / Multicorn
C Example
Existing FDW implementations
