# Data Warehouse Layer

## Flow
S3 (raw) → Spark ETL → S3 (processed) → RDS (PostgreSQL)

## Warehouse Table
retail_sales

## Loader
Python script using psycopg2