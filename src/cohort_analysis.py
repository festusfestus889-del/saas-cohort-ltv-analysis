import pandas as pd
import os
os.makedirs("data/processed", exist_ok=True)

users = pd.read_csv("data/raw/users.csv", parse_dates=['join_date'])
payments = pd.read_csv("data/raw/payments.csv", parse_dates=['payment_date'])

users['cohort_month'] = users['join_date'].dt.to_period('M')
payments['payment_month'] = payments['payment_date'].dt.to_period('M')

# Merge to get cohort for each payment
df = payments.merge(users[['user_id','cohort_month']], on='user_id')
df['period_number'] = (df['payment_month'] - df['cohort_month']).apply(lambda x: x.n)

# 1. Cohort Retention Matrix
cohort_counts = df.groupby(['cohort_month','period_number'])['user_id'].nunique().reset_index()
cohort_sizes = users.groupby('cohort_month')['user_id'].nunique().reset_index().rename(columns={'user_id':'cohort_size'})
retention = cohort_counts.merge(cohort_sizes, on='cohort_month')
retention['retention_rate'] = retention['user_id'] / retention['cohort_size']

pivot = retention.pivot_table(index='cohort_month', columns='period_number', values='retention_rate')
pivot.to_csv("data/processed/cohort_retention.csv")
print(pivot.round(2))

# 2. Churn by cohort
retention.to_csv("data/processed/retention_detail.csv", index=False)
print("Cohort analysis saved")
