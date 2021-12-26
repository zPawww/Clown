import discord
from discord.ext import commands
import datetime
import asyncio
from discord import Permissions, embeds
from colorama import Fore, Style
import random
import time
import sys

class TestCog(commands.Cog):
  def __init__(self, client):
    self.client = client

# Help Command

  @commands.command()
  async def help(self,ctx):
    embed = discord.Embed(title="Commands to Clown",description="",timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.add_field(name="► Help menu",value="We have 2 categories and more than 20 commands created. \n\n Command list: !help <category>ﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ")
    embed.add_field(name="► Category",
                    value='''

    `c!mod` = Moderator Commands                
    `c!fun` = Commands to laugh
    `c!romance` = Romance commands
    `c!musica` = Music commands

    ''',
                    inline="False")
    embed.add_field(name="► Links",value="[Website](http://google.com) | [Privacy](http://youtube.com) | [Commands]( http://wikipedia.com)",  inline="False")
    await ctx.send(embed=embed)

# Help Mod

  @commands.command()
  async def mod(self,message):
    embed = discord.Embed(
        title="Commands to Clown",
        description="",
        color=discord.Color.blue())
    embed.add_field(name="Moderador", value="Moderator Commands Helpﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ", inline="False")
    embed.add_field(name="**Commands**",value='''
    kick
    ban
    mute
    ''',  inline="True")
    embed.add_field(name="**ﾠﾠﾠﾠﾠﾠﾠﾠ**",value='''
    clear
    nuke
    none
    ''', inline="True")
    embed.add_field(name="**ﾠﾠﾠﾠﾠﾠﾠﾠ**",value='''
    none
    none
    none
    ''')
    await message.channel.send(embed=embed)
    
# Help Fun

  @commands.command()
  async def fun(self,message):
    embed = discord.Embed(
        title="Commands to Clown",
        description="",
        color=discord.Color.blue())
    embed.add_field(name="Fun", value="Help on fun commandsﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ", inline="False")
    embed.add_field(name="**Commands**",value='''
    banana
    avatar
    lucky
    ''',  inline="True")
    embed.add_field(name="**ﾠﾠﾠﾠﾠﾠﾠﾠ**",value='''
    roll
    8ball
    whois
    ''', inline="True")
    embed.add_field(name="**ﾠﾠﾠﾠﾠﾠﾠﾠ**",value='''
    none
    none
    none
    ''')
    await message.channel.send(embed=embed)

  @commands.command()
  async def romance(self,message):
    embed = discord.Embed(
        title="Commands to Clown",
        description="",
        color=discord.Color.blue())
    embed.add_field(name="Romance", value="Romance Commands Helpﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ", inline="False")
    embed.add_field(name="**Commands**",value='''
    hug
    kiss
    none
    ''',  inline="True")
    embed.add_field(name="**ﾠﾠﾠﾠﾠﾠﾠﾠ**",value='''
    none
    none
    none
    ''', inline="True")
    embed.add_field(name="**ﾠﾠﾠﾠﾠﾠﾠﾠ**",value='''
    none
    none
    none
    ''')
    await message.channel.send(embed=embed)


  @commands.command()
  async def music(self,ctx):
    embed = discord.Embed(title="Commands to Music",description="",timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.add_field(name="► Command menu",value="We have 4 music commands, the music mode is still being developed there are bugs but it works correctly. \n\n If you have a music listening with the bot and you add another it will not work, you have to wait for your song to finish and then add the next one, we are working to fix that \n\n Command listﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ")
    embed.add_field(name="► Commands",
                    value='''

    `c!play` = Add music to the audio channel                
    `c!leave` = Leave the audio channel

    ''',
                    inline="False")
    embed.add_field(name="► Links",value="[Website](http://google.com) | [Privacy](http://youtube.com) | [Commands]( http://wikipedia.com)",  inline="False")
    await ctx.send(embed=embed)


def setup(client):
  client.add_cog(TestCog(client))