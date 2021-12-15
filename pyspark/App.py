from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

from Treatment import *
from AppConfig import *


def main():
    
    SparkConf().setAppName(app_name).setMaster(master)
    
    spark = SparkSession \
        .builder \
        .appName(app_name) \
        .getOrCreate()

    treatment_sql(spark)

    spark.stop()
    

    
if __name__ == "__main__":

    main()