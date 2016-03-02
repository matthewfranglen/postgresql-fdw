##  Concurrent Transactional Requests

Postgres only uses a single CPU to run a query

Splitting the query runs the risk of the database changing

You can share transactions

---

##  Joining Transactions

Start the transaction

    BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    SELECT pg_export_snapshot();

And join it from another thread

    BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    SET TRANSACTION SNAPSHOT 'THE TRANSACTION ID';

Python example in [resources/set-transaction.py](resources/set-transaction.py)

Documentation [in the Postgres manual](http://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-SNAPSHOT-SYNCHRONIZATION)

---

##  Postgres Progression

Neat tricks should be used sparingly

Better to improve the tool

The equivalent work done by postgres is more efficient

 * [Parallel Aggregation](http://www.cybertec.at/en/products/agg-parallel-aggregations-postgresql/)

 * [Automatic Sharding](https://www.citusdata.com/)

 * ...

---

##  Limitations

Eventually your demands become too much

Other tools may be more limited

But they can do specific tasks faster
