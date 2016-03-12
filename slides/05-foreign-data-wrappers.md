##  Foreign Data Wrappers

Data in Postgres is in Tables

Queries get data from Tables

Foreign Data Wrappers are Tables that call Methods

Note:

This is the second way of communication, the database talking back

---

##  Postgres is written in C

The core Foreign Data Wrapper API is written in C

---

##  Query Table

![Query Flow Chart](resources/fdw-query.png)

Each step is a method call

Iterate returns one row at a time

---

##  WHERE Clauses

WHERE clauses are useful for passing information

```sql
SELECT * FROM fdw_solr WHERE t_query = 'title:psql AND rank:[50 TO *]';
```

Provide queries as conditions on virtual columns

By default Postgres checks the WHERE clause

You can drop the check on specific clauses

---

##  Query Planning

![Plan Flow Chart](resources/fdw-plan.png)

You can compute joins remotely

DELETE and UPDATE read the rows before altering

---

##  Scan Table

![Scan Flow Chart](resources/fdw-scan.png)

Iterate is called until it returns NULL

Can batch the requests to be made

Trade off first row speed for all row speed?

---

##  Alter Table

![Alter Flow Chart](resources/fdw-alter.png)

Implementing the callbacks provides the functionality

Can restrict the tables that a method can alter

Note:

The Query Plan slide shows that the plan is modified for updates and deletes

---

##  Create Table

The special command CREATE FOREIGN TABLE is used

You can use OPTIONS to configure the table

Implement IMPORT FOREIGN SCHEMA for bulk creation

Just return CREATE FOREIGN TABLE statements

---

##  Analyze Table

Sample remote tables and return statistics

Relation Size method can use the estimates

---

##  C is hard work

There are APIs written in other languages

C will always be capable of the best performance
