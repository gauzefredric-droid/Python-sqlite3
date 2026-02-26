from sqlalchemy import create_engine, text

engine = create_engine('mysql:///mydata.db', echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS test (Id INT(3), name VARCHAR(20), age INT(3))"))

conn.commit