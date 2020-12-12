# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ""


user_table_create = ""

song_table_create = "CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, artist_id varchar, year decimal, duration decimal);"


artist_table_create = "CREATE TABLE IF NOT EXISTS artists (artist_id int,name varchar,location varchar, latitude int, longitude int);"

time_table_create = ""

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
                        
""")

song_table_insert = ("""
                        INSERT INTO songs(song_id, title, artist_id, year, duration) 
                        VALUES (%s,%s,%s,%s,%s);
""")

artist_table_insert = ("""
                        INSERT INTO artists(artist_id, name, location, latitude, longitude)
                        VALUES (%s,%s,%s,%s,%s);
""")


time_table_insert = ("""
                        
""")

# FIND SONGS

song_select = ("""
                        
                
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_table_queries = [songplay_table_insert,user_table_insert,song_table_insert,artist_table_insert,time_table_insert]