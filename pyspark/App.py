from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

from Treatment import *
from AppConfig import *


def main():
    
    conf = SparkConf().setAppName(app_name).setMaster(master)
    sc = SparkContext(conf=conf)
    

    spark = SparkSession \
        .builder \
        .appName(app_name) \
        .getOrCreate()

    treatment_sql(spark)
    

    
if __name__ == "__main__":

    main()