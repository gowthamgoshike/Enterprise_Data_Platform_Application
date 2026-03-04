import streamlit as st
import requests

API_URL = "http://<EC2-PUBLIC-IP>:8000"

st.title("Enterprise Retail Analytics Dashboard")

# Get total records
count = requests.get(f"{API_URL}/sales/count").json()
st.metric("Total Sales Records", count["total_records"])

# Get top customers
top = requests.get(f"{API_URL}/sales/top").json()

st.subheader("Top 5 Customers by Revenue")

for customer in top["top_customers"]:
    st.write(f"Customer: {customer[0]} | Total Revenue: {customer[1]}")