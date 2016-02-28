Broad Theme

The talk starts by discussing how you query from a language to the database.
How you can then improve those queries to get the data in parallel. How those
improvements can be packaged up into the database and you can forget about
them, treating the database as a bucket to be filled and queried.

Then the talk covers how different data storage services are being used. How
some of them are like databases, and some of them are more like queues or maps.
Then how each of them can be used where the language mediates the
communication.

Then the idea of postgres taking on the role of data mediator. A discussion of
how SQL is already a declarative language that has proven itself capable of
managing relations between data. How about using postgres to manage these
different data sources?

An example of using an elasticsearch fdw to index a table.

Then the discussion of the concrete steps required to implement a fdw. This
should start with the multicorn library which is simpler. Each step should be
covered.

Then cover analysis of the table to determine the likely number of rows for a
query. How can this be supported?

Then move onto the C api and how bulk actions are possible through this.

At this point real world considerations should be addressed. What if you are
querying a remote system run by another company and there is a rate limit? What
happens if their service is down? Materialized views.

Slides

 * Introduction

 * Contents

 * Simple Requests
 - Simple requests from language to database

 * Concurrent Transactional Requests
 - export the transaction and join in threads

 * Joining Different Databases
 - PostgreSQL to ES / Solr / Kafka / Stripe / arbitrary APIs ...
 - Language as a mediator
 - Foreign Data Wrappers

 * Foreign Data Wrappers
 - Methods Invoked and Flow
 - Query Planning
 - Using WHERE as a filter
 - Languages supported
 - Python Example / Multicorn
 - C Example
 - Existing FDW implementations

 * Improvements
 - Materialized views
 - External Indicies
 - Import Foreign Schema
 - Analyze

Code Samples

 * Simple Requests
 - Python
 - Java

 * Concurrent Transactional Requests
 - Python
 - Java

 * Joining Different Databases
 - Python example with Elastic Search and Postgres
 - Jave example with same

 * Foreign Data Wrappers
 - Python read
 - Python write
 - C read
 - C write and bulk write

 * Improvements
 - SQL Materialized View
 - Python analyze

Techniques

 * SET TRANSACTION
 - http://www.postgresql.org/docs/current/static/sql-set-transaction.html
