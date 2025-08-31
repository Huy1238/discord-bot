import discord
from discord.ext import commands

TOKEN = "MTQxMTI2NjAzMDk0ODQ1MDM2Nw.G3h3jH.UScROKlqPXBpeGR97KLx9Q52M72gCvACYU"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập dưới tên {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Chào {ctx.author.mention} 👋!")

bot.run(TOKEN)
commit message: Add bot.py
