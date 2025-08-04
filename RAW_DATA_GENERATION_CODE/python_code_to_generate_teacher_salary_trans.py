import os
import json
import random
from datetime import datetime
import hashlib
import pandas as pd

# ===============================
# CONFIGURATION
# ===============================

# Input folder: teacher info
teacher_info_dir = r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\teacher_info\teacher_info_portal"

# Output folder: teacher salary transactions
salary_transactions_dir = r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\teacher_salary"
os.makedirs(salary_transactions_dir, exist_ok=True)

new_salary_folder = os.path.join(salary_transactions_dir, "teacher_salary_transactions")
os.makedirs(new_salary_folder, exist_ok=True)

# ===============================
# LOAD TEACHER INFO
# ===============================

teacher_info_files = os.listdir(teacher_info_dir)

teacher_df = pd.DataFrame(columns=[['names', 'gender', 'teacher_email', 'teacher_qualification',
       'skill_tier', 'Dob', 'subject_name', 'experience_in_years',
       'teacher_id', 'first_name', 'last_name', 'Term_num', 'academic_year',
       'created_by', 'created_at', 'trans_id', 'row_id']])

for file in teacher_info_files:
    with open(os.path.join(teacher_info_dir, file), "r") as f:
        json_data = json.load(f)
    temp_df = pd.DataFrame([json_data])
    teacher_df = pd.concat([teacher_df, temp_df], ignore_index=True)
print(teacher_df)

# Inspect loaded columns
print("Loaded teacher columns:", teacher_df.columns.tolist())

# ===============================
# CREATE SALARY TRANSACTIONS DATAFRAME
# ===============================

salary_transactions_df = pd.DataFrame(columns=[
    'teacher_name', 'skill_tier', 'month_of_salary_deposit',
    'term', 'academic_year', 'created_time', 'transaction_mode',
    'created_by', 'trans_id', 'salary_amount'
])

# Modes of payment
modes_of_payment = ['Bank Transfer', 'Cash', 'Cheque']

# Salary by skill tier
skill_salary_map = {
    1: 25000,
    2: 50000,
    3: 75000
}

# Current month
current_month = datetime.now().strftime('%B')

for ind, row in teacher_df.iterrows():
    temp_df = pd.DataFrame([[
        row['names'],
        row['skill_tier'],
        current_month,
        row.get('term_num', '1'),            # fallback if term_num missing
        row.get('academic_year', '2025'),    # fallback if academic_year missing
        datetime.now().isoformat(),
        random.choice(modes_of_payment),
        'salary portal'
    ]],
    columns=[
        'teacher_name', 'skill_tier', 'month_of_salary_deposit',
        'term', 'academic_year', 'created_time',
        'transaction_mode', 'created_by'
    ])
    
    # Salary amount based on skill tier
    try:
        skill_tier = int(row['skill_tier'])
    except (ValueError, TypeError):
        skill_tier = 1  # fallback

    salary_amount = skill_salary_map.get(skill_tier, 25000)
    temp_df['salary_amount'] = salary_amount

    salary_transactions_df = pd.concat([salary_transactions_df, temp_df], ignore_index=True)

# ===============================
# GENERATE TRANSACTION ID
# ===============================

def generate_tranx_id(row):
    rand_no = random.randint(1000, 9999)
    unique_str = f"{row['teacher_name']}-{row['skill_tier']}-{rand_no}-{datetime.now()}"
    trans_id = hashlib.sha256(unique_str.encode()).hexdigest()
    return trans_id

salary_transactions_df['trans_id'] = salary_transactions_df.apply(generate_tranx_id, axis=1)

# ===============================
# WRITE JSON FILES
# ===============================

for ind, row in salary_transactions_df.iterrows():
    json_data = row.to_dict()
    with open(os.path.join(new_salary_folder, f"salary_transaction_{ind}.json"), "w") as f:
        json.dump(json_data, f, indent=4)
    print(f"Salary transaction No.{ind} created Successfully!")

