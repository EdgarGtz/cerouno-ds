import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.sensors import TimeDeltaSensor
from airflow.operators.python_operator import PythonOperator


def print_world():
    print('world')


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 5, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('airflow_cerouno_v03',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo "hello"')
    # sleep = BashOperator(task_id='sleep',
    #                      bash_command='sleep 5')
    sensor_dormilon = TimeDeltaSensor(task_id='sensor_dormilon',
                                delta=dt.timedelta(minutes=5))
    print_world = PythonOperator(task_id='print_world',
                                 python_callable=print_world)


print_hello >> sensor_dormilon >> print_world
