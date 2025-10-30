# 🚀 CI/CD Pipeline with GitHub Actions, Docker, Kubernetes & Ansible

## 📖 Overview
This project demonstrates a **complete local DevOps pipeline** using **GitHub Actions** with **self-hosted runners** on both Windows (PowerShell) and Ubuntu (WSL).  
The pipeline automates **build, test, containerization, and deployment** processes for a sample application.

---

## 🧩 Architecture Summary

| Stage | Tool | Environment | Description |
|--------|------|--------------|--------------|
| **Build & Test** | Python, Pytest | 🪟 PowerShell (Windows) | Runs automated unit tests and builds Docker image |
| **Containerization** | Docker | 🪟 PowerShell (Windows) | Builds and pushes image to Docker Hub |
| **Deployment** | Ansible, Kubernetes | 🐧 Ubuntu (WSL) | Deploys the containerized app to Kubernetes cluster |

---

## ⚙️ Tools Used
- **GitHub Actions** – CI/CD orchestration  
- **Docker** – Containerization and image management  
- **Kubernetes** – Cluster orchestration and service management  
- **Ansible** – Automated deployment tool  
- **PowerShell (Windows)** – Self-hosted runner for build/test  
- **Ubuntu (WSL)** – Self-hosted runner for deployment  
- **Python** – Application and test environment  

---

## 🏗️ Pipeline Workflow

### 1️⃣ Build & Test (PowerShell Runner)
- Installs dependencies
- Runs Python tests with `pytest`
- Builds and pushes Docker image to Docker Hub

### 2️⃣ Deploy (Ubuntu Runner)
- Runs inside **WSL Ubuntu**
- Executes `ansible-playbook` for automated deployment
- Applies Kubernetes manifests for application rollout

---

## 🧱 GitHub Actions Workflow (`.github/workflows/ci-cd.yml`)

```yaml
name: Full Local CI/CD — Windows + Ubuntu (WSL)

on:
  push:
    branches:
      - main

jobs:
  build-test-push:
    name: Build, Test, and Push (Windows)
    runs-on: [self-hosted, self-host]
    defaults:
      run:
        shell: powershell

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Verify Python and Pip
        run: python --version

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest

      - name: Run tests
        run: python -m pytest -q

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and Push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/try100:latest

  deploy:
    name: Deploy via Ansible (Ubuntu WSL)
    needs: build-test-push
    runs-on: [self-hosted, self-host]
    defaults:
      run:
        shell: bash

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Verify Tools
        run: |
          kubectl version --client
          ansible --version

      - name: Run Ansible Playbook
        run: ansible-playbook /mnt/c/Users/John\ Israel/Desktop/try100/ansible/deploy_k8s.yml


🧰 Folder Structure
try100/
│
├── app/                      # Application source code
├── ansible/
│   └── deploy_k8s.yml        # Ansible playbook for deployment
├── k8s/
│   ├── deployment.yaml       # Kubernetes deployment manifest
│   └── service.yaml          # Kubernetes service manifest
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # CI/CD pipeline
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

🌐 Pipeline Flow Diagram
   ┌─────────────┐        ┌─────────────┐        ┌───────────────┐
   │   Git Push   │ ───▶  │  GitHub     │ ───▶  │ Windows Runner │
   │   (main)     │       │  Actions CI │        │  Build + Test  │
   └─────────────┘        └─────────────┘        └───────────────┘
                                                         │
                                                         ▼
                                                ┌──────────────────┐
                                                │ Ubuntu (WSL)     │
                                                │ Ansible Deploy   │
                                                │ + Kubernetes Roll │
                                                └──────────────────┘
🔐 Secrets Configuration

In your GitHub repository → Settings → Secrets and variables → Actions, add:
| Secret Name          | Description                                |
| -------------------- | ------------------------------------------ |
| `DOCKERHUB_USERNAME` | Your Docker Hub username                   |
| `DOCKERHUB_TOKEN`    | Docker Hub access token for pushing images |


👨‍💻 Author

John Israel
DevOps | Cloud | Automation

🏁 Result

✅ Fully automated local CI/CD pipeline
✅ Seamless hybrid execution across Windows + Ubuntu
✅ Real-world DevOps setup ready for production or cloud expansion 🚀


