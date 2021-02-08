from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.types import PickleType

Base = declarative_base()


class Weapon(Base):
    __tablename__ = "weapon"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, unique=True)
    base_atk = Column("base_atk", Integer, default=1)
    substat = Column("substat", String)
    type = Column("type", String)
    rarity = Column("rarity", Integer, default=3)
    icon_url = Column("icon_url", String)
    passive = Column("passive", String)


class Character(Base):
    __tablename__ = "character"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, unique=True)
    element = Column("element", String)
    weapon_type = Column("weapon_type", String)
    base_atk = Column("base_atk", Integer, default=1)
    rarity = Column("rarity", Integer, default=4)
    icon_url = Column("icon_url", String)


class Artifact(Base):
    __tablename__ = "artifact"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, unique=True)
    rarity = Column("rarity", String)
    where = Column("where", String)
    two_piece_effect = Column("two_piece", String)
    four_piece_effect = Column("four_piece", String)
    icon_url = Column("icon_url", String)
