from AppConfig import *
from pyspark.sql.types import IntegerType


def treatment_sql(spark):
    """
    SQL treatment on Spark
    :param spark:
    :return:
    """
    rdd = spark.sparkContext.parallelize(range(1, 10000), 10)
    df = spark.createDataFrame(rdd, IntegerType())

    df.count()
    



