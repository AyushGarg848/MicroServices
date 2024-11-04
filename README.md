# Microservices with FastAPI

This repository demonstrates how to create a basic microservice using FastAPI, packaged with Docker for consistent deployment. The microservice includes a simple API endpoint and provides instructions for running it locally and in a Docker container.

## Project Overview

This microservice offers an endpoint:
- **Root Endpoint** (`/`) - Returns a "Hello World" message.

## Setup and Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Microservices
```

### 2. Create and Activate a Virtual Environment

1. **Create a Virtual Environment** (if not already created):
   ```bash
   python -m venv venv
   ```
2. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### 3. Install Dependencies

Once the virtual environment is activated, install the required dependencies:

```bash
pip install fastapi uvicorn
```


## Running the Application

### 1. Run Locally

Start the FastAPI server locally:

```bash
uvicorn main:app --reload
```

- **Access the API Documentation**:
  - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API through FastAPI's interactive documentation.

### 2. Run with Docker

1. **Build Docker Image**:
   ```bash
   docker build -t fastapi-app .
   ```
2. **Run Docker Container**:
   ```bash
   docker run -p 8000:8000 fastapi-app
   ```

- **Access the API**:
  - Open [http://localhost:8000/docs](http://localhost:8000/docs) to view the documentation from within the Docker container.

## Project Structure

```plaintext
Microservices/
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
├── Dockerfile
├── README.md
├── requirements.txt
├── test_main.py
└── .gitignore
```

## Contact

For questions or suggestions, please feel free to reach out.
