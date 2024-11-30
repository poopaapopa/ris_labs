SELECT category_name, revenue, quantity, year, month
FROM supermarket.report
JOIN supermarket.categories ON report.category_id = categories.category_id
WHERE 1 = 1
AND year = '$year'
AND month = '$month';