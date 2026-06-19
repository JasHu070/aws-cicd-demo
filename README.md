# AWS CI/CD Demo

A simple Flask application demonstrating a complete CI/CD pipeline using:

- Flask
- Docker
- GitHub Actions
- AWS ECR
- AWS EC2

## Architecture

Developer Push
↓
GitHub Actions
↓
Run Tests
↓
Build Docker Image
↓
Push to ECR
↓
Deploy to EC2

## Current Status

- [x] Flask Application
- [x] Dockerized Application
- [ ] GitHub Actions
- [ ] AWS ECR
- [ ] AWS EC2 Deployment

## Run Locally

```bash
python app.py
```

## Run With Docker

```bash
docker build -t aws-cicd-demo:v1 .
docker run -d -p 5000:5000 aws-cicd-demo:v1
```
