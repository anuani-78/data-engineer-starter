WITH recent_orders AS (
    SELECT customer_id, order_date
    FROM orders
    WHERE order_date > '2024-01-01'
)
SELECT c.customer_name, r.order_date
FROM customers c
INNER JOIN recent_orders r
ON c.customer_id = r.customer_id;
