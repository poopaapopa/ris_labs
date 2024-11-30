SELECT prod_name, quantity, (quantity * prod_price) AS revenue, DAY(sale_date) AS day, MONTH(sale_date) AS month, YEAR(sale_date) AS year
FROM supermarket.sales
JOIN supermarket.products ON sales.prod_id = products.prod_id