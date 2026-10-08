# SaaS Cohort Retention & LTV Analysis

Goal: Understand retention and Customer Lifetime Value for pricing strategy.

## What I did
- Generated 1000 SaaS users with 3 plans (Basic ₦5k, Pro ₦12k, Premium ₦25k)
- Simulated churn (20% monthly)
- Built cohort retention curves: cohort_month vs period_number
- Calculated LTV per user, by plan

## Key Findings
- Average LTV: ~₦18,000
- Pro plan has highest LTV
- Month 1 retention: 80%, Month 2: 64% (typical SaaS decay)
- Use case: Focus retention on Pro users Month 1-2

## Stack
Python, Pandas, GitHub Actions (daily refresh)
