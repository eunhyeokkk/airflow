from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_operator",
    schedule="10 0 * * 6#1", #분 시 일 월 요일 (6#1 -> 첫번째주 토요일)
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE", #워커 컨테이너가 쉘프로그램 위치 알수있도록
    )
    t1_kiwi = BashOperator(
        task_id="t1_kiwi",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh KIWI", #워커 컨테이너가 쉘프로그램 위치 알수있도록
    )

    t1_orange >> t1_kiwi