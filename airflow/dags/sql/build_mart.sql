
CREATE SCHEMA IF NOT EXISTS mart;

DROP TABLE IF EXISTS mart.transactions_mart;

CREATE TABLE mart.transactions_mart AS
SELECT *
FROM lakehouse.transactions_gold;


