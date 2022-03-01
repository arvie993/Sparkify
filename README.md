# Introduction to Sparkify

Sparkify is a music startup that wants to analyze song data they have gathered on their users from their music app.
Sparkify has data on the user activity and the songs as JSON data on their app and directories, respectively. The purpose of the project is to create a 
relational database(Postgres DB) and an ETL pipeline that allows the JSON data to be inserted into the appropriate tables; this will enable analysts 
to query this information analyze the songplays data. 

# Datasets

Song Dataset - subset of the million song dataset(JSON format) and contains metadata about the song and artist
Log Dataset - simulated activity logs created based on the song dataset.

# Database schema

The database schema will be a star schema and will contain a **fact table (songplays)** and **four dimension tables (songs, artists, time, users)**

## Fact table
songplays - data related to songplays

## Dimension tables
1. users - user data from Sparkify application(Log Dataset)
2. songs - songs data from the Song Dataset
3. artists - artists data from the Song Dataset
4. time - timestamps which are broken into smaller units from the Log Dataset


![Database schema!](https://github.com/arvie993/Sparkify/blob/main/Sparkify%20Database%20Schema.png)


# Python scripts

There are a total of 5 python scripts that are executed for this project.

## sql_queries.py

This script contains all the CREATE statements to create the database tables, INSERT statements to insert data to the tables, and DROP statements as well 
which are utilized every time one wants to rerun the ETL process.

## Create_tables.py  

This script is used to create/drop all the tables, and each time an ETL script is run.

## test.ipynb

This script allows one to test the database by querying the first few rows of the database.

## Steps taken in the ETL process:
Steps taken in the ETL process:
1. Processing the song file:
   - Open the song file and convert it into a dataframe(df) 
   - Take a subset(song_id, title, artist_id , year, and duration columns) of the dataframe and insert it into the song table
   - Take a subset(artist_id, artist_name, artist_location , artist_latitude, and artist_longitude columns) of the dataframe and insert it into 
     the artist table
     
2. Processing the log file:
   - Open the log file and convert it into a dataframe(df)
   - Filter the dataframe by the "NextSong" action(column:page)
   - Convert timestamp column into a datetime format
   - Use dt attribute to convert the timestamp column into the appropriate columns(hour, week, month etc.) and then insert columns into the time table
   - Take a subset of user data(userId, firstname, lastname, gender, level) of dataframe and insert the rows into the user table
   - Get song and artist column from the song and artist table respectively and insert the rows into the songplay table along with other necessary 
     columns for the table
     
 3. Processing data:
    - Get all json data using the glob  function and append it to an empty list 
    - Get the total number of files found and process the files


## etl.ipynb

This script reads and processes the song and log data and loads them to the tables. The script provides the transformation/process logic to convert the
files into data in the appropriate tables. This script is used to test if the transformation logic works.

## etl.py

Performs the same functions as etl.ipynb but is the final script that runs an ETL process that is persisted to the database.

# How to run the Python scripts

All python scripts can be run on the terminal. Scripts can be run by using the command **python sample.py**. The steps to run the tables are as follows:
1. Run create_tables.py to create the tables that will later receive the JSON file data
2. Run etl.py will contain the functions that will read/process the JSON files from their respective directories and insert the data into the appropriate tables.
3. Use the test.ipynb notebook to see if the data has been inserted properly

