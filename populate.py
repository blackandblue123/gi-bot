import pandas as pd
import sqlite3

from models import Character, Weapon, Base, Artifact
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from from_xlsx import character_df, weapon_df, artifact_df


character_dict = character_df.transpose().to_dict()
weapon_dict = weapon_df.transpose().to_dict()
artifact_dict = artifact_df.transpose().to_dict()

engine = create_engine("sqlite:///sample.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

char_objs = [Character(**character_dict.get(key)) for key in character_dict]
weapon_objs = [Weapon(**weapon_dict.get(key)) for key in weapon_dict]
artifact_objs = [Artifact(**artifact_dict.get(key)) for key in artifact_dict]

session.bulk_save_objects(char_objs)
session.bulk_save_objects(weapon_objs)
session.bulk_save_objects(artifact_objs)
session.commit()

session.close()

con = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * from weapon", con)
