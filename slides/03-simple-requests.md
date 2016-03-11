##  Simple Requests

Its easy to pull data from the database

    import records

    db = records.Database('postgres://...')
    rows = db.query('select * from active_users')

An ORM can make it practically invisible

---

##  Make it Faster

Your requests take time to execute

Postgres only uses a single CPU to run a query

Splitting the query runs the risk of the database changing

To make a request parallel you must synchronize transactions

---

##  Synchronizing Transactions

Start the transaction and export the snapshot

    BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    SELECT pg_export_snapshot();

You can then synchronize other transactions

    BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    SET TRANSACTION SNAPSHOT 'THE TRANSACTION SNAPSHOT';

With care you can split your query into parts

---

##  Postgres Progression

Neat tricks should be used sparingly

Getting the database to do it is more efficient

Many techniques and extensions exist to improve performance

---

##  Limitations

Eventually your demands become too much

Other tools may be more limited

But they can do specific tasks faster
