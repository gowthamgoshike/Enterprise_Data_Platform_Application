from pyspark.sql import SparkSession
import boto3
import glob
import os
from pyspark.sql.functions import col, datediff, current_date

# Initialize Spark
spark = SparkSession.builder.appName("ETL_Retail").getOrCreate()

# Load raw CSV from S3
s3_bucket = "enterprise-ml-data-platform-gowtham"
raw_key = "raw/retail_sales.csv"

s3 = boto3.client('s3')
s3.download_file(s3_bucket, raw_key, "/tmp/retail_sales.csv")

# Read data
df = spark.read.csv("/tmp/retail_sales.csv", header=True, inferSchema=True)

# ETL transformations
df_clean = df.dropna()  # remove missing values
df_clean = df_clean.dropDuplicates()  # remove duplicates

# Feature engineering
df_clean = df_clean.withColumn("days_since_last_purchase", datediff(current_date(), col("purchase_date")))

# Save processed CSV locally first
processed_key = "d/Users/gowthamgoshike/projects/Enterprise_Data_Platform_Application/data/processed/retail_sales_processed.csv"
# Save locally
df_clean.coalesce(1).write.csv("/tmp/processed.csv", header=True, mode="overwrite")

# Automatically find the file starting with 'part-00000'
files = glob.glob("/tmp/processed.csv/part-00000*.csv")

if files:
    actual_file_path = files[0]
    print(f"Found file: {actual_file_path}")
    
    # Upload to S3
    s3.upload_file(actual_file_path, s3_bucket, processed_key)
    print("ETL completed and uploaded to S3 successfully!")
else:
    print("Error: No CSV part file found in /tmp/processed.csv")