import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("=" * 40)
    print(f"NexusHost test bot is ONLINE!")
    print(f"Logged in as: {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print(f"Servers: {len(bot.guilds)}")
    print("=" * 40)


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! `{latency}ms`")


@bot.command()
async def test(ctx):
    await ctx.send("✅ NexusHost Python hosting works!")


@bot.command()
async def info(ctx):
    await ctx.send(
        f"🐍 Python bot running successfully!\n"
        f"📡 Ping: `{round(bot.latency * 1000)}ms`\n"
        f"🌐 Servers: `{len(bot.guilds)}`"
    )


if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN is missing. Add it to your NexusHost environment variables."
    )

bot.run(TOKEN)
