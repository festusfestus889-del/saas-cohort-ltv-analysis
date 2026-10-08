import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

os.makedirs("data/raw", exist_ok=True)
np.random.seed(42)

# 1. Generate 1000 users who joined in last 12 months
users = []
for i in range(1000):
    join_date = datetime(2025, np.random.randint(1,13), np.random.randint(1,28))
    plan = np.random.choice(['Basic_5000', 'Pro_12000', 'Premium_25000'], p=[0.5, 0.3, 0.2])
    price = {'Basic_5000':5000, 'Pro_12000':12000, 'Premium_25000':25000}[plan]
    users.append([f"user_{i}", join_date, plan, price])

df_users = pd.DataFrame(users, columns=['user_id','join_date','plan','monthly_price'])
df_users.to_csv("data/raw/users.csv", index=False)

# 2. Generate monthly payments with churn (20% churn each month)
payments = []
for _, user in df_users.iterrows():
    cur_date = user['join_date']
    for month in range(0, 13):
        if cur_date + timedelta(days=30*month) > datetime(2026,10,1): break
        # Churn logic: 20% chance to stop after 1st month
        if month>0 and np.random.rand() < 0.20: break
        payments.append([user['user_id'], cur_date + timedelta(days=30*month), user['monthly_price']])

df_pay = pd.DataFrame(payments, columns=['user_id','payment_date','amount'])
df_pay.to_csv("data/raw/payments.csv", index=False)
print("Data generated: 1000 users, payments")
