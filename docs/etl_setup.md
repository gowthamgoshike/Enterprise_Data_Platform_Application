# ETL Setup Documentation

- Spark 3.5.1 installed
- PySpark + pandas + boto3 installed
- ETL script downloads raw CSV from S3
- Cleans data, adds feature "days_since_last_purchase"
- Uploads processed CSV back to S3