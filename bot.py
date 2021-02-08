import discord
import os
import pandas as pd

from discord.ext import commands
from models import Character, Weapon, Base, Artifact
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

client = commands.Bot(command_prefix="!")
TWT_ACCESS_TOKEN = os.getenv('TWT_ACCESS_TOKEN', None)
TWT_ACCESS_TOKEN_SECRET = os.getenv('TWT_ACCESS_TOKEN_SECRET', None)
TWT_API_KEY = os.getenv('TWT_API_KEY', None)
TWT_API_KEY_SECRET = os.getenv('TWT_API_KEY_SECRET', None)
token = os.getenv('TOKEN', None)

engine = create_async_engine(
    "sqlite:///sample.db", echo=True,
)


def query_character(session, name):
    return session.query(Character).filter(
        Character.name.like('%{0}%'.format(name)),
    ).first()


def query_weapon(session, name):
    return session.query(Weapon).filter(
        Weapon.name.like('%{0}%'.format(name)),
    ).first()


def query_artifact(session, name):
    return session.query(Artifact).filter(
        Artifact.name.like('%{0}%'.format(name)),
    ).first()


@client.event
async def on_ready():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.do_not_disturb)


@client.command(pass_context=True)
async def say_hi(ctx, *data):
    await ctx.channel.send('Hi!')


@client.command(pass_context=True)
async def character(ctx, name):
    async with AsyncSession(engine) as session:
        await session.begin()
        a = await session.run_sync(query_character, name=name)
        if not a:
            await ctx.channel.send("No object found")
            return
        data = {
            "Rarity": a.rarity,
            "Element": a.element,
            "Weapon Type": a.weapon_type,
            "Lvl 90 Base Attack": a.base_atk,
        }

        # turn dictionary to a list with proper formatting
        data_list = ["**{} :** {}\n".format(key, data[key]) for key in data]

        # create embedded message
        l_msg = discord.Embed(
            description=''.join(data_list),
            colour=discord.Colour.gold()
        )
        l_msg.set_author(name=a.name, icon_url=a.icon_url)
        print(''.join(data_list))
        await ctx.channel.send(embed=l_msg)


@client.command(pass_context=True)
async def weapon(ctx, name):
    async with AsyncSession(engine) as session:
        await session.begin()
        a = await session.run_sync(query_weapon, name=name)
        if not a:
            await ctx.channel.send("No object found")
            return
        data = {
            "Rarity": a.rarity,
            "Type": a.type,
            "Substat": a.substat,
            "Lvl 90 Base Attack": a.base_atk,
            "Passive": "\n" + a.passive,
        }

        # turn dictionary to a list with proper formatting
        data_list = ["**{} :** {}\n".format(key, data[key]) for key in data]

        # create embedded message
        l_msg = discord.Embed(
            description=''.join(data_list),
            colour=discord.Colour.blue()
        )
        l_msg.set_author(name=a.name, icon_url=a.icon_url)
        await ctx.channel.send(embed=l_msg)


@client.command(pass_context=True)
async def artifact(ctx, name):
    async with AsyncSession(engine) as session:
        await session.begin()
        a = await session.run_sync(query_artifact, name=name)
        if not a:
            await ctx.channel.send("No object found")
            return
        data = {
            "Rarity": a.rarity,
            "Location": a.where,
            "2-pc effect": a.two_piece_effect,
            "4-pc effect": a.four_piece_effect,
        }

        # turn dictionary to a list with proper formatting
        data_list = ["**{} :** {}\n".format(key, data[key]) for key in data]

        # create embedded message

        l_msg = discord.Embed(
            description=''.join(data_list),
            colour=discord.Colour.red()
        )
        l_msg.set_author(name=a.name, icon_url=a.icon_url)
        await ctx.channel.send(embed=l_msg)

client.run(token)
