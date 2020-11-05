#html2text web browser for discord bots created by smartfrigde#5834 . 
#keep in mind this can leak your location etc.
from bs4 import BeautifulSoup
import urllib.request
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix=',', description="Text Browser in Discord Bot! ")

@bot.command(pass_context=True, brief="Search the web with this cool web browser.", description='Search the web with this cool web browser.')
async def web(ctx, url):
    await ctx.send('Experimental Text Web Browser')
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    await ctx.send(output)

bot.run('TOKEN') #paste your token here
