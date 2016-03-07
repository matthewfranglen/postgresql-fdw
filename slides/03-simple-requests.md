##  Simple Requests

Pull data from the database

    import records

    db = records.Database('postgres://...')
    rows = db.query('select * from active_users')

---

##  Applications Mediate Data

The database holds the data

The application controls the data
