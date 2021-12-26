import discord
from discord.ext import commands
import datetime
import asyncio
from discord import Permissions, embeds
from colorama import Fore, Style
import random
import time
import sys

class RomanceCog(commands.Cog):
  def __init__(self, client):
    self.client = client

# Command Kiss

  @commands.command()
  async def kiss(self,ctx, member:discord.Member):
    pruebmem = [
  "https://media0.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
  "https://media1.giphy.com/media/zkppEMFvRX5FC/giphy.gif",
  "https://media3.giphy.com/media/FqBTvSNjNzeZG/giphy.gif",
  "https://media3.giphy.com/media/IdzovcoOUoUM0/giphy.gif",
  "https://media0.giphy.com/media/bm2O3nXTcKJeU/giphy.gif",
  "https://media0.giphy.com/media/nyGFcsP0kAobm/giphy.gif",
  "https://media1.giphy.com/media/kU586ictpGb0Q/giphy.gif",
  "https://media4.giphy.com/media/wOtkVwroA6yzK/giphy.gif",
  "https://media1.giphy.com/media/gTLfgIRwAiWOc/giphy.gif",
  "https://media0.giphy.com/media/jR22gdcPiOLaE/giphy.gif",
  "https://media4.giphy.com/media/WynnqxhdFEPYY/giphy.gif",
  "https://media3.giphy.com/media/iseq9MQgxo4aQ/giphy.gif",
  "https://media1.giphy.com/media/QGc8RgRvMonFm/giphy.gif",
  "https://media4.giphy.com/media/11rWoZNpAKw8w/giphy.gif",
  "https://media4.giphy.com/media/pwZ2TLSTouCQw/giphy.gif",
  "https://media0.giphy.com/media/KmeIYo9IGBoGY/giphy.gif",
  "https://media1.giphy.com/media/7ZsnUYLno9IWI/giphy.gif",
  "https://media2.giphy.com/media/KH1CTZtw1iP3W/giphy.gif"
]
    embed = discord.Embed(title=ctx.message.author.name + " has given a kiss to " + member.display_name, description=" ", color=discord.Color.blue())
    embed.set_image(
      url=(random.choice(pruebmem)))
    await ctx.send(embed=embed)
  
# Hug Command

  @commands.command()
  async def hug(self,ctx, member:discord.Member):
    huggif = [
  "https://media1.giphy.com/media/49mdjsMrH7oze/giphy.gif",
  "https://media4.giphy.com/media/svXXBgduBsJ1u/giphy.gif",
  "https://media0.giphy.com/media/lrr9rHuoJOE0w/giphy.gif",
  "https://media1.giphy.com/media/qscdhWs5o3yb6/giphy.gif",
  "https://media3.giphy.com/media/IRUb7GTCaPU8E/giphy.gif",
  "https://media1.giphy.com/media/Y8wCpaKI9PUBO/giphy.gif",
  "https://media2.giphy.com/media/143v0Z4767T15e/giphy.gif",
  "https://media4.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
  "https://media0.giphy.com/media/QFPoctlgZ5s0E/giphy.gif",
  "https://media1.giphy.com/media/wnsgren9NtITS/giphy.gif",
  "https://media3.giphy.com/media/yziFo5qYAOgY8/giphy.gif",
  "https://media1.giphy.com/media/3ZnBrkqoaI2hq/giphy.gif",
  "https://media3.giphy.com/media/LIqFOpO9Qh0uA/giphy.gif",
  "https://media3.giphy.com/media/5eyhBKLvYhafu/giphy.gif",
  "https://media1.giphy.com/media/10BcGXjbHOctZC/giphy.gif",
  "https://media3.giphy.com/media/VXP04aclCaUfe/giphy.gif",
  "https://media4.giphy.com/media/FUiZjgshtlMly/giphy.gif",
  "https://media2.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
  "https://media1.giphy.com/media/du8yT5dStTeMg/giphy.gif"
]

    embed = discord.Embed(title=ctx.message.author.name + " has given a hug to " + member.display_name, description=" ", color=discord.Color.blue())
    embed.set_image(
      url=(random.choice(huggif)))
    await ctx.send(embed=embed)
    

def setup(client):
  client.add_cog(RomanceCog(client))