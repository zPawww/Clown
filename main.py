import os

my_secret = os.environ['DISCORD_BOT_SECRET']
import discord
from discord import activity
from discord import embeds
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
import datetime
import asyncio
from discord import Permissions, embeds
from colorama import Fore, Style
import random
import sys
from webserver import keep_alive
from requests import get
from discord import FFmpegPCMAudio
from discord import client
from discord.ext import commands
from youtube_dl import YoutubeDL
import requests
from random import randint
import json


bot = commands.Bot(command_prefix='c!', intents = discord.Intents.all(), help_command=None) 
intents = discord.Intents.default()
intents.members = True
# Prefix

# Status presence and bot on

@bot.event
async def on_ready():
    print("Bot is ready")
    while True:  # BUCLE
        await bot.change_presence(activity=discord.Game(name="🆘 c!help"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(
            name="⚙ Creator by Paw#0743"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(
            name="🛠 Clown created to help users"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name="😴 sleeping..."))
        await asyncio.sleep(15)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title='You lack an argument steve',description=" ", color=discord.Color.blue())
        embed.set_image(url="https://media2.giphy.com/media/ViZylgfPSfJFm/giphy.gif")
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(title="You do not have the permits and because of that you will take a rickroll, Merry Christmas !!",description=" ", color=discord.Color.blue())
      embed.set_image(url="https://c.tenor.com/u9XnPveDa9AAAAAC/rick-rickroll.gif")
      await ctx.send(embed=embed)


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

# Music Bot

def search(query):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        try:
            requests.get(query)
        except:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        else:
            info = ydl.extract_info(query, download=False)
    return (info, info['formats'][0]['url'])
@bot.command(name="Join",help="joins the channel the author is in", aliases=["join", "J", "j"])
async def Join(context):
    member_voice = context.author.voice
    if member_voice and member_voice.channel:
        if context.voice_client:
            await context.send("Bot already in a voice channel!")
        else:
            try:
                await member_voice.channel.connect()
                await context.send("Successfully connected to voice channel!")
            except:
                await context.send("An error occured make sure you're in a voice channel!")
@bot.command(name="Leave",help="Leaves the channel the bot is currently in", aliases=["leave", "L", "l"])
async def Leave(context):
    member_voice = context.author.voice
    if member_voice and member_voice.channel:
        if context.voice_client:
            if member_voice.channel == context.voice_client.channel:
                try:
                    if context.voice_client.is_playing():
                        context.voice_client.stop()
                        await context.voice_client.disconnect()
                        await context.send("Successfully disconnected to voice channel!")
                    else:
                        await context.voice_client.disconnect()
                        await context.send("Successfully disconnected to voice channel!")
                except:
                    await context.send("An error occured!")
            else:
                await context.send("You must be in the same voice channel as the bot!")
        else:
            await context.send("Bot is not in a voice channel!")
@bot.command(name="Play",help="Plays a song", aliases=["play","P","p"])
async def play(ctx,*,query):
    member_voice = ctx.author.voice
    if member_voice and member_voice.channel:
        if ctx.voice_client:
            client_voice = ctx.voice_client
            video, source = search(query)
            embed = discord.Embed(title="Now Playing 🎶",description=f"{video['title']}                                  ",color=discord.Color.blue())
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
            client_voice.play(FFmpegPCMAudio(source))
            client_voice.is_playing()
        else:
            await member_voice.channel.connect()
            client_voice = ctx.voice_client
            video, source = search(query)
            embed = discord.Embed(title="Now Playing 🎶",description=f"{video['title']}                                  ",color=discord.Color.blue())
            embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
            client_voice.play(FFmpegPCMAudio(source))
            client_voice.is_playing()


# Reaction role 
# Discord bot run

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
