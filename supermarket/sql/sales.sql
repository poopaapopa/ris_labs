SELECT prod_name, quantity, (quantity * prod_price) AS revenue
FROM supermarket.sales
JOIN supermarket.products ON sales.prod_id = products.prod_id
WHERE 1 = 1
AND YEAR(sale_date) = '$year'
AND MONTH(sale_date) = '$month'
AND DAY(sale_date) = '$day';