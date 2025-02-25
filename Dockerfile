# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY ip_processor.py /app/
COPY logs /app/logs/

# Install required packages
RUN pip install pymongo

# Run the script when the container starts
CMD ["python", "/app/ip_processor.py"]
