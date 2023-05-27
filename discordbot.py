import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
import asynciod

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

botstatus = cycle(["command activate = !", "join https://discord.gg/sg4Qwgun if you need help","or type !hlp", "made by= theholyhuub"])
            
@tasks.loop(seconds=5)
async def changestatus():
    await client.change_presence(activity=discord.Game(next(botstatus)))

@client.event
async def on_ready():
    print("*biep* *biep* *biep*")
    print("ready and running")
    changestatus.start()

@client.command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000) 
    await ctx.send(f"pong! {bot_latency} ms.")

@client.command()
async def pong(ctx):
    while 1 == 1:
        await ctx.author.send("pong!")

@client.command()
async def sigma(ctx):
    await ctx.send("balz")

@client.command()
async def hlp(ctx):
    embed_message = discord.Embed(title="HELP", description="here are some commands", color=discord.Color.random())

    embed_message.set_author(name=f"Requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
    embed_message.set_thumbnail(url=ctx.guild.icon)
    embed_message.set_image(url="https://murraywoodswimandracquetclub.org/wp-content/uploads/2014/05/help.jpg")
    embed_message.add_field(name="command list:", value="!ping to see the ping of the bot. !pong let spam your self!. and !deez for a meme:) ", inline=False)
    embed_message.set_footer(text="ask if somthing not works!", icon_url=ctx.author.avatar)

    await ctx.send(embed = embed_message)

@client.command()
async def deez(ctx):
    embed_message = discord.Embed(title="NUTS", description="good taste man", color=discord.Color.random())

    embed_message.set_author(name=f"Requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
    embed_message.set_thumbnail(url=ctx.guild.icon)
    embed_message.set_image(url="https://www.tubefilter.com/wp-content/uploads/2023/02/mr-beast-deez-nuts.jpg")
    embed_message.add_field(name="times this command is ussed:", value="69.420,69", inline=False)
    embed_message.set_footer(text="jimi says deeznuts", icon_url=ctx.author.avatar)

    await ctx.send(embed = embed_message)

@client.command()
async def clear( ctx, count: int):
    await ctx.channel.purge(limit=count)
    await ctx.send(f"{count} message(s) deleted!")

@client.command()
async def kick(ctx, member: discord.Member, *, modreason):
    await ctx.guild.kick(member)
    
    kick_embed = discord.Embed(title="Succes!", color=discord.Color.green())
    kick_embed.add_field(name="kicked: ", value=f"{member.mention} by {ctx.author.mention}.", inline=False)
    kick_embed.add_field(name="reason: ", value=modreason, inline=False)

    await ctx.send(embed=kick_embed) 

@client.command()
async def ban(ctx, member: discord.Member, *, modreason):
    await ctx.guild.ban(member)

    ban_embed = discord.Embed(title="Succes!", color=discord.Color.green())
    ban_embed.add_field(name="banned: ", value=f"{member.mention} by {ctx.author.mention}.", inline=False)
    ban_embed.add_field(name="reason: ", value=modreason, inline=False)

    await ctx.send(embed=ban_embed)                       

client.run("put your own webhook here!")
