SELECT  `user_id` , GROUP_CONCAT( source_json
ORDER BY source_json DESC 
SEPARATOR  ', ' ) AS  'user_skill'
FROM main_skill
WHERE  'user_skill' IS NOT NULL 
GROUP BY  `user_id` 
LIMIT 50
