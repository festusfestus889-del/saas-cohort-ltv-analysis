-- 1. Cohort Retention Rate
SELECT cohort_month, period_number, 
       COUNT(DISTINCT user_id) / MAX(cohort_size) as retention_rate
FROM retention_detail
GROUP BY 1,2;

-- 2. LTV by Plan
SELECT plan, AVG(LTV) as avg_ltv, COUNT(*) as users
FROM ltv_per_user
GROUP BY plan
ORDER BY avg_ltv DESC;

-- 3. Churn Prediction: Users at risk after 2 months
SELECT user_id, plan, LTV
FROM ltv_per_user
WHERE LTV < 15000;
