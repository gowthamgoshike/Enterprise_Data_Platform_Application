import psycopg2
import pandas as pd
import boto3

import os
from dotenv import load_dotenv


# 1. Force the absolute path to your .env file
env_path = "/Users/gowthamgoshike/projects/Enterprise_Data_Platform_Application/.env"
load_dotenv(dotenv_path=env_path)
# AWS Config
bucket = "enterprise-ml-data-platform-gowtham"
processed_key = "processed/retail_sales_processed.csv"

# Download processed file
s3 = boto3.client("s3")
s3.download_file(bucket, processed_key, "/tmp/retail_sales_processed.csv")

# Load into pandas
df = pd.read_csv("/tmp/retail_sales_processed.csv")

# Connect to RDS
conn = psycopg2.connect(
    host=os.getenv("RDS_HOST"),         # Changed to UPPERCASE
    database=os.getenv("RDS_DB"),       # Matches your .env RDS_DB
    user=os.getenv("RDS_USER"),         # Changed to UPPERCASE
    password=os.getenv("RDS_PASSWORD")  # Changed to UPPERCASE
)
cursor = conn.cursor()

# Insert rows
# Insert rows
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO retail_sales 
        (customer_id, purchase_amount, purchase_date, product_id, days_since_last_purchase)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            row['customer_id'], 
            row['purchase_amount'], 
            row['purchase_date'], 
            row['product_id'], 
            row['days_since_last_purchase']
        )
    )

conn.commit()
cursor.close()
conn.close()

print("Data loaded into RDS successfully!")