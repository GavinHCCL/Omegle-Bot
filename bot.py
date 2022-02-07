import discord
import random
import time
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "-", intents = intents)

client.remove_command('help')

#When bot is on

@client.event
async def on_ready():
    print("Omegle Bot is ready!")
    game = discord.Game("Busy Chatting rn!")
    await client.change_presence(status=discord.Status.online, activity=game)
#Commands

@client.command(aliases = ["Help"])
async def help(ctx):
    helpembed = discord.Embed(title="Help Commands",
                       description=f"Just chat in the bots dm and you can talk to everyone who is in a server with the bot!",
                       color=0xF97EE6)
    await ctx.send(embed=helpembed)

#Anon chat commmand


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.guild:
        yuh = message.author.discriminator + ": " + message.content
        print(message.author.discriminator + ": " + message.content)
        for guild in client.guilds:
            for channel in guild.channels:
                if(channel.name == 'chat'):
                    await channel.send(yuh)
                else:
                    if(channel.name != 'chat'):
                        pass
        members = guild.members
        for member in members:
            try:
                await member.send(message.author.discriminator + ": " + message.content)
            except:
                pass





client.run("TOKEN HERE!")
