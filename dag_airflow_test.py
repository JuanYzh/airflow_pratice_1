# -*- coding: utf-8 -*-
# Copyright (c) 2023 by WenHuan Yang-Zhang.
# Date: 2023-03.01
# Ich und google :)
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': datetime(2024, 6, 16),
    'email': ['juanyzhang@outlook.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


dag = DAG(
    'juanyzh_tasks_test', default_args=default_args, schedule=timedelta(days=1))


t1 = BashOperator(
    task_id='print_numbers',
    bash_command='python /home/juanyzh/workspace/python_codes/airflow_task1.py',
    dag=dag)


t2 = BashOperator(
    task_id='print_time',
    bash_command='python /home/juanyzh/workspace/python_codes/airflow_task2.py',
    dag=dag)


t3 = BashOperator(
    task_id='print_hello_word',
    bash_command='python /home/juanyzh/workspace/python_codes/airflow_task3.py',
    dag=dag)


t4 = BashOperator(
    task_id='print_random_num',
    bash_command='python /home/juanyzh/workspace/python_codes/airflow_task4.py',
    dag=dag)


t5 = BashOperator(
    task_id='print_time_now',
    bash_command='python /home/juanyzh/workspace/python_codes/airflow_task5.py',
    dag=dag)


email_task = EmailOperator(
    task_id="send_email",
    to="juanyzhang@outlook.com",
    subject="test_subject",
    html_content="<h1>test-content</h1>",
    cc="juanyangzhang@whgsj.onmicrosoft.com",
    dag=dag
)


[t1, t2] >> t3
t4 >> t5
email_task.set_upstream([t3, t5])