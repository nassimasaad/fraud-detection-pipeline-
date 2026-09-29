from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

PROJECT_DIR = "/opt/project"

default_args = {
    "owner": "nassima",
    "retries": 1,
}

with DAG(
    dag_id="fraud_lakehouse_pipeline",
    start_date=datetime(2026, 5, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    # ✅ 1. run pipeline (utilise ton fichier existant)
    run_pipeline = BashOperator(
        task_id="run_pipeline",
        bash_command=f"cd {PROJECT_DIR} && python src/load_to_postgres.py",
    )

    # ✅ 2. load postgres
    load_postgres = BashOperator(
        task_id="load_postgres",
        bash_command=f"cd {PROJECT_DIR} && python src/load_to_postgres.py",
    )

    # ✅ 3. build mart
    build_mart = SQLExecuteQueryOperator(
        task_id="build_mart",
        conn_id="fraud_postgres",
        sql="sql/build_mart.sql",
    )

    # ✅ 4. build KPI views
    build_kpis = SQLExecuteQueryOperator(
        task_id="build_kpis",
        conn_id="fraud_postgres",
        sql="sql/build_kpi_views.sql",
    )

    # ✅ ordre des tâches
    run_pipeline >> load_postgres >> build_mart >> build_kpis
