import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request 
import time
from urllib import parse, request
from itertools import cycle
import discord
import requests
from discord import Permissions
from discord.ext import commands
from discord.utils import get
import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from aiohttp import ClientSession
import aiohttp
import os
import requests
import os
import discord
from discord.ext import commands , tasks


import sys

from discord.ext import commands, tasks

import pymongo
from discord_components import *

from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option



import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request 
import time
from urllib import parse, request
from itertools import cycle
import discord
import requests
from discord import Permissions
from discord.ext import commands
from discord.utils import get
import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from aiohttp import ClientSession
import aiohttp
import os
import requests
import os
import discord
from discord.ext import commands , tasks


import sys

from discord.ext import commands, tasks

import pymongo
from discord_components import *

from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

modules = [
    'role',
    'channel',
    'channel_del',
    'role_del',
    'ban',
    'kick',
    'bot',
    'role_update',
    'webhook_creation'
]







token = 'OTE1Mjk4NjY0NDc2NDcxMjk4.YaZkTw.bU1UjzcA8akcanPsq49D2nj-nSM'
client = discord.Client()
client = commands.Bot(command_prefix=">",  intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
client.remove_command('help')



mongoClient = pymongo.MongoClient('mongodb://COOOLLLLLLBOYYYYY:qCpIslnCXm7qT9iM@forbeast-shard-00-00.wcenb.mongodb.net:27017,forbeast-shard-00-01.wcenb.mongodb.net:27017,forbeast-shard-00-02.wcenb.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-kpgs1i-shard-0&authSource=admin&retryWrites=true&w=majority')
db = mongoClient.get_database("Protected").get_collection("servers")
db2 = mongoClient.get_database("Protected").get_collection("protection")



class ProtectionSystem:

    def NewServer(owner_id, server_id):
        db.insert_one({
            "whitelisted": [803164742142918688],
            "log": None,
            "guild_id": server_id
        })
        db2.insert_one({
            "guild_id": server_id,
            "role": 'Enabled',
            "channel": 'Enabled',
            "channel_del": 'Enabled',
            "role_del": 'Enabled',
            "ban": 'Enabled',
            "kick": 'Enabled',
            "bot": 'Enabled',
            "role_update": 'Enabled',
            "webhook_creation": 'Enabled',
        })

@commands.Cog.listener()
async def on_connect(self):
    os.system('cls')
    for server in self.client.guilds:
        if not db.find_one({ "guild_id": server.id }):
            guild_ = self.client.get_guild(server.id)
            ProtectionSystem.NewServer(guild_.owner.id, guild_.id)



@client.event
async def on_ready():
	#turns on discord components lib
    DiscordComponents(client)




buttons = [
    [
        Button(style=ButtonStyle.URL, label='SUPPORT SERVER !', url='https://discord.gg/2RDVVpcJqC'),
        Button(style=ButtonStyle.URL, label='INVITE ME !', url='https://discord.com/api/oauth2/authorize?client_id=915298664476471298&permissions=8&scope=bot%20applications.commands')
    ],
]


@client.command()
async def help(ctx):
    e = discord.Embed()
    e.add_field(name='**Protected 2.O**' , value="Whitelist - Bot Will Ignore That Person\n UnWhitelist - Remove Whitelisted Member\n Whitelisted - Shows The List Of Whitelisted User\n Botinfo - Tells Info About Bot Ban - Ban A Member \n Kick - Kick A Member")
    e.set_author(name="Project Protected")
    e.set_footer(text='Ravager Development', icon_url='https://images-ext-1.discordapp.net/external/bDDxuClUX8snm7AW2BaVX2T5ZbcTBnnNuksYk8xRMq4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777437789356032011/a_be571618bce1786ab1042378e166284d.gif?width=408&height=408')
    e.set_thumbnail(url='https://images-ext-1.discordapp.net/external/bDDxuClUX8snm7AW2BaVX2T5ZbcTBnnNuksYk8xRMq4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777437789356032011/a_be571618bce1786ab1042378e166284d.gif?width=408&height=408')
    await ctx.send(embed=e, components=buttons)



@client.command()
@commands.has_permissions(administrator=True)
async def whitelisted(ctx):
    if ctx.author.id == ctx.guild.owner.id:
        result = ''
        data = db.find_one({ "guild_id": ctx.guild.id })['whitelisted']
        for i in data:
            user_ = client.get_user(i)
            if user_ == None:
                user = 'Unable To Fetch Name'
            else:
                user = user_.name
            result += f"[{user}] :: {i}\n"
        with open(f'{ctx.guild.id}-Whitelisted.txt', 'a+') as f:
            f.write(result)
            f.close()
        await ctx.send(f"Whitelisted List Of your server", file=discord.File(f'{ctx.guild.id}-Whitelisted.txt'))
        os.remove(f'{ctx.guild.id}-Whitelisted.txt')
    else:
        await ctx.send(f"Ask {ctx.guild.owner} to use it")

@client.command()
async def botinfo(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='Botinfo', icon_url='https://images-ext-1.discordapp.net/external/bDDxuClUX8snm7AW2BaVX2T5ZbcTBnnNuksYk8xRMq4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777437789356032011/a_be571618bce1786ab1042378e166284d.gif?width=408&height=408')
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/bDDxuClUX8snm7AW2BaVX2T5ZbcTBnnNuksYk8xRMq4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777437789356032011/a_be571618bce1786ab1042378e166284d.gif?width=408&height=408')
    embed.add_field(name='Name', value='`Protected`', inline=False)
    embed.add_field(name='Server Count', value=f'`{len(client.guilds)}`', inline=False)
    embed.add_field(name='User Count', value= f'`{sum([len(guild.members) for guild in client.guilds])}`', inline=False)
    embed.add_field(name='Ping', value=f'`{int(client.latency * 1000)}`', inline=False)
    embed.add_field(name='Languages', value=f'`discord.js + discord.py`', inline=False)
    embed.set_footer(text='Ravager Development', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)



@client.event
async def on_guild_join(guild):
    server = client.get_guild(guild.id)
    ProtectedSystem.NewServer(guild.owner.id, guild.id)
    log_channel = client.get_channel(915310165832663060)
    embed = discord.Embed(color=0, description=f'Joined New Server!')
    embed.add_field(name='Server Name', value=f'**`{server.name}`**')
    embed.add_field(name='Server Owner', value=f'**`{server.owner}`**')
    embed.add_field(name='Server Members', value=f'**`{len(server.members)}`**')
    embed.set_footer(text='Ravager Development')
    embed.set_author(name='Project Protected', icon_url='https://images-ext-1.discordapp.net/external/bDDxuClUX8snm7AW2BaVX2T5ZbcTBnnNuksYk8xRMq4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777437789356032011/a_be571618bce1786ab1042378e166284d.gif?width=408&height=408')
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/bDDxuClUX8snm7AW2BaVX2T5ZbcTBnnNuksYk8xRMq4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777437789356032011/a_be571618bce1786ab1042378e166284d.gif?width=408&height=408')
    await log_channel.send(embed=embed)



@client.command()
@commands.is_owner()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f"Dne loading The {extention}")

@client.command(aliases=["ms", "aliases!"]) # You make make the command respond to other commands too
async def ping(ctx, a_variable): # a_variable is a argument you use in the command
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms. Your input was {a_variable}")


@client.command()
async def ban(ctx, member: discord.Member = None, *, reason = None):
    if ctx.author.id == ctx.guild.owner.id:
        if reason == None:
            await member.ban(reason=f'Banned By {ctx.author} With No Reason Provided...')
            await ctx.send(f"{member} was banned! With No Reason Provided")
        elif member == None:
            await ctx.send("Pls Provide A Member To Ban")
        else:
            await member.ban(f'Banned By {ctx.author} || {reason}')
            await ctx.send(f"{member} was banned by {ctx.author} with reason {reason}")
    else:
        await ctx.send(f"Ask {ctx.guild.owner} To Ban Buddy")

@client.command()
@commands.has_permissions(administrator=True)
async def whitelist(ctx, member: discord.Member = None):
    if ctx.author.id == ctx.guild.owner.id:
        if member == None:
            await ctx.send("Please Specify A Member To Whitelist")
        else:
            db.update_one({ "guild_id": ctx.guild.id }, { "$push": { "whitelisted": member.id}})
            await ctx.send(f'Whitelisted {member.name}')
    else:
        await ctx.send(f"Only {ctx.server.owner} Can Run This Command")

@client.command()
@commands.has_permissions(administrator=True)
async def unwhitelist(ctx, member: discord.Member = None):
    if ctx.author.id == ctx.guild.owner.id:
        if member == None:
            await ctx.send("Please Specify A Member To Un Whitelist")
        else:
            db.update_one({ "guild_id": ctx.guild.id }, { "$pull": { "whitelisted": member.id }})
            await ctx.send(f'Un Whitelisted {member.name}')
    else:
        await ctx.send(f"Only {ctx.server.owner} Can Run This Command")

@client.command()
async def kick(ctx, member: discord.Member = None, *, reason = None):
    if ctx.author.id == ctx.guild.owner.id:
        if reason == None:
            await member.kick(reason=f'kickned By {ctx.author} With No Reason Provided...')
            await ctx.send(f"{member} was kickned! With No Reason Provided")
        elif member == None:
            await ctx.send("Pls Provide A Member To kick")
        else:
            await member.kick(f'kickned By {ctx.author} || {reason}')
            await ctx.send(f"{member} was kickned by {ctx.author} with reason {reason}")
    else:
        await ctx.send(f"Ask {ctx.guild.owner} To kick Buddy")


@client.command()
async def invite(ctx):
    await ctx.send("INVITE ME !!", components=buttons)
	
	

@client.command()
@commands.is_owner()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    await ctx.send(f"Dne Unloading The {extention}")



for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')





client.run(token)
