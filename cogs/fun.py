import discord
from discord.ext import commands
import datetime
import asyncio
from discord import Permissions, embeds
from colorama import Fore, Style
import random
import time
import sys

class FunCog(commands.Cog):
  def __init__(self, client):
    self.client = client

# Command Meme

  @commands.command()
  async def meme(self,ctx):
    memesszx = [
    "https://tenor.com/view/peppa-pig-minecraft-meme-peppa-pig-minecraft-meme-gif-14960039",
    "https://tenor.com/view/spongebob-nickelodeon-handsome-squidward-funny-meme-gif-14625359",
    "https://tenor.com/view/bye-memes-dead-wow-incredible-gif-12520076",
    "https://tenor.com/view/meme-gif-13939251",
    "https://tenor.com/view/dance-baby-fun-varinha-gif-4766783",
    "https://tenor.com/view/baseball-mlb-slide-butt-ass-gif-9642083"
]
    randomsxa = random.choice(memesszx)
    await ctx.send(f" {randomsxa}")

# Command Hack

  @commands.command(pass_context = True)
  async def hack(self,message,ctx, member:discord.Member):
    message = await message.channel.send("Hacking! Target: " + "@" + ctx.message.author.mention())
    await asyncio.sleep(2)
    await message.edit(content="Accessing discord files...")
    await asyncio.sleep(2)
    await message.edit(content="Discord files hacked...")
    await asyncio.sleep(2)
    await message.edit(content="Logging into account " + f'{member.display_name}')
    await asyncio.sleep(2)
    await message.edit(content="Trying to log into the account ...")
    await asyncio.sleep(2)
    await message.edit(content="An error has occurred trying to enter the account, try again❌")

# Command Banana

  @commands.command(pass_context = True)
  async def banana(self,ctx):
    size = [
  "7",
  "10",
  "11",
  "13",
  "15",
  "17",
  "19",
  "18",
  "21",
  "20",
  "19",
  "24",
  "25",
  "40",
  "8",
  "12",
  "16",
  "9",
]
    sizex = random.choice(size)
    embed = discord.Embed(title=f"The banana of{ctx.message.author.name} is {sizex}cm",description=" ",color=discord.Color.blue())
    embed.set_image(url="https://media1.giphy.com/media/1AD3TMRwXlNgk/giphy.gif")
    await ctx.send(embed=embed)

  @commands.command()
  async def roll(self,ctx):
    rollrandom = [
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "10"
]

    rollchoice = random.choice(rollrandom)
    embed = discord.Embed(title=f"🎲 {ctx.message.author.name} has rolled a die where the odds are from (1-10) and has rolled {rollchoice}",description=" ",color=discord.Color.blue())
    embed.set_image(url="https://media1.giphy.com/media/M9HNXnSW3CFqIF6USF/giphy.gif")
    await ctx.send(embed=embed)

  @commands.command(aliases=['whois'])
  async def userinfo(self,ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On :", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On : ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in member.roles[1:]]))
    embed.add_field(name="Highest Role", value=member.top_role.mention)
    await ctx.send(embed=embed)


  @commands.command()
  async def lucky(self,ctx):
    suerte = ['6','7','8','9','12','25','28','34','37','40','50','70','78','80','85','90','96','100']
    dinero = ['6','7','8','9','12','25','28','34','37','40','50','70','78','80','85','90','96','100']
    amor = ['6','7','8','9','12','25','28','34','37','40','50','70','78','80','85','90','96','100']
    suerterandom = random.choice(suerte)
    dinerorandom = random.choice(dinero)
    amorrandom = random.choice(amor)
    embed = discord.Embed(title=f"Clown says lucky {ctx.message.author.name} is:",description="🍀 Lucky: " + suerterandom + "\n :heart: Love: " + amorrandom + "\n 💰 Money: " + dinerorandom + "ﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ", color=discord.Color.blue())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


  
  @commands.command()
  async def avatar(self,ctx, member: discord.Member = None):
    if not member:
      member = ctx.message.author
    userAvatar = member.avatar_url
    embed = discord.Embed(title='',description='', color= discord.Color.blue())
    embed.set_image(url=userAvatar)
    await ctx.send(embed=embed)


 
 
 

def setup(client):
  client.add_cog(FunCog(client))