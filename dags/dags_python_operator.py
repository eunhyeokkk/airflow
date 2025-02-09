from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id = "dags_python_operator",
    schedule="30 6 * * *",  # 분 시 일 월 요일 (6#1 -> 첫번째주 토요일)
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    def select_fruit():
        fruit = ['BANANA','ORANGE','ORANGE', 'AVOCADO']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])
    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable = select_fruit
    )