SELECT 
    us.Week, 
    us.ai as us_ai, 
    us.chatgpt as us_chatgpt, 
    india.ai as india_ai, 
    india.chatgpt as india_chatgpt
FROM {{ source('mage_demo', 'dbt_pipeline_load_us_py') }} AS us
JOIN {{ source('mage_demo', 'dbt_pipeline_load_india_py') }} AS india 
ON us.Week = india.Week