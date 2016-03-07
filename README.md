Two Way Communication with PostgreSQL
=====================================

This is the presentation for the Brighton PostgreSQL Meetup.

It is hosted on [github pages](http://matthewfranglen.github.io/postgresql-fdw/#/).

This uses the [Reveal.js](https://github.com/hakimel/reveal.js) HTML Presentation library with [Yeoman](http://yeoman.io) and the [Reveal Generator](https://github.com/slara/generator-reveal).

Documentation
-------------

### Synchronizing Transactions

Python example in [resources/set-transaction.py](resources/set-transaction.py)

Documentation is [here](http://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-SNAPSHOT-SYNCHRONIZATION)

### Foreign Data Wrappers

Foreign Data Wrapper Documentation is [here](http://www.postgresql.org/docs/current/static/fdwhandler.html)

Query Planning Documentation is [here](http://www.postgresql.org/docs/current/static/fdw-planning.html)

Example of estimating size based on ANALYZE stats is [here](https://github.com/laurenz/oracle_fdw/blob/master/oracle_fdw.c#L801-L803)
