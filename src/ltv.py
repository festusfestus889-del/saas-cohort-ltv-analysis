import pandas as pd
import os
os.makedirs("data/processed", exist_ok=True)

payments = pd.read_csv("data/raw/payments.csv")
users = pd.read_csv("data/raw/users.csv")

# LTV per user
ltv_per_user = payments.groupby('user_id')['amount'].sum().reset_index().rename(columns={'amount':'LTV'})
ltv_per_user = ltv_per_user.merge(users[['user_id','plan','join_date']], on='user_id')

# LTV by Plan and Cohort
ltv_by_plan = ltv_per_user.groupby('plan')['LTV'].agg(['mean','median','count']).round(2)
ltv_by_plan.to_csv("data/processed/ltv_by_plan.csv")

ltv_per_user.to_csv("data/processed/ltv_per_user.csv", index=False)

avg_ltv = ltv_per_user['LTV'].mean()
print(f"Average LTV: NGN {avg_ltv:,.0f}")
print(ltv_by_plan)
