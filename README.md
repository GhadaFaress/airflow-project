# Apache Airflow Data Engineering Project 🚀

A production-ready Apache Airflow setup using Docker Compose, demonstrating data engineering workflows and ETL pipeline orchestration.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [DAGs Included](#dags-included)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project showcases a scalable Apache Airflow deployment using Docker containers with CeleryExecutor, demonstrating key data engineering concepts including:

- ETL pipeline orchestration
- Task branching and conditional logic
- XCom for inter-task communication
- Distributed task execution with Celery
- PostgreSQL backend for metadata storage
- Redis as message broker

## ✨ Features

- **Docker-based Deployment**: Fully containerized setup for easy deployment and scalability
- **CeleryExecutor**: Distributed task execution across multiple workers
- **Custom DAGs**: Pre-built workflows demonstrating various Airflow capabilities
- **PostgreSQL Backend**: Robust metadata database
- **Redis Message Broker**: Efficient task queueing and distribution
- **Health Checks**: Built-in monitoring for all services
- **Custom Configuration**: Flexible configuration using environment variables

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Airflow Web UI (8080)                    │
│                      (API Server)                           │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼────────┐  ┌──────▼──────┐   ┌───────▼────────┐
│   Scheduler    │  │     DAG     │   │   Triggerer    │
│                │  │  Processor  │   │                │
└───────┬────────┘  └─────────────┘   └────────────────┘
        │
        │ (Tasks via Redis)
        │
┌───────▼────────┐     ┌──────────┐     ┌──────────────┐
│ Celery Worker  │────▶│  Redis   │────▶│  PostgreSQL  │
│                │     │ (Broker) │     │  (Metadata)  │
└────────────────┘     └──────────┘     └──────────────┘
```

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: Version 20.10 or higher
- **Docker Compose**: Version 2.0 or higher
- **Minimum System Requirements**:
  - 4GB RAM
  - 2 CPU cores
  - 10GB disk space

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/airflow_project.git
cd airflow_project
```

### 2. Set Up Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit the `.env` file to customize your configuration (optional).

### 3. Initialize Airflow

On Linux/Mac:
```bash
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

On Windows (PowerShell):
```powershell
mkdir -p dags, logs, plugins, config
```

### 4. Start Services

```bash
docker-compose up -d
```

Wait for all services to be healthy (this may take 2-3 minutes on first run).

### 5. Access Airflow Web UI

- **URL**: http://localhost:8080
- **Username**: `airflow` (or as set in `.env`)
- **Password**: `airflow` (or as set in `.env`)

## 🚀 Usage

### Running DAGs

1. Navigate to http://localhost:8080
2. Toggle the DAG switch to enable it
3. Click the "Play" button to trigger a manual run
4. Monitor task progress in the Graph or Grid view

### Managing Services

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f airflow-scheduler

# Restart services
docker-compose restart

# Stop and remove volumes (⚠️ deletes all data)
docker-compose down -v
```

## 📊 DAGs Included

### 1. **test_dag**
- **Purpose**: Simple test DAG to verify Airflow installation
- **Schedule**: Daily (`@daily`)
- **Tasks**: Print hello message and current date

### 2. **model_training_branching**
- **Purpose**: Demonstrates branching logic and XCom usage
- **Schedule**: Daily (`@daily`)
- **Features**:
  - Parallel model training tasks
  - XCom for sharing data between tasks
  - Conditional branching based on accuracy
  - BranchPythonOperator usage

### 3. **ecommerce_etl_pipeline** & **ecommerce_etl_simple**
- **Purpose**: ETL pipeline for e-commerce data processing
- **Schedule**: Daily at 2:00 AM UTC
- **Tasks**: Load, transform, and process raw data

## 📁 Project Structure

```
airflow_project/
│
├── dags/                      # Airflow DAG definitions
│   ├── myfirstdag.py         # Model training with branching
│   └── test_dag.py           # Simple test DAG
│
├── logs/                      # Airflow logs (gitignored)
├── plugins/                   # Custom Airflow plugins
├── config/                    # Airflow configuration files
│   └── airflow.cfg           # Custom Airflow settings
│
├── docker-compose.yaml        # Docker Compose configuration
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## ⚙️ Configuration

### Custom Airflow Configuration

Modify `config/airflow.cfg` to customize Airflow settings. Common configurations:

- **Parallelism**: Max number of tasks running across DAGs
- **DAG Concurrency**: Max tasks per DAG
- **Worker Concurrency**: Max tasks per worker

### Environment Variables

Key variables in `.env`:

| Variable | Description | Default |
|----------|-------------|---------|
| `AIRFLOW_UID` | User ID for Airflow containers | 50000 |
| `_AIRFLOW_WWW_USER_USERNAME` | Web UI username | airflow |
| `_AIRFLOW_WWW_USER_PASSWORD` | Web UI password | airflow |
| `_PIP_ADDITIONAL_REQUIREMENTS` | Extra Python packages | "" |

### Adding Python Dependencies

**Quick method** (for testing):
```bash
# In .env file
_PIP_ADDITIONAL_REQUIREMENTS=pandas==1.5.3 requests==2.28.1
```

**Production method** (recommended):
1. Create a `requirements.txt` file
2. Build a custom Docker image extending the official Airflow image
3. Update `docker-compose.yaml` to use your custom image

## 🐛 Troubleshooting

### Services Not Starting

```bash
# Check service status
docker-compose ps

# View logs for errors
docker-compose logs

# Ensure ports are not in use
netstat -an | grep 8080
```

### Permission Issues (Linux/Mac)

```bash
# Set correct permissions
sudo chown -R $(id -u):0 ./logs ./dags ./plugins ./config
```

### Database Connection Errors

```bash
# Restart postgres and wait for it to be healthy
docker-compose restart postgres
docker-compose ps postgres
```

### Reset Everything

```bash
# Stop and remove all containers, volumes, and networks
docker-compose down -v

# Remove all generated files
rm -rf logs/*

# Start fresh
docker-compose up -d
```

## 🔄 Common Operations

### Adding a New DAG

1. Create a Python file in the `dags/` directory
2. Define your DAG using Airflow operators
3. Save the file
4. Wait ~30 seconds for Airflow to detect it
5. Refresh the Web UI

### Viewing Logs

```bash
# Container logs
docker-compose logs -f airflow-scheduler
docker-compose logs -f airflow-worker

# Task logs: Available in Web UI → Logs button on each task
```

### Executing Airflow CLI Commands

```bash
docker-compose run airflow-worker airflow dags list
docker-compose run airflow-worker airflow tasks test <dag_id> <task_id> <execution_date>
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## 📧 Contact

Your Name - [your-email@example.com](mailto:your-email@example.com)

Project Link: [https://github.com/yourusername/airflow_project](https://github.com/yourusername/airflow_project)

## 🙏 Acknowledgments

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Docker Compose Setup Guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

---

**⭐ If you find this project useful, please give it a star!**

