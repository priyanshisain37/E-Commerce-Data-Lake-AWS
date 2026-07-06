import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, abs

# Initialize Spark and Glue Contexts
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# ==========================================
# 1. PROCESS CUSTOMERS
# ==========================================
dyf_customers = glueContext.create_dynamic_frame.from_catalog(
    database="ecommerce-raw-db2",
    table_name="customers"
)
df_customers = dyf_customers.toDF()
df_customers_clean = df_customers.fillna({"email": "unknown_email@example.com"})
df_customers_clean.write.mode("overwrite").parquet("s3://priyanshi-ecommerce-processed-data/customers/")

# ==========================================
# 2. PROCESS PRODUCTS
# ==========================================
dyf_products = glueContext.create_dynamic_frame.from_catalog(
    database="ecommerce-raw-db2",
    table_name="products"
)
df_products = dyf_products.toDF()
df_products_clean = df_products.withColumn("price", abs(col("price").cast("float"))) \
                               .fillna({"category": "Uncategorized"})
df_products_clean.write.mode("overwrite").parquet("s3://priyanshi-ecommerce-processed-data/products/")

# ==========================================
# 3. PROCESS ORDERS
# ==========================================
dyf_orders = glueContext.create_dynamic_frame.from_catalog(
    database="ecommerce-raw-db2",
    table_name="orders"
)
df_orders = dyf_orders.toDF()
# Defensive implementation: Safe-cast to string before evaluating nulls or empty spacing
df_orders_clean = df_orders.filter(
    col("quantity").cast("string").isNotNull() & 
    (col("quantity").cast("string") != "")
)
df_orders_clean.write.mode("overwrite").parquet("s3://priyanshi-ecommerce-processed-data/orders/")

job.commit()