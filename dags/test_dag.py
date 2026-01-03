"""
Simple test DAG to verify Airflow is working
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'test_dag',
    default_args=default_args,
    description='A simple test DAG',
    schedule='@daily',  # Updated for Airflow 2.9+
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:

    t1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello from Airflow!"',
    )

    t2 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t1 >> t2

