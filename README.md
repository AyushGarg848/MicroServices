# Microservices with FastAPI

This repository demonstrates how to create a basic microservice using FastAPI, packaged with Docker for consistent deployment. The microservice includes two simple API endpoints and provides instructions for running it locally and in a Docker container.


## Project Overview

This microservice offers two endpoints:
- **Root Endpoint** (`/`) - Returns a "Hello World" message.
- **Roll Dice Endpoint** (`/roll-dice`) - Simulates rolling a 6-sided die and returns a random integer between 1 and 6.


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
├── venv/               # Virtual environment folder
├── main.py             # FastAPI application code
├── test_main.py        # Unit tests for API
├── Dockerfile          # Docker configuration for containerizing the app
├── requirements.txt    # Dependency list (if using pip freeze)
└── README.md           # Project documentation
```


## Contact

For questions or suggestions, please feel free to reach out.
