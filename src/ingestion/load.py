import duckdb

def load_rows(rows, db_path=":memory:"):
    con = duckdb.connect(db_path)
    con.execute("create table if not exists events(id integer, name varchar)")
    con.executemany("insert into events values (?,?)", rows)
    return con.execute("select count(*) from events").fetchone()[0]
