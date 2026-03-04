FROM python:3.10

WORKDIR /app

# Copy the entire project
COPY . .

# Install all dependencies for both Frontend and Backend
RUN pip install fastapi uvicorn psycopg2-binary streamlit requests python-dotenv

# Make the startup script executable
RUN chmod +x start.sh

# Expose both ports to the EC2
EXPOSE 8000
EXPOSE 8501

# Launch both services
CMD ["./start.sh"]