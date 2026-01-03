# Airflow Branching DAG – Model Training Simulation

This project demonstrates a basic Apache Airflow workflow using Docker Compose.  
The DAG simulates training multiple models in parallel, compares their results using XCom, and conditionally branches based on the best accuracy.

The goal of this project is to practice **Airflow orchestration concepts**, not machine learning itself.

---

## 🚀 What This Project Covers

- Apache Airflow 2.x / 3.x setup using Docker Compose
- Parallel task execution with `PythonOperator`
- Inter-task communication using **XCom**
- Conditional branching using `BranchPythonOperator`
- DAG scheduling and manual triggering via Airflow UI
- Debugging common Airflow issues (DAG parsing, start_date, imports)

---

## 🧠 DAG Logic Overview

1. Three model training tasks run **in parallel**
2. Each task returns a random accuracy score
3. A branching task selects the best accuracy
4. The workflow continues to:
   - `accurate` if accuracy > 8
   - `inaccurate` otherwise

---


---

## 🛠 Tech Stack

- Apache Airflow
- Docker & Docker Compose
- Python
- BashOperator
- CeleryExecutor (local setup)

---

## ▶️ How to Run

1. Clone the repository
2. Start Airflow:
   ```bash
   docker compose up -d


## 🗂 DAG Structure

---

## 🛠 Tech Stack

- Apache Airflow
- Docker & Docker Compose
- Python
- BashOperator
- CeleryExecutor (local setup)

---

## ▶️ How to Run

1. Clone the repository
2. Start Airflow:
   ```bash
   docker compose up -d
   ```
3. Open Airflow UI:
    ```bash
    http://localhost:8080
    ```
4.  Login:
      ```bash
      username: airflow
      password: airflow
      ```
5.Enable or manually trigger the DAG from the UI
## 📌 Notes 
* The project focuses on **workflow orchestration**, not real ML training 
* Designed for learning and experimentation
* Easily extendable into a full ETL or ML pipeline”


