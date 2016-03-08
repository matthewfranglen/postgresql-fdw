##  Services Are Data

Querying a remote data store

Is like querying a service

Services you use can be Tables in your Database

---

##  Authentication

Most APIs require Authentication

Credentials can be provided when creating the table

Or per query through virtual columns

---

##  Rate Limiting

Queries are unaware of rate limits

Exceeding a rate limit is easy

Querying a MATERIALIZED VIEW can solve this

Or just copying the data to another table

---

Materialized views
External Indicies
Import Foreign Schema
Analyze
