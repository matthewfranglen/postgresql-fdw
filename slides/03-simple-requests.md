##  Simple Requests

Its easy to pull data from the database

    import records

    db = records.Database('postgres://...')
    rows = db.query('select * from active_users')

An ORM can make it practically invisible

Note:

This is the normal way to do things

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

Note:

This is how pgdump works.

The query can be very difficult to split.

---

##  Postgres Progression

Neat tricks should be used sparingly

Getting the database to do it is more efficient

Many techniques and extensions exist to improve performance

Note:

Parallel Aggregation is possible

Sharding and Partitioning can affect how fast queries are

There are many approaches
