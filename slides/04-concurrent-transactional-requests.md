##  Concurrent Transactional Requests

Postgres only uses a single CPU to run a query

Splitting the query runs the risk of the database changing

You can join transactions

##  Joining Transactions

http://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-SNAPSHOT-SYNCHRONIZATION


