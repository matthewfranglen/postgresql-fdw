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

##  Changing Data

Foreign Data Wrappers can be the target of TRIGGERs

Keep your services up to date

Your database can invalidate your cache entries
