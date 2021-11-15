"""
Steps to run file:

cd /opt/spark/bin
./spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0
--jars mysql-connector-java-8.0.11.jar /home/ubuntu/code/spark_integration.py
"""

import math
import string
import random
import time

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

KAFKA_INPUT_TOPIC_NAME_CONS = "DataVisualizationG3"
KAFKA_BOOTSTRAP_SERVERS_CONS = "localhost:9092"

db_target_properties_dict = {"user":"sparkuser", "password":"Spark@123", "driver": 'com.mysql.jdbc.Driver'}

url = "jdbc:mysql://localhost:3306/test"
dbtable = "sparkdata"

def foreach_batch_function(df, epoch_id):

    df.write.mode('append').jdbc(url=url, table=dbtable,  properties=db_target_properties_dict)

if __name__ == "__main__":
    print("PySpark Structured Streaming with Kafka Application Started …")
    spark = SparkSession \
    .builder \
    .appName("PySpark Structured Streaming with Kafka") \
    .master("local") \
    .getOrCreate()

    stream_detail_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS_CONS) \
    .option("subscribe", KAFKA_INPUT_TOPIC_NAME_CONS) \
    .option("startingOffsets", "latest") \
    .load()

    split_col = split(stream_detail_df['value'],',')
    stream_detail_df = stream_detail_df.withColumn('quantity',split_col.getItem(0))
    stream_detail_df = stream_detail_df.withColumn('location',split_col.getItem(1))
    stream_detail_df = stream_detail_df.withColumn('status',split_col.getItem(2))

    # stream_detail_df.printSchema()
    query = stream_detail_df.selectExpr(
        "CAST(quantity AS STRING)",
        "CAST(location as STRING)",
        "CAST(status as STRING)",
        "CAST(value AS STRING)"
        ).writeStream.outputMode("append").foreachBatch(foreach_batch_function).start().awaitTermination()
    print("PySpark Structured Streaming with Kafka Application Completed.")
