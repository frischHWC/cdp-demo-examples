from AppConfig import *


def treatment_sql(spark):
    """
    SQL treatment on Spark
    :param spark:
    :return:
    """
    path = hdfs + hdfs_home_dir + "random-data.csv"
    df_init = spark.read \
        .csv(path=path, header=True)

    df_init.select("name").show()
    



