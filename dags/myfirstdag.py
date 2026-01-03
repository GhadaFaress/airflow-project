from airflow import DAG
from datetime import datetime
from random import randint
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import pendulum


def training_model():
    return randint(1, 10)


def choose_best_model(ti):
    accuracies = ti.xcom_pull(task_ids=[
        'training_model_A',
        'training_model_B',
        'training_model_C'
    ])

    best_accuracy = max(accuracies)

    if best_accuracy > 8:
        return 'accurate'
    return 'inaccurate'


with DAG(
    dag_id="model_training_branching",
    start_date=pendulum.now("UTC").subtract(days=1),
    schedule="@daily",
    catchup=False
) as dag:

    training_model_A = PythonOperator(
        task_id="training_model_A",
        python_callable=training_model
    )

    training_model_B = PythonOperator(
        task_id="training_model_B",
        python_callable=training_model
    )

    training_model_C = PythonOperator(
        task_id="training_model_C",
        python_callable=training_model
    )

    choose_best = BranchPythonOperator(
        task_id="choose_best_model",
        python_callable=choose_best_model
    )

    accurate = BashOperator(
        task_id="accurate",
        bash_command='echo "accurate"'
    )

    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command='echo "inaccurate"'
    )

    # Dependencies
    [training_model_A, training_model_B, training_model_C] >> choose_best
    choose_best >> [accurate, inaccurate]
