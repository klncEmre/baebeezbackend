import psycopg2 as dbapi2
from dotenv import load_dotenv
import os
import csv
import urllib.parse
load_dotenv()


if __name__=="__main__":
    dsn="""user="""+os.getenv("DATABASE_USERNAME") +""" password="""+os.getenv("DATABASE_PASSWORD")+""" 
         host='localhost' port=5432 dbname="""+os.getenv("DATABASENAME")
    with dbapi2.connect(dsn) as connection:
        
        cursor = connection.cursor()

        statement = """   CREATE TABLE IF NOT EXISTS Users (        
                UserId TEXT PRIMARY KEY NOT NULL, 
                Name TEXT NOT NULL,
                Gender TEXT NOT NULL,
                Department TEXT NOT NULL,
                Instagram TEXT NOT NULL,
                Snapchat TEXT NOT NULL,
                Twitter TEXT NOT NULL,
                Phone TEXT NOT NULL,
                PhotoId TEXT NOT NULL,
                saveCounter TEXT NOT NULL
            )
        """
        cursor.execute(statement)
        connection.commit()
        statement = """CREATE TABLE IF NOT EXISTS ListOfDislikes(
                Id SERIAL PRIMARY KEY NOT NULL,
                UserId TEXT NOT NULL,
                DislikedUser TEXT  NOT NULL,
                CONSTRAINT fk_userid FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
                CONSTRAINT fk_dislikeduser FOREIGN KEY (DislikedUser) REFERENCES Users(UserId) ON DELETE CASCADE
            )"""
        cursor.execute(statement)
        
        statement = """CREATE TABLE IF NOT EXISTS ListOfLikes(
                Id SERIAL PRIMARY KEY NOT NULL,
                UserId TEXT NOT NULL,
                DislikedUser TEXT  NOT NULL,
                CONSTRAINT fk_userid FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
                CONSTRAINT fk_dislikeduser FOREIGN KEY (DislikedUser) REFERENCES Users(UserId) ON DELETE CASCADE
            )"""
        cursor.execute(statement)
        
        statement = """CREATE TABLE IF NOT EXISTS ListOfMatches(
                MatchId INT PRIMARY KEY NOT NULL,
                UserId TEXT  NOT NULL,
                DislikedUser TEXT  NOT NULL,
                CONSTRAINT fk_userid FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
                CONSTRAINT fk_dislikeduser FOREIGN KEY (DislikedUser) REFERENCES Users(UserId) ON DELETE CASCADE
            )"""
        cursor.execute(statement)