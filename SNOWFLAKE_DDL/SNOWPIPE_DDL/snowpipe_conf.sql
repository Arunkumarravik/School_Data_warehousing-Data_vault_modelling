-- 1️⃣ STUDENT INFO
CREATE OR REPLACE PIPE STUDENT_INFO_INGEST_PIPE
AUTO_INGEST = TRUE
INTEGRATION = GCP_SNOW_NOTIFY
AS
COPY INTO STG_STUDENT_INFO
FROM (
    SELECT
        $1:student_id::STRING AS student_id,
        $1:First_name::STRING AS First_name,
        $1:Last_name::STRING AS Last_name,
        $1:class_id::STRING AS class_id,
        $1:class_num::INT AS class_num,
        $1:dob::DATE AS dob,
        $1:student_email::STRING AS student_email,
        $1:gender::STRING AS gender,
        $1:student_age::INT AS student_age,
        $1:academic_year::STRING AS academic_year,
        $1:created_at::TIMESTAMP AS created_at,
        $1:term::STRING AS term,
        $1:term_num::INT AS term_num,
        $1:admission_date::DATE AS admission_date,
        $1:trans_id::STRING AS trans_id,
        $1:created_by::STRING AS created_by,
        CURRENT_TIMESTAMP AS Target_created_date,
        METADATA$FILENAME AS source_folder
    FROM @GCS_TO_SNOWFLAKE/school_raw_data/Student_info
)
FILE_FORMAT = (TYPE = 'JSON');


-- 2️⃣ STUDENT TRANSACTION
CREATE OR REPLACE PIPE STUDENT_TRANSACTION_INGEST_PIPE
AUTO_INGEST = TRUE
INTEGRATION = GCP_SNOW_NOTIFY
AS
COPY INTO STG_STUDENT_TRANSACTION
FROM (
    SELECT
        $1:student_name::STRING AS student_name,
        $1:class_no::INT AS class_no,
        $1:term::INT AS term,
        $1:academic_year::STRING AS academic_year,
        $1:transaction_type::STRING AS transaction_type,
        $1:fees_amount::NUMBER AS fees_amount,
        $1:transaction_time::TIMESTAMP AS transaction_time,
        $1:mode_of_transaction::STRING AS mode_of_transaction,
        $1:created_by::STRING AS created_by,
        $1:trans_id::STRING AS trans_id,
        CURRENT_TIMESTAMP AS Target_created_date,
        METADATA$FILENAME AS source_folder
    FROM @GCS_TO_SNOWFLAKE/school_raw_data/Student_fees_info
)
FILE_FORMAT = (TYPE = 'JSON');


-- 3️⃣ TEACHER INFO
CREATE OR REPLACE PIPE TEACHER_INFO_INGEST_PIPE
AUTO_INGEST = TRUE
INTEGRATION = GCP_SNOW_NOTIFY
AS
COPY INTO STG_TEACHER_INFO
FROM (
    SELECT
        $1:names::STRING AS names,
        $1:gender::STRING AS gender,
        $1:teacher_email::STRING AS teacher_email,
        $1:teacher_qualification::STRING AS teacher_qualification,
        $1:skill_tier::INT AS skill_tier,
        $1:Dob::DATE AS Dob,
        $1:subject_name::STRING AS subject_name,
        $1:experience_in_years::INT AS experience_in_years,
        $1:teacher_id::STRING AS teacher_id,
        $1:first_name::STRING AS first_name,
        $1:last_name::STRING AS last_name,
        $1:Term_num::INT AS Term_num,
        $1:academic_year::STRING AS academic_year,
        $1:created_by::STRING AS created_by,
        $1:created_at::TIMESTAMP AS created_at,
        $1:trans_id::STRING AS trans_id,
        $1:row_id::INT AS row_id,
        CURRENT_TIMESTAMP AS Target_created_date,
        METADATA$FILENAME AS source_folder
    FROM @GCS_TO_SNOWFLAKE/school_raw_data/Teacher_info
)
FILE_FORMAT = (TYPE = 'JSON');


-- 4️⃣ TEACHER SALARY TRANSACTION
CREATE OR REPLACE PIPE TEACHER_SALARY_INGEST_PIPE
AUTO_INGEST = TRUE
INTEGRATION = GCP_SNOW_NOTIFY
AS
COPY INTO STG_TEACHER_SALARY_TRANSACTION
FROM (
    SELECT
        $1:teacher_name::STRING AS teacher_name,
        $1:skill_tier::INT AS skill_tier,
        $1:month_of_salary_deposit::STRING AS month_of_salary_deposit,
        $1:term::STRING AS term,
        $1:academic_year::STRING AS academic_year,
        $1:created_time::TIMESTAMP AS created_time,
        $1:transaction_mode::STRING AS transaction_mode,
        $1:created_by::STRING AS created_by,
        $1:trans_id::STRING AS trans_id,
        $1:salary_amount::NUMBER AS salary_amount,
        CURRENT_TIMESTAMP AS Target_created_date,
        METADATA$FILENAME AS source_folder
    FROM @GCS_TO_SNOWFLAKE/school_raw_data/Teacher_salary_info
)
FILE_FORMAT = (TYPE = 'JSON');


-- 5️⃣ ENROLLMENT
CREATE OR REPLACE PIPE ENROLLMENT_INGEST_PIPE
AUTO_INGEST = TRUE
INTEGRATION = GCP_SNOW_NOTIFY
AS
COPY INTO STG_ENROLLMENT
FROM (
    SELECT
        $1:First_name::STRING AS First_name,
        $1:Last_name::STRING AS Last_name,
        $1:teacher_name::STRING AS teacher_name,
        $1:subject::STRING AS subject,
        $1:class_no::INT AS class_no,
        $1:term_num::INT AS term_num,
        $1:academic_year::STRING AS academic_year,
        $1:created_at::TIMESTAMP AS created_at,
        $1:trans_id::STRING AS trans_id,
        $1:created_by::STRING AS created_by,
        CURRENT_TIMESTAMP AS Target_created_date,
        METADATA$FILENAME AS source_folder
    FROM @GCS_TO_SNOWFLAKE/school_raw_data/enrollment_info
)
FILE_FORMAT = (TYPE = 'JSON');


-- 6️⃣ EXAM RESULTS
CREATE OR REPLACE PIPE EXAM_RESULTS_INGEST_PIPE
AUTO_INGEST = TRUE
INTEGRATION = GCP_SNOW_NOTIFY
AS
COPY INTO STG_EXAM_RESULTS
FROM (
    SELECT
        $1:student_name::STRING AS student_name,
        $1:teacher_name::STRING AS teacher_name,
        $1:class_no::INT AS class_no,
        $1:subject::STRING AS subject,
        $1:grade::STRING AS grade,
        $1:mark::INT AS mark,
        $1:term::INT AS term,
        $1:academic_year::STRING AS academic_year,
        $1:created_at::TIMESTAMP AS created_at,
        $1:created_by::STRING AS created_by,
        $1:trans_id::STRING AS trans_id,
        CURRENT_TIMESTAMP AS Target_created_date,
        METADATA$FILENAME AS source_folder
    FROM @GCS_TO_SNOWFLAKE/school_raw_data/exam_results_info
)
FILE_FORMAT = (TYPE = 'JSON');
