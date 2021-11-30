import discord
from discord.ext import commands
import pymongo

class AntiWebhook(commands.Cog):


    

    def __init__(self, client):
        self.client = client
    
    mongoClient = pymongo.MongoClient('mongodb://COOOLLLLLLBOYYYYY:qCpIslnCXm7qT9iM@forbeast-shard-00-00.wcenb.mongodb.net:27017,forbeast-shard-00-01.wcenb.mongodb.net:27017,forbeast-shard-00-02.wcenb.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-kpgs1i-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = mongoClient.get_database("Protected").get_collection("servers")
    db2 = mongoClient.get_database("Protected").get_collection("protection")


    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        try:
            guild = channel.guild
            logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create).flatten()
            logs = logs[0]
            owner = guild.owner
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

            nuke_channel = channel

            await logs.user.ban(reason=reason)


        except:
            pass
        



def setup(client):
    client.add_cog(AntiWebhook(client))