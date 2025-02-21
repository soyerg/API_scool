# Use a base image with Python
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY dash_app/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Verify installed packages
RUN pip list

# Copy the rest of the application
COPY dash_app /app

# Expose the port
EXPOSE 8050

# Run the application
CMD ["python", "app.py"]
