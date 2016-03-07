##  Concurrent Transactional Requests

Postgres only uses a single CPU to run a query

Splitting the query runs the risk of the database changing

You can synchronize transactions

---

##  Synchronizing Transactions

Start the transaction and export the snapshot

    BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    SELECT pg_export_snapshot();

You can then synchronize other transactions

    BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    SET TRANSACTION SNAPSHOT 'THE TRANSACTION SNAPSHOT';

---

##  Postgres Progression

Neat tricks should be used sparingly

Better to improve the tool

Getting the database to do it is more efficient

Many extensions exist to improve performance

---

##  Limitations

Eventually your demands become too much

Other tools may be more limited

But they can do specific tasks faster
