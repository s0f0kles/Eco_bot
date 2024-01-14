import discord
from discord.ext import commands
from config import TOKEN
from random import choice
from os import listdir

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Обработка события при запуске бота
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$what recycling materials do you offer me?'):
        await message.channel.send('Hello friend, I am an Eco bot who can give you different ideas for recycling plastic, cardboard and glass.')
    if message.content.startswith('$How can I find out about recycling ideas?'):
        await message.channel.send('If you are interested in my ideas for recycling YOUR material, write it in the chat (!material, e.g. !plastic/cardboard/glass)')
    await bot.process_commands(message)

# Обработка команды для отправки мема
@bot.command()
async def hi(ctx):
    image_files = listdir('images')
    random_meme = choice(image_files)
    picture = discord.File(f'images/{random_meme}')
    await ctx.send(file=picture)

@bot.command(name='plastic')
async def plastic(ctx):
    random_ideas_plastic = choice([
        'Idea 1: https://recyclops.com/7-creative-ways-to-recycle-plastic-bottles/',
        'Idea 2: https://secondlife.earth/learning-center/plastic-recycling-ideas/',
        'Idea 3: https://foshbottle.com/blogs/fosh/60-ways-to-reuse-plastic-bottles',
    ])

    await ctx.send(f'Here is an idea based on your material: {random_ideas_plastic}')

    random_youtube_links_plastic = choice([
        'Link 1: https://www.youtube.com/watch?v=9wHWKPaS9jM',
        'Link 2: https://www.youtube.com/watch?v=HZ6f5W5PrvM',
        'Link 3: https://www.youtube.com/watch?v=VP_Fk8-vGVg'
    ])

    await ctx.send(f'If you are interested, watch this video on YouTube: {random_youtube_links_plastic}')


@bot.command(name='cardboard')
async def cardboard(ctx):
    random_ideas_cardboard = choice([
        'Idea 1: https://planetsave.com/articles/8-ideas-to-recycle-cardboard-into-something-useful/',
        'Idea 2: https://www.pinterest.com/boxplayforkids/recycled-cardboard-crafts/',
        'Idea 3: https://simplelifeofalady.com/20-ways-to-recycle-cardboard/',
    ])

    await ctx.send(f'Here is an idea based on your material: {random_ideas_cardboard}')

    random_youtube_links_cardboard = choice([
        'Link 1: https://www.youtube.com/watch?v=w-ZhZj-0VME',
        'Link 2: https://www.youtube.com/watch?v=OprQZ_OZrf4',
        'Link 3: https://www.youtube.com/watch?v=6dvli6DLI_k'
    ])

    await ctx.send(f'If you are interested, watch this video on YouTube: {random_youtube_links_cardboard}')


@bot.command(name='glass')
async def cardboard(ctx):
    random_ideas_glass = choice([
        'Idea 1: https://www.pinterest.com/vdesigner007/recycled-glass-ideas/',
        'Idea 2: https://www.budgetdumpster.com/blog/reusing-glass-bottles-and-jars/',
        'Idea 3: https://www.kissplanet.shop/en/blog/zero-waste-kitchen-7/10-original-ideas-to-reuse-your-glass-bottles-128',
    ])

    await ctx.send(f'Here is an idea based on your material: {random_ideas_glass}')

    random_youtube_links_glass = choice([
        'Link 1: https://www.youtube.com/watch?v=_OJ6Hz5vFNY',
        'Link 2: https://www.youtube.com/watch?v=BYoMMs7pr98',
        'Link 3: https://www.youtube.com/watch?v=zrl8vmhqCT4'
    ])

    await ctx.send(f'If you are interested, watch this video on YouTube: {random_youtube_links_glass}')


bot.run(TOKEN)
