# DROP TABLES

songplay_table_drop = "DROP TABLE songplays"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = "(CREATE TABLE IF NOT EXISTS songplays (songplay_id int,start_time datetime, user_id int, level varchar,\
                         song_id int, artist_id int, session_id int, location varchar, user_agent varchar);"


user_table_create = "(CREATE TABLE IF NOT EXISTS users (user_id int,first_name varchar, last_name varchar, gender varchar,\
                    level int);"

song_table_create = "(CREATE TABLE IF NOT EXISTS songs (song_id int, title varchar, artist_id int, year int, duration datetime);"


artist_table_create = "(CREATE TABLE IF NOT EXISTS artists (artist_id int,name varchar,location varchar, latitude int, longitude int);"

time_table_create = "(CREATE TABLE IF NOT EXISTS time (start_time datetime,hour int,day varchar,week varchar, month varchar, year int,\
                     weekday varchar);"

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]