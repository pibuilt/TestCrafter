# Use Python 3.12.3 as the base image
FROM python:3.12.3

# Set working directory inside container
WORKDIR /app

# Copy requirements file and install dependencies
COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt

# Copy application source code
COPY . .

# Expose port for Flask API
EXPOSE 5000

# Start the Flask app
CMD ["python", "App/App.py"]
