# Using an official Python 3.11 image as the base
FROM python:3.11-slim

# Sets the working directory inside the container
WORKDIR /app

# Copy only the necessary files from the current directory into the container's /app directory.
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY ./app ./app

# Expose port 8000 for the app to run
EXPOSE 80

# Command that starts the Uvicorn server when the container runs
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]