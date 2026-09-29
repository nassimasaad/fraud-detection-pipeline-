import pandas as pd
import sqlalchemy
from pathlib import Path

def run():
    # ✅ Docker path
    ROOT = Path("/opt/project")

    # ✅ chemins corrigés
    tx_path = ROOT / "data" / "gold" / "transactions_gold.parquet"
    cust_path = ROOT / "data" / "gold" / "customers_gold.parquet"
    tx_bi_path = ROOT / "data" / "gold" / "transactions_bi_gold.parquet"

    # ✅ lire data
    tx = pd.read_parquet(tx_path)
    cust = pd.read_parquet(cust_path)
    tx_bi = pd.read_parquet(tx_bi_path)

    print("✅ Loaded parquet:", tx.shape, cust.shape, tx_bi.shape)

    # ✅ connexion postgres corrigée
    USER = "postgres"
    PASSWORD = "NASSIMA11nadine"
    HOST = "host.docker.internal"   # ✅ IMPORTANT
    PORT = "5432"
    DB = "fraud_lakehouse"
    SCHEMA = "lakehouse"

    engine = sqlalchemy.create_engine(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )

    # ✅ chargement
    tx.to_sql("transactions_gold", engine, schema=SCHEMA,
              if_exists="replace", index=False)

    cust.to_sql("customers_gold", engine, schema=SCHEMA,
                if_exists="replace", index=False)

    tx_bi.to_sql("transactions_bi_gold", engine, schema=SCHEMA,
                 if_exists="replace", index=False)


    