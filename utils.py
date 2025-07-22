import pandas as pd
import os

EMP_CSV = "employees.csv"
PAY_CSV = "payroll.csv"

def init_emp_csv():
    if not os.path.exists(EMP_CSV):
        df = pd.DataFrame(columns=["ID", "Name", "Department", "Joining Date", "Status"])
        df.to_csv(EMP_CSV, index=False)

def load_emp_data():
    return pd.read_csv(EMP_CSV)

def save_emp_data(df):
    df.to_csv(EMP_CSV, index=False)

def init_pay_csv():
    if not os.path.exists(PAY_CSV):
        df = pd.DataFrame(columns=["ID","Name","Hours worked","Hourly Rate","Gross Salary","Tax Deducted","Net Salary"])
        df.to_csv(PAY_CSV, index=False)

def load_pay_data():
    return pd.read_csv(PAY_CSV)

def save_pay_data(df):
    df.to_csv(PAY_CSV, index=False)
