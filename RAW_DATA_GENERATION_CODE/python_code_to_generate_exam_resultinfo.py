import os
import json
import random
from datetime import datetime, timedelta
from raw_data import teacher_names
import hashlib
import pandas as pd
import numpy as np
from collections import defaultdict


# defining the directory to get the enrollment information:

enrollment_base_dir=r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\enrollment_info\enrollment_info_portal"

#creating a folder to save the exam results info:

exam_results_dir=r"D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\exam_results"

os.makedirs(exam_results_dir , exist_ok=True)

new_exam_folder=os.path.join(exam_results_dir ,"exam_results_info")

os.makedirs(new_exam_folder , exist_ok=True)

# Fetching the information about the enrollment from each file

enrollment_files=os.listdir(enrollment_base_dir)

# creating a dataframe and reading that enrollment json data into the dataframe:

enrollment_df=pd.DataFrame(columns=['First_name', 'Last_name', 'teacher_name', 'subject', 'class_no',
       'term_num', 'academic_year', 'created_at', 'trans_id', 'created_by'])

#Loading the data into the dataframe

for file in enrollment_files:

    with open(f"{enrollment_base_dir}\\{file}", "r") as f:

        json_df=json.load(f)

        f.close()

    temp_df=pd.DataFrame([json_df])

    enrollment_df=pd.concat([enrollment_df , temp_df] , ignore_index=True)

#check the aggregrated list for how many students in each class:
enrollment_df['student_name']=enrollment_df['First_name'] + " " +enrollment_df['Last_name']

agg_student_count=enrollment_df.groupby('class_no')['student_name'].nunique().reset_index()

exam_results_df=pd.DataFrame(columns=['student_name' , 'teacher_name' , 'class_no' , 'subject' ,'grade' ,'mark' ,'term' , 'academic_year' ,'created_at' , 'created_by'  ])


for ind  , row  in enrollment_df.iterrows(): 

    temp_df=pd.DataFrame([[row['student_name'] , row['teacher_name'] ,row['class_no'], row['subject'] , row['term_num'] , row['academic_year'] , 'Exam_results_info'] ] , columns=['student_name' , 'teacher_name' , 'class_no' , 'subject' ,'term' , 'academic_year' , 'created_by' ])

    grade=random.choice(["O","A+","A","B+","B","RA"])

    temp_df['grade']=grade

    mark=0

    if grade == 'O':
        mark = random.randint(91, 100)
    elif grade == 'A+':
        mark = random.randint(81, 90)
    elif grade == 'A':
        mark = random.randint(71, 80)
    elif grade == 'B+':
        mark = random.randint(61, 70)
    elif grade == 'B':
        mark = random.randint(50, 60)
    elif grade == 'RA':
        mark = random.randint(0, 49)
    else:
        mark = None  # fallback, should not happen

    # Add mark to temp_df
    temp_df['mark'] = mark

    temp_df['created_at']=datetime.now().isoformat()

    #Concating the two dfs

    exam_results_df=pd.concat([exam_results_df , temp_df],ignore_index=True)


def generate_tranx_id(row):

    rand_no=random.randint(1000,9999)

    student_name,teacher_name=row['student_name'] ,  row['teacher_name']

    unique_str=f"{student_name}-{teacher_name}-{rand_no}-{datetime.now()}"

    trans_id = hashlib.sha256(unique_str.encode()).hexdigest()

    return trans_id

exam_results_df['trans_id']=exam_results_df.apply(generate_tranx_id ,axis=1)

#converting the df records into json file

for ind  , row in exam_results_df.iterrows():

    json_data=row.to_dict()

    with open(f"{new_exam_folder}\\exam_results_{ind}.json" , "w") as f:

        json.dump(json_data  , f , indent=4)

        f.close()

    print(f"No .{ind}  created Successfully !")



