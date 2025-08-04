CREATE OR REPLACE TABLE STG_STUDENT_INFO (
    student_id           VARCHAR,
    First_name           VARCHAR,
    Last_name            VARCHAR,
    class_id             VARCHAR,
    class_num            INT,
    dob                  DATE,
    student_email        VARCHAR,
    gender               VARCHAR,
    student_age          INT,
    academic_year        VARCHAR,
    created_at           TIMESTAMP,
    term                 VARCHAR,
    term_num             INT,
    admission_date       DATE,
    trans_id             VARCHAR,
    created_by           VARCHAR,
    TARGET_CREATED_DATE  TIMESTAMP,
    SOURCE_FOLDER        VARCHAR
);


CREATE OR REPLACE TABLE STG_TEACHER_INFO (
    names                VARCHAR,
    gender               VARCHAR,
    teacher_email        VARCHAR,
    teacher_qualification VARCHAR,
    skill_tier           INT,
    Dob                  DATE,
    subject_name         VARCHAR,
    experience_in_years  INT,
    teacher_id           VARCHAR,
    first_name           VARCHAR,
    last_name            VARCHAR,
    Term_num             INT,
    academic_year        VARCHAR,
    created_by           VARCHAR,
    created_at           TIMESTAMP,
    trans_id             VARCHAR,
    row_id               INT ,
    TARGET_CREATED_DATE  TIMESTAMP,
    SOURCE_FOLDER        VARCHAR
);



CREATE OR REPLACE TABLE STG_STUDENT_TRANSACTION (
    student_name         VARCHAR,
    class_no             INT,
    term                 INT,
    academic_year        VARCHAR,
    transaction_type     VARCHAR,
    fees_amount          NUMBER,
    transaction_time     TIMESTAMP,
    mode_of_transaction  VARCHAR,
    created_by           VARCHAR,
    trans_id             VARCHAR,
    TARGET_CREATED_DATE  TIMESTAMP,
    SOURCE_FOLDER        VARCHAR
);


CREATE OR REPLACE TABLE STG_TEACHER_SALARY_TRANSACTION (
    teacher_name             VARCHAR,
    skill_tier               INT,
    month_of_salary_deposit  VARCHAR,
    term                     VARCHAR,
    academic_year            VARCHAR,
    created_time             TIMESTAMP,
    transaction_mode         VARCHAR,
    created_by               VARCHAR,
    trans_id                 VARCHAR,
    salary_amount            NUMBER,
    TARGET_CREATED_DATE  TIMESTAMP,
    SOURCE_FOLDER        VARCHAR
);




CREATE OR REPLACE TABLE STG_ENROLLMENT (
    First_name           VARCHAR,
    Last_name            VARCHAR,
    teacher_name         VARCHAR,
    subject              VARCHAR,
    class_no             INT,
    term_num             INT,
    academic_year        VARCHAR,
    created_at           TIMESTAMP,
    trans_id             VARCHAR,
    created_by           VARCHAR,
    TARGET_CREATED_DATE  TIMESTAMP,
    SOURCE_FOLDER        VARCHAR
);



CREATE OR REPLACE TABLE STG_EXAM_RESULTS (
    student_name         VARCHAR,
    teacher_name         VARCHAR,
    class_no             INT,
    subject              VARCHAR,
    grade                VARCHAR,
    mark                 INT,
    term                 INT,
    academic_year        VARCHAR,
    created_at           TIMESTAMP,
    created_by           VARCHAR,
    trans_id             VARCHAR,
    TARGET_CREATED_DATE  TIMESTAMP,
    SOURCE_FOLDER        VARCHAR
);