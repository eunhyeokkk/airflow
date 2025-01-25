
from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", #airflow UI에서 보여주는 DAG이름, 통상적으론 py파일명과 동일하게설정
    schedule="0 0 * * *", #분 시 일 월 요일
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo TEST",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    bash_t1 >> bash_t2
