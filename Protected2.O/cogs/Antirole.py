import discord
from discord.ext import commands
import pymongo

class Antirole(commands.Cog):


    

    def __init__(self, client):
        self.client = client
    
    mongoClient = pymongo.MongoClient('mongodb://COOOLLLLLLBOYYYYY:qCpIslnCXm7qT9iM@forbeast-shard-00-00.wcenb.mongodb.net:27017,forbeast-shard-00-01.wcenb.mongodb.net:27017,forbeast-shard-00-02.wcenb.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-kpgs1i-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = mongoClient.get_database("Protected").get_collection("servers")
    db2 = mongoClient.get_database("Protected").get_collection("protection")


    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        try:

            guild = role.guild
            logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
            owner = guild.owner
            logs = logs[0]
            reason = "BEAST IS BACK BUDDY || ROLE CREATE"
            whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
            if logs.user.id == owner.id:
                return
            elif logs.user.id in whitelisted:
                return
            elif self.client.user.id == logs.user.id:
                return
            else:
                pass
        
            await role.delete()

            await logs.user.ban(reason=reason)
        except:
            pass



    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        try:

            guild = role.guild
            logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
            owner = guild.owner
            logs = logs[0]
            reason = "BEAST IS BACK BUDDY || ROLE DELETE"
            whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
            if logs.user.id == owner.id:
                return
            elif logs.user.id in whitelisted:
                return
            elif self.client.user.id == logs.user.id:
                return
            else:
                pass
        

            await logs.user.ban(reason=reason)
        except:
            pass



    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        try:
            guild = after.guild
            logs = await guild.audit_logs(limit=2, action=discord.AuditLogAction.role_update).flatten()
            owner = guild.owner
            logs = logs[0]
            reason = "BEAST IS BACK BUDDY || role UPDATE"
            whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
            if logs.user.id == owner.id:
                return
            elif logs.user.id in whitelisted:
                return
            elif self.client.user.id == logs.user.id:
                return
            else:
                pass
        

            await logs.user.ban(reason=reason)
        except:
            pass


def setup(client):
    client.add_cog(Antirole(client))