from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from AppConfig import *


def main():
    
    SparkConf().setAppName(app_name).setMaster(master)
    
    spark = SparkSession \
        .builder \
        .appName(app_name) \
        .getOrCreate()

    rdd = spark.sparkContext.parallelize(range(1, 10000), 10)
    df = spark.createDataFrame(rdd, IntegerType())

    df.count()

    spark.stop()
    

    
if __name__ == "__main__":

    main()
