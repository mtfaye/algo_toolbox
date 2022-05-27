SELECT 
    cust.name as customers
FROM customers cust
LEFT JOIN orders ord ON cust.id=ord.customerId
WHERE ord.id IS NULL;
