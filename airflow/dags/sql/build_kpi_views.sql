
CREATE OR REPLACE VIEW mart.v_kpi_total_transactions AS
SELECT COUNT(*) AS total_transactions
FROM mart.transactions_mart;

CREATE OR REPLACE VIEW mart.v_kpi_total_amount AS
SELECT SUM(amount) AS total_amount
FROM mart.transactions_mart;
