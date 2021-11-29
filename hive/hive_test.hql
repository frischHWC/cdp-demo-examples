# CREATE TABLE

CREATE DATABASE fake_data;

USE fake_data;

CREATE TABLE fake_full_data AS SELECT * random_datagen.full_rd WHERE recording_time > 1617764585 ;
