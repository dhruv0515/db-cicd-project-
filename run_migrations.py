import psycopg2
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "cicd_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root@123")

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cursor = conn.cursor()

files = sorted(os.listdir("migrations"))

for file in files:
    with open(f"migrations/{file}", "r") as f:
        sql = f.read()
        cursor.execute(sql)
        print(f"Applied {file}")

conn.commit()
cursor.close()
conn.close()

print("All migrations applied successfully.")