# E-Commerce-Data-Lake-AWS
Serverless E-Commerce Data Lake Project using AWS Glue, S3, Athena and PySpark


 E-Commerce Data Lake using AWS Glue

 Project Overview

This project demonstrates how to build a serverless data lake on AWS using Amazon S3, AWS Glue, and Amazon Athena. The pipeline ingests raw e-commerce data, catalogs it with AWS Glue Crawlers, transforms it using a PySpark ETL job, stores the processed data in Parquet format, and performs SQL analytics with Amazon Athena.

 AWS Services Used:

- Amazon S3
- AWS Glue
- AWS Glue Crawler
- AWS Glue Data Catalog
- AWS Glue ETL (PySpark)
- Amazon Athena
- AWS IAM



Project Structure


├── README.md
├── ecommerce_glue_etl.py
├── customers.csv
├── products.csv
├── orders.csv
├── Project_Documentation.pdf
└── screenshots/
    ├── s3_bucket.png
    ├── glue_crawler.png
    ├── glue_job_success.png
    └── athena_query.png




 Features

- Serverless data lake architecture
- Automated metadata cataloging
- Data cleaning using PySpark
- CSV to Parquet conversion
- SQL analytics using Amazon Athena
- Scalable ETL pipeline



 Project Screenshots

Amazon S3

<img width="1365" height="625" alt="s3_bucket1" src="https://github.com/user-attachments/assets/04f224d7-ef47-4b4a-92fb-b4156c2cee6b" />

<img width="1354" height="600" alt="s3_bucket2" src="https://github.com/user-attachments/assets/11e4e693-7af5-4eff-ac5a-a4c92e00ec77" />



 AWS Glue Crawler

 <img width="1355" height="637" alt="glue_crawler" src="https://github.com/user-attachments/assets/f519134d-f089-4315-a31d-e1200cfe4390" />



AWS Glue ETL Job

<img width="1365" height="627" alt="glue_job" src="https://github.com/user-attachments/assets/8d0481d2-db0d-41aa-9d99-b3224fac9255" />



  Amazon Athena Query
<img width="1366" height="768" alt="athena_query" src="https://github.com/user-attachments/assets/0fb41ed4-b05e-44a4-911f-6e928527a087" />

 Author
Priyanshi Sain

