# 🚀 Enterprise Data Platform on AWS

A production-style **Enterprise Data Platform** built using modern **Data Engineering, Cloud, and Backend technologies** on AWS Free Tier.

This project demonstrates how to build an **end-to-end scalable data platform** including:

• Data Lake  
• Distributed ETL Processing  
• Data Warehouse  
• REST API Layer  
• Analytics Dashboard  
• Containerized Deployment  

---

# 🏗 Architecture

The platform follows a modern **data lake architecture pipeline**.

Raw Data

  ↓

AWS S3 (Data Lake)

  ↓

Apache Spark ETL

  ↓

Processed Data

  ↓

PostgreSQL (AWS RDS)

  ↓

FastAPI REST API

  ↓

Streamlit Analytics Dashboard


---

# ☁️ Cloud Infrastructure

AWS services used:

• EC2 — compute instance  
• S3 — data lake storage  
• RDS PostgreSQL — relational data warehouse  

---

# 🛠 Tech Stack

### Data Engineering
- Apache Spark
- Python
- Pandas

### Backend
- FastAPI
- PostgreSQL

### Visualization
- Streamlit

### DevOps
- Docker
- Git
- GitHub

---

# 📂 Project Structure

enterprise-data-platform_application/

backend/
main.py

frontend/
app.py

spark_jobs/
etl.py

loaders/
load_to_rds.py

data/
raw_sales.csv

docs/
architecture.md

requirements.txt

Dockerfile

.env

README.md

 
---

# ⚙️ Environment Variables

Create `.env` file in the project root.

DB_HOST=your-rds-endpoint

DB_NAME=enterprise_db

DB_USER=postgres

DB_PASSWORD=yourpassword

DB_PORT=5432

API_HOST=0.0.0.0

API_PORT=8000


---

# 📦 Install Dependencies

pip install -r requirements.txt


requirements.txt


pandas

numpy

pyspark

fastapi

uvicorn

psycopg2-binary

sqlalchemy

streamlit

requests

python-dotenv

boto3

plotly

matplotlib


---

# 🚀 Run FastAPI

uvicorn api.main:app --host 0.0.0.0 --port 8000


Swagger API documentation:

http://localhost:8000/docs


---

# 📊 Run Streamlit Dashboard

streamlit run dashboard/app.py


Dashboard URL:

http://localhost:8501


---

# 🐳 Docker Deployment

Build Docker image

docker build -t enterprise-data-platform .


Run container

docker run -p 8000:8000 enterprise-data-platform


---

# 📅 Development Timeline

Day 1 — Project setup and GitHub repository  

Day 2 — Enterprise architecture design  

Day 3 — AWS infrastructure setup (EC2 + RDS)  

Day 4 — Data lake creation using S3  

Day 5 — Spark ETL pipeline development  

Day 6 — FastAPI backend service  

Day 7 — Streamlit dashboard and Docker containerization  

---

# 📈 Skills Demonstrated

• Data Engineering  
• Cloud Infrastructure  
• Distributed Data Processing  
• REST API Development  
• Data Visualization  
• DevOps and Containerization  

---

# 🔮 Future Improvements

• Terraform infrastructure automation  
• CI/CD pipelines with GitHub Actions  
• Kubernetes deployment  
• ML pipeline integration  
• Feature store implementation  

---

# 👨‍💻 Author

Gowtham Goshike  

Data Scientist | Data Engineer | Cloud Enthusiast

