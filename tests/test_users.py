import psycopg2

def test_users_table_exists():
    conn = psycopg2.connect(
        dbname="cicd_db",
        user="postgres",
        password="root@123",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT to_regclass('public.users');")
    result = cursor.fetchone()
    assert result[0] == 'users'