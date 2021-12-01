#!/usr/bin/env bash
# TODO : Change it according to your python path and which python version you want to use (or remove it if you want to use default python installed)
export PYSPARK_PYTHON=python
spark-submit \
    --class App.py \
    --master yarn \
    --deploy-mode cluster \
    --principal {{ kerb_user }} \
    --keytab {{ kerb_keytab }} \
    --py-files python_files.zip \
    App.py 