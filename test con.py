import psycopg2

conn = psycopg2.connect(
    dbname="exam",
    user="postgres",
    password="eldorjon0704",
    host="localhost",
    port="5432"
)
print("✅ Connection successful")
