import os
import json
import random
from datetime import datetime, timedelta
from raw_data import teacher_names
import hashlib
import pandas as pd
import numpy as np
from collections import defaultdict

academic_year = 2025  # change as needed
classes = [f"CLS{str(i).zfill(2)}" for i in range(1, 11)]
now = datetime.now()

#Taking the student information:

base_dir="D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\student_info\student_info_portal"

files=os.listdir(base_dir)

student_df=pd.DataFrame([],columns=['student_id', 'First_name', 'Last_name', 'class_id', 'class_num', 'dob',
       'student_email', 'gender', 'student_age', 'academic_year', 'created_at',
       'term', 'term_num', 'admission_date', 'trans_id', 'created_by'])


for file in files:

    with open(f"{base_dir}/{file}" , "r") as f:

        json_data=json.load(f)

        f.close()

    temp_df=pd.DataFrame([json_data])

    #print(temp_df)

    student_df=pd.concat([student_df, temp_df],ignore_index=True)


#Taking the Teacher information:

teacher_df=pd.DataFrame(columns=['names', 'gender', 'teacher_email', 'teacher_qualification',
       'skill_tier', 'Dob', 'subject_name', 'experience_in_years',
       'teacher_id', 'first_name', 'last_name', 'Term_num', 'academic_year',
       'created_by', 'created_at', 'trans_id', 'row_id'])

teacher_base_dir=r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\teacher_info\teacher_info_portal"

teacher_files=os.listdir(teacher_base_dir)

teac_class_df=pd.DataFrame(columns=['teacher_id','teacher_name','class_no','subject'])

def check_class(skill_tier):

    if skill_tier==1:

        return 1
    
    if skill_tier==2:

        return 4
    
    if skill_tier==3:

        return 8
    
def assign_class(min_class, d_dict , skill_tier, sub):
    
    while sub in d_dict[min_class]:

        if (skill_tier==1 and min_class >=4 )or (skill_tier==2 and min_class >=8) or (skill_tier==3 and min_class >10):
            
            return None

        min_class+=1

    if min_class <= 10:

        d_dict[min_class].add(sub)
        
        return min_class
    
d_dict=defaultdict(set)

for file in teacher_files:

    with open(f"{teacher_base_dir}\\{file}","r") as f:

        json_data=json.load(f)

        f.close()

    temp_df=pd.DataFrame([json_data])

    skill, sub =temp_df['skill_tier'][0] ,temp_df['subject_name'][0]

    min_class=check_class(skill)

    class_no=assign_class(min_class, d_dict , skill,sub)

    if class_no is not None:

        new_df=pd.DataFrame([[temp_df['teacher_id'][0] ,temp_df['names'][0], class_no, sub]], columns=['teacher_id','teacher_name','class_no','subject'])

        teac_class_df=pd.concat([teac_class_df ,new_df] , ignore_index=True)

    teacher_df=pd.concat([teacher_df , temp_df] , ignore_index=True)

agg_skill_tier=teacher_df.groupby(['skill_tier' ,'subject_name']).count()

agg_class_teacher=teac_class_df.groupby('class_no').count()

print(agg_class_teacher)

#enrolling the staffs for the respective class 

combine_teach_stud_df=pd.merge(student_df ,teac_class_df ,left_on='class_num',right_on='class_no',how='inner' )
    

enrollment_df= combine_teach_stud_df[['First_name','Last_name','teacher_name','subject' ,'class_no' , 'term_num','academic_year']]

#generate trans_id:

enrollment_df['created_at']=datetime.now().isoformat()

def generate_tranx_id(row):

    rand_no=random.randint(1000,9999)

    student_name,teacher_name=(row['First_name']+" "+row['Last_name']) ,  row['teacher_name']

    unique_str=f"{student_name}-{teacher_name}-{rand_no}-{datetime.now()}"

    trans_id = hashlib.sha256(unique_str.encode()).hexdigest()

    return trans_id

enrollment_df['trans_id']=enrollment_df.apply(generate_tranx_id , axis=1)

enrollment_df['created_by']='Enrollment Portal'

#print(enrollment_df)
#print(enrollment_df)
#print(teac_class_df)


#Converting Dataframe into json file

base_enroll_dir=r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\enrollment_info"

os.makedirs(base_enroll_dir , exist_ok=True)

new_folder=os.path.join(base_enroll_dir,"enrollment_info_portal")

os.makedirs(new_folder , exist_ok=True)

for ind , row in enrollment_df.iterrows():

    json_file=row.to_dict()

    with open(f"{new_folder}\\enrollment_{ind}.json","w") as f:

        json.dump(json_file , f)

        f.close()

    print(f"enrollment_{ind} is converted into json file successfully")