import discord
from discord.ext import commands
import datetime
import asyncio
from discord import Permissions, embeds
from colorama import Fore, Style
import random
import time
import sys

class ModCog(commands.Cog):
  def __init__(self, client):
    self.client = client

# Help Clear

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx, amount=100):
    amount = int(amount)
    amount = amount+1
    user_name = ctx.author.name
    user_id = ctx.author.discriminator
    username = f'`{user_name}#{user_id}`'
    title = ''
    await ctx.channel.purge(limit=amount) 
    embed = discord.Embed(
        title=title, description=f'`Number of deleted messages:` `{amount-1}`', color=discord.Color.blue())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Made by {ctx.author.name}")
    await ctx.send(embed=embed)

# Help Nuke

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def nuke(self,ctx, amount=9000):
    embed = discord.Embed(
        title="Clown Bot",
        description="Clown, I exploded a nuclear bomb by accident",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.purple())
    embed.add_field(name="All conversation has been removed from the channel",
                    value="Clown says he's sorry :c",
                    inline="False")
    embed.set_thumbnail(
        url=
        "https://t3.ftcdn.net/jpg/03/33/09/88/360_F_333098851_oaiN8o7glILcg7nsT1vhSPewI1wSjzyN.jpg"
    )
    embed.set_image(
        url=
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/41606d9e-1486-4bb8-a9b4-eba3eccb1b35/ddmmjz8-10a4c85f-41d7-4d16-b011-e329762165a7.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzQxNjA2ZDllLTE0ODYtNGJiOC1hOWI0LWViYTNlY2NiMWIzNVwvZGRtbWp6OC0xMGE0Yzg1Zi00MWQ3LTRkMTYtYjAxMS1lMzI5NzYyMTY1YTcuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Gj7uC00OS8Ow8mAvS0SHWz0ecu9E_EQilFjEqK-FKrk"
    )
    await ctx.send(embed=embed)

# Help Ban

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx, member: discord.Member, *, reason=None):
    try:
      await member.ban(reason=reason)
      await ctx.message.delete()
      await ctx.channel.send(
            f'{member.name} You have been banned from this server by the '
            f'Reason: {reason}')
    except Exception:
      await ctx.channel.send("A")
      
# Help Kick

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx, user: discord.Member, *, reason="No reason provided"):
    await user.kick(reason=reason)
    kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}ﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ")
    await ctx.message.delete()
    await ctx.channel.send(embed=kick)
    await user.send(embed=kick)
  
  
def setup(client):
  client.add_cog(ModCog(client))