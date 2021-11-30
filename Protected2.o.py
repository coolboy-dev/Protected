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







token = 'ODA2MDY2Njk2MDMzMDA5NjY1.YBkCHA.yV5Y1RXdvO0Bay_JDn5Hl7BMSNc'
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
        Button(style=ButtonStyle.URL, label='SUPPORT SERVER !', url='https://discord.com/api/oauth2/authorize?client_id=852194474292412427&permissions=8&scope=bot%20applications.commands'),
        Button(style=ButtonStyle.URL, label='INVITE ME !', url='https://discord.com/api/oauth2/authorize?client_id=852194474292412427&permissions=8&scope=bot%20applications.commands')
    ],
]


@client.command()
async def help(ctx):
    e = discord.Embed()
    e.add_field(name='**Protected 2.O**' , value="Whitelist - Bot Will Ignore That Person\n UnWhitelist - Remove Whitelisted Member\n Ban - Ban A Member \n Kick - Kick A Member")
    e.set_author(name="Project Protected")
    e.set_footer(text='Ravager Development', icon_url='https://images-ext-1.discordapp.net/external/bDDxuClUX8snm7AW2BaVX2T5ZbcTBnnNuksYk8xRMq4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777437789356032011/a_be571618bce1786ab1042378e166284d.gif?width=408&height=408')
    e.set_thumbnail(url='https://images-ext-1.discordapp.net/external/bDDxuClUX8snm7AW2BaVX2T5ZbcTBnnNuksYk8xRMq4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777437789356032011/a_be571618bce1786ab1042378e166284d.gif?width=408&height=408')
    await ctx.send(embed=e, components=buttons)





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
@commands.is_owner()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    await ctx.send(f"Dne Unloading The {extention}")



for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')





client.run(token)