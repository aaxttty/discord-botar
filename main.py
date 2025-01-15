import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='a.', intents=discord.Intents.all())

TOKEN = 'MTIyNDc1MTQ5ODA4MTA3OTQwOA.G7qBHG.G7Wo6MJEKlE8QoXKy-9by5weSVryhJI-nibcl4'

@bot.event
async def on_ready():
    print("Bot ready!")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel() #ID ห้อง
    text = f"Welcome to the server, {member.memtion}!"
    await member.send(text) #ส่งข้อความส่วนตัว

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel() #ID ห้อง
    text = f"Thank you,{member.memtion}!"
    await member.send(text)

@bot.event
async def on_message(message):
    mes = message.content
    if mes == 'hello':
        await message.channel.send("ควย")

    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx. author.name}!")
bot.run(TOKEN)