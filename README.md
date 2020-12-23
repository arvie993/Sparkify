# Introduction to Sparkify

Sparkify is a music starup that want to analyze song data they have gathered on their users to understand the current trends in the music industry.
They have data on the user activity and the songs as JSON data on their app. The purpose of the project is to create a relational database(Postgres DB)
and an ETL pipeline that allows the JSON data to be inserted to the appropriate tables. This will allow analysts to query this information to make 
informed decisions on behalf of the company. 

# Database schema

The database schena will be a star schema and will contain a **fact table (songplays)** and **four dimension tables (songs, artists, time, users)**

# Python scripts

There are a total of 5 python scripts that are executed for this project

## sql_queries.py

This script contains all the CREATE statements to create the database tables, INSERT statements to insert data to the tables and DROP statements as well 
which are utilized everytime one wants to rerun the ETL process.

## Create_tables.py  

This script is used to create/drop all the tables and is run each time an ETL script is run.

## test.ipynb

This script allows one to test the database by querying the first few rows of the database.

## etl.ipynb

This script reads and processes the song and log data and loads the them to the tables. The script provides the transformation/process logic to convert the
files into data in the appropriate tables. This script is used to test if the transformation logic works.

## etl.py

Performs the same functions as etl.ipynb but is the final script that runs ETL process that is persisted to the database.

# How to run the Python scripts

All python scripts can be run on the terminal. Scripts can be run by using the command **python sample.py**. The steps to run the tables are as follows:
1. Run create_tables.py to create the tables that will later recieve the JSON file data
2. Run etl.py which will contain the functions that will read/process the json files from their respective directories and insert the data into the appropriate tables.
3. Use the test.ipynb notebook to see if the data has been inserted properly


