import os
import json
import random
from datetime import datetime, timedelta
from raw_data import teacher_names
import hashlib
import pandas as pd
import numpy as np

cademic_year = 2025  # change as needed
classes = [f"CLS{str(i).zfill(2)}" for i in range(1, 11)]
now = datetime.now()

# 🎓 500 Indian-style names

# Extend to reach 500 unique

# 🎒 Output folder
"""base_dir = "D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\teacher_info"
os.makedirs(base_dir, exist_ok=True)
portal_path = os.path.join(base_dir, "teacher_info_portal")
os.makedirs(portal_path, exist_ok=True)"""

# 🏷️ Generate data
used_names = set()

#column definition:

df_teacher=pd.DataFrame(teacher_names, columns=['names','gender'])

#future changable values

no_of_classes, term=10 ,1 

subjects=["English","Tamil","Maths","Science","socail"]

df_teacher['teacher_email']=''

df_teacher['teacher_qualification']=''

df_teacher['skill_tier']=np.nan

df_teacher['Dob']=None

df_teacher['subject_name']=''

df_teacher['experience_in_years']=np.nan

df_teacher[['teacher_id','first_name','last_name' , 'Term_num' , 'academic_year', 'created_by' , 'created_at','trans_id','row_id']]=[None,None,None, term ,"2025-2026","hr_portal",None,None,None]


#print(df_teacher)
teacher_count, academic_year=0, 2025

def determining_skill(class_num):

    if class_num < 4 :

        return 1
    
    elif 4 <= class_num < 8:

        return 2
    
    else:

        return 3
    
def calculate_dob(exp):

    max_date=academic_year-(25 +  exp)

    min_date=academic_year-(26 +  exp)

    dob_year=random.choice([max_date , min_date])

    dob = datetime(
            dob_year,
            random.randint(1, 12),
            random.randint(1, 28)
        )
    
    return dob

i=0

loop=2

while  i <  loop:

    for  class_no in range(no_of_classes+1):

        class_id = f"CLS{str(class_no).zfill(2)}"

        curr=teacher_count

        for sub in subjects:

            if teacher_count >= len(df_teacher):

                break

            teacher_id=f"TEA{teacher_count:03}"

            first_name, second_name=df_teacher['names'][curr].split()

            teacher_email=f"{first_name}.{second_name}@teac.com"

            qualification=random.choice(['B.ED','B.ED , M.ED'])

            skill_tier=determining_skill(class_no)

            exp_years=random.randint(1 , 15)

            dob=calculate_dob(exp_years)
            
            age = academic_year - dob.year

            subject_name=sub

            created_at=datetime.now().isoformat()

            rand_no=random.randint(1000,9999)

            unique_str=f"{teacher_id}-{sub}-{rand_no}-{datetime.now()}"

            trans_id = hashlib.sha256(unique_str.encode()).hexdigest()

            df_teacher.loc[teacher_count, ['teacher_id','first_name','last_name','teacher_email','teacher_qualification','skill_tier','Dob','subject_name','experience_in_years','Term_num','created_at','trans_id','row_id']]=[teacher_id, first_name, second_name , teacher_email , qualification,skill_tier,dob, sub ,exp_years,term,created_at,trans_id, teacher_count]

            teacher_count+=1

    i+=1

print(df_teacher.dtypes)

print(type(df_teacher.loc[0, 'created_at']))


#converting each record into json "
base_dir = r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\teacher_info"

os.makedirs(base_dir , exist_ok=True)

new_folder=os.path.join(base_dir,"teacher_info_portal")

os.makedirs(new_folder,  exist_ok=True)


for col in df_teacher.columns:
    df_teacher[col] = df_teacher[col].apply(lambda x: x.isoformat() if isinstance(x, (pd.Timestamp, datetime)) else x)

for ind  , row in df_teacher.iterrows():

    json_data=row.to_dict()

    with open(f"{new_folder}/teacher_{row['row_id']}.json" , "w") as f:

        json.dump(json_data,f)
print(df_teacher)
