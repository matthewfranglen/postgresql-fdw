import psycopg2

settings = "dbname='postgres' user='postgres' host='localhost'"

with psycopg2.connect(settings) as setup_conn, setup_conn.cursor() as cur:
    cur.execute('CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, key TEXT, value TEXT)')

with psycopg2.connect(settings) as master_conn, master_conn.cursor() as master_cursor:
    master_cursor.execute('BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ')
    master_cursor.execute("SELECT pg_export_snapshot()")
    snapshot_id = master_cursor.fetchone()[0]

    with psycopg2.connect(settings) as changing_conn, changing_conn.cursor() as changing_cursor:
        changing_cursor.execute("INSERT INTO test (key, value) SELECT 'new_key', 'new_value'")
        changing_cursor.execute("SELECT count(1) FROM test")
        print "After inserting a record the count is: {}".format(changing_cursor.fetchone()[0])

    with psycopg2.connect(settings) as slave_conn, slave_conn.cursor() as slave_cursor:
        slave_cursor.execute('BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ')
        slave_cursor.execute("SET TRANSACTION SNAPSHOT '{}'".format(snapshot_id))
        slave_cursor.execute("SELECT count(1) FROM test")
        print "After joining the earlier transaction the count is: {}".format(slave_cursor.fetchone()[0])

with psycopg2.connect(settings) as final_conn, final_conn.cursor() as final_cursor:
    final_cursor.execute("SELECT count(1) FROM test")
    print "The final count is: {}".format(final_cursor.fetchone()[0])
