SELECT 
    gender,
    day,
    SUM(score_points) OVER(PARTITION BY gender ORDER BY day ASC) as total
FROM scores 
