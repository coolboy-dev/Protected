import discord
from discord.ext import commands
import pymongo

class AntiKick(commands.Cog):


    

    def __init__(self, client):
        self.client = client
    
    mongoClient = pymongo.MongoClient('mongodb://COOOLLLLLLBOYYYYY:qCpIslnCXm7qT9iM@forbeast-shard-00-00.wcenb.mongodb.net:27017,forbeast-shard-00-01.wcenb.mongodb.net:27017,forbeast-shard-00-02.wcenb.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-kpgs1i-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = mongoClient.get_database("Protected").get_collection("servers")
    db2 = mongoClient.get_database("Protected").get_collection("protection")


    # @commands.Cog.listener()
    # async def on_member_remove(self, member):
    #     try:
    #         guild = member.guild
    #         logs = await guild.audit_logs(limit=5, action=discord.AuditLogAction.kick).flatten()
    #         owner = guild.owner
    #         logs = logs[0]
    #         reason = "BEAST IS BACK BUDDY || MEMBER KICK"
    #         whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
    #         if logs.user.id == owner.id:
    #             return
    #         elif logs.user.id in whitelisted:
    #                 return
    #         elif self.client.user.id == logs.user.id:
    #                 return
    #         else:  
    #                 pass
        

    #         await logs.user.ban(reason=reason)
    #     except:
    #             pass


def setup(client):
    client.add_cog(AntiKick(client))