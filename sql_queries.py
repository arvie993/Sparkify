import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_events"
songplay_table_drop = "DROP TABLE IF EXISTS staging_events"
user_table_drop = "DROP TABLE IF EXISTS staging_events"
song_table_drop = "DROP TABLE IF EXISTS staging_events"
artist_table_drop = "DROP TABLE IF EXISTS staging_events"
time_table_drop = "DROP TABLE IF EXISTS staging_events"

# CREATE TABLES

staging_events_table_create= ("""
    CREATE TABLE IF NOT EXISTS staging_events(
    artist varchar,
    auth varchar,
    firstName varchar,
    gender varchar,
    ItemInSession varchar,
    lastName varchar,
    length float,
    level varchar,
    location varchar,
    method varchar,
    page varchar,
    registration varchar,
    sessionId varchar,
    song varchar,
    status varchar,
    ts timestamp,
    userAgent varchar,
    userId varchar
    )
""")

staging_songs_table_create = ("""
    CREATE TABLE IF NOT EXISTS staging_songs(
    num_songs int,
    artist_id varchar,
    artist_latitude varchar,
    artist_longitude varchar,
    artist_location varchar,
    artist_name varchar,
    song_id varchar,
    title varchar,
    duration float,
    year int
    )
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
    songplay_id varchar,
    start_time timestamp,
    user_id varchar,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id varchar,
    location varchar,
    user_agent varchar
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
    user_id varchar,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
    song_id varchar,
    title varchar,
    artist_id varchar,
    year int,
    duration timestamp
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar,
    name varchar,
    location varchar,
    latitude varchar,
    longitude varchar
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
    start_time timestamp,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
    )
""")

# STAGING TABLES

staging_events_copy = ("""
COPY staging_events
FROM {}
iam_role {}
FORMAT AS json {}
region 'us-east-2'
""").format(config['S3']['LOG_DATA'],config["IAM_ROLE"]["ARN"],config['S3']['LOG_JSONPATH'])

staging_songs_copy = ("""
COPY staging_songs
FROM {}
iam_role AS {}
region 'us-east-2'
""").format(config['S3']['SONG_DATA'],config["IAM_ROLE"]["ARN"])

# FINAL TABLES

songplay_table_insert = ("""
INSERT INTO songplays(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent)

SELECT DISTINCT
sd.ts as start_time,
sd.userid as user_id,
sd.level as level,
ss.song_id as song_id,
ss.artist_id as artist_id,
sd.sessionid as session_id,
sd.location as location,
sd.userAgent as user_agent
FROM staging_data sd
LEFT JOIN staging_songs ss
on (sd.song = ss.title)
WHERE sd.page = 'NextSong'

""")

user_table_insert = ("""
INSERT INTO users(user_id,first_name,last_name,gender,level)

SELECT 
sd.userid as user_id,
sd.firstName as first_name,
sd.lastName as last_name,
sd.gender as gender,
sd.level as level
FROM staging_data sd
WHERE sd.page = 'NextSong'

""")

song_table_insert = ("""
INSERT INTO songs(song_id,title,artist_id,year,duration)
SELECT
song_id as song_id,
title as title,
artist_id as artist_id,
year as year,
duration as duration
FROM staging_songs

""")

artist_table_insert = ("""
INSERT INTO artists(artist_id,name,location,lattitude,longitude)
select
artist_id as artist_id,
artist_name as artist,
artist_location as location,
artist_lattitude as lattitude,
artist_longitude as longitude,
FROM staging_songs
""")

time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday)

SELECT DISTINCT timestamp 'epoch' + ts/1000 * INTERVAL '1 second' as start_time,
EXTRACT(HOUR from start_time),
EXTRACT(DAY from start_time),
EXTRACT(WEEK from start_time),
EXTRACT(MONTH from start_time),
EXTRACT(YEAR from start_time),
EXTRACT(DOW from start_time)
FROM staging_events

""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
