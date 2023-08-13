-- Which are the top 10 members by spending
SELECT
    m.membership_id,
    m.first_name,
    m.last_name,
    SUM(tr.total_items_price) AS total_spent
FROM
    Members m
JOIN
    Transactions tr ON m.membership_id = tr.membership_id
GROUP BY
    m.membership_id, m.first_name, m.last_name
ORDER BY
    total_spent DESC
LIMIT 10;


-- Which are the top 3 items that are frequently brought by members
SELECT
    i.item_name,
    SUM(ti.item_quantity) AS total_items_bought
FROM
    Items i
JOIN
    TransactionItems ti ON i.item_id = ti.item_id
GROUP BY
    i.item_id
ORDER BY
    total_items_bought DESC
LIMIT 3;
