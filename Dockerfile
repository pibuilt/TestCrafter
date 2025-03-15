# Use a lightweight Python image
FROM python:3.12.3

# Set the working directory inside the container
WORKDIR /App

# Copy the entire 'App' folder into the container
COPY App /App

# Copy requirements.txt separately
COPY Requirements.txt /Requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /Requirements.txt

# Expose Flask API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "/App/App.py"]
