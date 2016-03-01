##  Concurrent Transactional Requests

Postgres only uses a single CPU to run a query

Splitting the query runs the risk of the database changing

You can join transactions

---

##  Joining Transactions

Start the transaction

    BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    SELECT pg_export_snapshot();

And join it from another thread

    BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    SET TRANSACTION SNAPSHOT '{}';

Python example in [resources/set-transaction.py](resources/set-transaction.py)

Documentation [in the Postgres manual](http://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-SNAPSHOT-SYNCHRONIZATION)
