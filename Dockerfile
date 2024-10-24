# Using an official Python 3.9 image as the base
FROM python:3.9-slim

# Sets the working directory inside the container
WORKDIR /app

# Copy files from the current directory into the container's /app directory.
COPY . /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Expose port 8000 for the app to run
EXPOSE 8000

# Command that starts the Uvicorn server when the container runs
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]