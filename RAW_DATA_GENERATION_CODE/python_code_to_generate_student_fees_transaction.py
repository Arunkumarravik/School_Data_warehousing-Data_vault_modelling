import os
import json
import random
from datetime import datetime
import hashlib
import pandas as pd

# ===============================
# CONFIGURATION
# ===============================

# Folder containing student info JSON files
student_info_dir = r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\student_info\student_info_portal"

# Output folder for fees transactions JSON files
fees_transactions_dir = r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\student_fees"
os.makedirs(fees_transactions_dir, exist_ok=True)

new_fees_folder = os.path.join(fees_transactions_dir, "student_fees_transactions")
os.makedirs(new_fees_folder, exist_ok=True)

# ===============================
# LOAD STUDENT INFO
# ===============================

student_info_files = os.listdir(student_info_dir)

student_df = pd.DataFrame()

for file in student_info_files:
    with open(os.path.join(student_info_dir, file), "r") as f:
        json_data = json.load(f)
    temp_df = pd.DataFrame([json_data])
    student_df = pd.concat([student_df, temp_df], ignore_index=True)

# Inspect keys
print("Columns loaded:", student_df.columns.tolist())

# Rename class_num to class_no
if 'class_num' in student_df.columns:
    student_df.rename(columns={'class_num': 'class_no'}, inplace=True)

student_df['student_name'] = student_df['First_name'] + " " + student_df['Last_name']

# ===============================
# CREATE FEES TRANSACTIONS DATAFRAME
# ===============================

fees_transactions_df = pd.DataFrame(columns=[
    'student_name', 'class_no', 'term', 'academic_year',
    'transaction_type', 'fees_amount', 'transaction_time',
    'mode_of_transaction', 'created_by'
])

# Possible modes of transaction
modes_of_transaction = ['Online', 'Cash', 'Card']

for ind, row in student_df.iterrows():
    temp_df = pd.DataFrame([[
        row['student_name'],
        row['class_no'],
        row['term_num'],
        row['academic_year'],
        'Tuition Fees'
    ]],
    columns=['student_name', 'class_no', 'term', 'academic_year', 'transaction_type'])
    
    # Fees amount: 50,000 for class 1, +5,000 for each higher class
    base_fees = 50000
    increment = 5000
    try:
        class_no = int(row['class_no'])
    except (ValueError, TypeError):
        class_no = 1  # fallback if class_no is missing or NaN

    fees_amount = base_fees + (class_no - 1) * increment
    temp_df['fees_amount'] = fees_amount

    temp_df['transaction_time'] = datetime.now().isoformat()

    # Random mode of transaction
    temp_df['mode_of_transaction'] = random.choice(modes_of_transaction)

    temp_df['created_by']='Fees Portal'

    fees_transactions_df = pd.concat([fees_transactions_df, temp_df], ignore_index=True)

# ===============================
# GENERATE TRANSACTION ID
# ===============================

def generate_tranx_id(row):
    rand_no = random.randint(1000, 9999)
    unique_str = f"{row['student_name']}-{row['class_no']}-{rand_no}-{datetime.now()}"
    trans_id = hashlib.sha256(unique_str.encode()).hexdigest()
    return trans_id

fees_transactions_df['trans_id'] = fees_transactions_df.apply(generate_tranx_id, axis=1)

# ===============================
# WRITE JSON FILES
# ===============================

for ind, row in fees_transactions_df.iterrows():
    json_data = row.to_dict()
    with open(os.path.join(new_fees_folder, f"fees_transaction_{ind}.json"), "w") as f:
        json.dump(json_data, f, indent=4)
    print(f"Fees transaction No.{ind} created Successfully!")

