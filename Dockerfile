# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install poppler-utils for PDF handling
RUN apt-get update && apt-get install -y \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the extractor script
CMD ["python", "extractor/extract_tables.py"]