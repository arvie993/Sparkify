# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = """

    CREATE TABLE IF NOT EXISTS songplays (
    songplay_id serial PRIMARY KEY,\ 
    start_time datetime not null,\
    user_id varchar not null,\ 
    level varchar,\
    song_id varchar,\
    artist_id varchar,\
    session_id int,\
    location varchar,\
    user_agent varchar);

"""


user_table_create = """

    CREATE TABLE IF NOT EXISTS users (
    userId varchar PRIMARY KEY,\ 
    firstName varchar,\ 
    lastName varchar,\
    gender varchar,\ 
    level varchar);

"""  

song_table_create = """

    CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY,\ 
    title varchar,\ 
    artist_id varchar,\
    year int,\
    duration float);

"""  


artist_table_create = """

    CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY,\
    artist_name varchar,\
    artist_location varchar,\
    artist_latitude float,\
    artist_longitude float);



"""


time_table_create = """

    CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY,
    hour int,\
    day int,\
    week int,\
    month int,\ 
    year int,\
    weekday int);

"""  

# INSERT RECORDS

songplay_table_insert = ("""
                        INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""
                        INSERT INTO users(userId, firstName, lastName, gender, level) 
                        VALUES (%s,%s,%s,%s,%s)
                        ON CONFLICT (userId) DO NOTHING;
                        
""")

song_table_insert = ("""
                        INSERT INTO songs(song_id, title, artist_id, year, duration) 
                        VALUES (%s,%s,%s,%s,%s);
""")

artist_table_insert = ("""
                        INSERT INTO artists(artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
                        VALUES (%s,%s,%s,%s,%s)
                        ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
                        INSERT INTO time(start_time, hour, day, week, month, year, weekday)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
                        
                Select s.song_id, a.artist_id
                from songs s join artists a 
                on s.artist_id = a.artist_id
                where s.title = %s and a.artist_name = %s and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [song_table_create, artist_table_create, time_table_create,user_table_create,songplay_table_create]
drop_table_queries = [song_table_drop, artist_table_drop,time_table_drop,user_table_drop,songplay_table_drop]
insert_table_queries = [song_table_insert,artist_table_insert,time_table_insert,user_table_insert,songplay_table_insert]