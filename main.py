import discord
from webserver import keep_alive
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")

keep_alive()
BOT_TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(BOT_TOKEN)
