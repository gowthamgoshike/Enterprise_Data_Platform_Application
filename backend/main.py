from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DB_CONFIG = {
    "host": "<RDS-ENDPOINT>",
    "database": "enterprise_db",
    "user": "postgres",
    "password": "<YOUR_PASSWORD>"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.get("/")
def root():
    return {"message": "Enterprise Data Platform API is running"}

@app.get("/sales/count")
def sales_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM retail_sales;")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return {"total_records": count}

@app.get("/sales/top")
def top_sales():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT customer_id, SUM(purchase_amount) as total
        FROM retail_sales
        GROUP BY customer_id
        ORDER BY total DESC
        LIMIT 5;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"top_customers": rows}