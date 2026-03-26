# FastAPI + Docker + CI/CD + AWS Project

## Overview
This project demonstrates a simple Python API built with FastAPI, containerized using Docker, integrated with a CI pipeline using GitHub Actions and deployed on AWS ECS Fargate.

---

## Tech Stack
- Python
- FastAPI
- Docker
- GitHub Actions (CI/CD)
- AWS ECS Fargate
- AWS ECR

---

## Features
- REST API with multiple endpoints
- Health check endpoint (`/health`)
- Version endpoint (`/version`)
- Logging support
- Dockerized application
- Automated CI/CD pipeline:
  - Build Python code & Docker image
  - Push Docker image to AWS ECR
- Deployable to AWS ECS Fargate
- Publicly accessible API via Security Group configuration

---

## Running the App Locally

### 1. Install dependencies
```sh
pip install -r requirements.txt
```

### 2. Run locally
```sh
uvicorn app.main:app --reload
```

### 3. Access endpoints
- http://localhost:8000/
- http://localhost:8000/health
- http://localhost:8000/version

---

## Running with Docker

### Build image
```sh
docker build -t fastapi-app .
```

### Run container
```sh
docker run -p 8000:8000 fastapi-app
```

---

## CI Pipeline

A CI pipeline is configured using GitHub Actions.
It automatically runs on every push to `main` branch and performs:

- Dependency installation
- Basic checks
- Docker image build
- Login to AWS ECR
- Tag Docker image for ECR
- Push Docker image to ECR
---

## Project Structure

```
.
├── app/
│   └── main.py
├── Dockerfile
├── requirements.txt
└── .github/workflows/ci.yml
```

---

## Why this project?

This project showcases:
- Backend API development
- Containerization best practices
- CI/CD fundamentals
