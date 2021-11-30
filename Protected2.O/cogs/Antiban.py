import discord
from discord.ext import commands
import pymongo

class AntiBan(commands.Cog):


    

    def __init__(self, client):
        self.client = client
    
    mongoClient = pymongo.MongoClient('mongodb://COOOLLLLLLBOYYYYY:qCpIslnCXm7qT9iM@forbeast-shard-00-00.wcenb.mongodb.net:27017,forbeast-shard-00-01.wcenb.mongodb.net:27017,forbeast-shard-00-02.wcenb.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-kpgs1i-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = mongoClient.get_database("Protected").get_collection("servers")
    db2 = mongoClient.get_database("Protected").get_collection("protection")





    @commands.Cog.listener()
    async def on_member_unban(self, guild, user : discord.User):
        try:
            logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
            owner = guild.owner
            logs = logs[0]
            reason = "BEAST IS BACK BUDDY || MEMBER UNBAN"
            whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
            if logs.user.id == owner.id:
                return
            elif logs.user.id in whitelisted:
                return
            elif self.client.user.id == logs.user.id:
                return
            else:
                pass
            member_id = user.id
            await logs.user.ban(reason=reason)
            await user.ban(user=member_id, reason="NO UNBAN BABU")
        except:
            pass



    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        try:
            logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
            owner = guild.owner
            logs = logs[0]
            reason = "BEAST IS BACK BUDDY || MEMBER BAN"
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
            await user.unban(reason="SORRY BABU")
        except:
            pass


def setup(client):
    client.add_cog(AntiBan(client))