import os
import json
import random
from datetime import datetime, timedelta
from raw_data import names
import hashlib

# 🎓 Academic Year
academic_year = 2025  # change as needed
classes = [f"CLS{str(i).zfill(2)}" for i in range(1, 11)]
now = datetime.now()

# 🎓 500 Indian-style names

# Extend to reach 500 unique

# 🎒 Output folder
base_dir = "D:\Documents\Push_DE\Data_Vault_Mock_project\Raw_data_code\student_info"
os.makedirs(base_dir, exist_ok=True)
portal_path = os.path.join(base_dir, "student_info_portal")
os.makedirs(portal_path, exist_ok=True)

# 🏷️ Generate data
used_names = set()
student_count = 0

for class_no in range(1, 11):
    class_id = f"CLS{str(class_no).zfill(2)}"
    students_in_class = random.randint(40, 60)
    for i in range(students_in_class):
        # Pick unique name

        first,last="",""
        if len(used_names)==500:
            break
        while True:
            picked_name = random.choice(names)
            if picked_name not in used_names:
                used_names.add(picked_name)
                break

        first, last = picked_name.split()

        # DOB logic
        min_year = academic_year - (class_no + 6)
        max_year = academic_year - (class_no + 5)
        dob_year = random.randint(min_year, max_year)
        dob = datetime(
            dob_year,
            random.randint(1, 12),
            random.randint(1, 28)
        )
        age = academic_year - dob.year

        student_count += 1

        rand_no=random.randint(1000,9999)

        unique_str=f"STU{student_count:04}-{class_id}-{rand_no}-{datetime.now()}"

        trans_id = hashlib.sha256(unique_str.encode()).hexdigest()

        student_info = {
            "student_id": f"STU{student_count:04}",
            "First_name": first,
            "Last_name" : last ,
            "class_id": class_id,
            "class_num": class_no,
            "dob": dob.strftime("%Y-%m-%d"),
            "student_email" : f"{first}.{last}@edu.com",
            "gender": random.choice(["Male", "Female"]),
            "student_age": age,
            "academic_year": f"{academic_year}-{academic_year+1}",
            "created_at": now.isoformat(),
            "academic_year": "2025-2026",
            "term": "Term 1",
            "term_num" :  1 ,
            "class_id": class_id,
            "admission_date": now.strftime("%Y-%m-%d"),
            "trans_id": trans_id,     
            "created_by": "admin_portal",
            "created_at": now.isoformat()
        }

        with open(f"{portal_path}/student_info_{student_count}.json", "w") as f:
            json.dump(student_info, f, indent=4)

print(f"✅ Done Kitty! Generated {student_count} students in '{portal_path}' 🎉🐾")
