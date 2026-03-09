import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv,
                          ['file_name',
                           'source_path',
                           'destination_path'])

file_name = args['file_name']
source_path = args['source_path']
destination_path = args['destination_path']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

bucket = "sales-data-takeo"

input_path = f"s3://{bucket}/{source_path}{file_name}"
output_path = f"s3://{bucket}/{destination_path}"

print("Reading from:", input_path)

df = spark.read.csv(input_path, header=True, inferSchema=True)

# Example transformation
df_filtered = df.filter(df.status == "Completed")

df_filtered.write.mode("overwrite").partitionBy("city").parquet(output_path)

print("Data written to:", output_path)