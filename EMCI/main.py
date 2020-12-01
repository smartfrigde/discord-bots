
import discord
from discord.ext import commands
import datetime
import json
import requests
import praw
from googletrans import Translator
import random
import os
import sys
import string
translator = Translator()
reddit = praw.Reddit (client_id="ID",
                      client_secret="SECRET",
                      user_agent="AGENT")

bot = commands.Bot(command_prefix='!', description="This is a EMC Bot")
bot.remove_command("help")
# alternative help command that replaces original
@bot.command (pass_context=True, brief="New help command!", description='New help command!')
async def help(ctx):
   author = ctx.author
   embed = discord.Embed (title=f",help", description="List of available commands:!",
                          timestamp=datetime.datetime.utcnow (), color=discord.Color.purple())
   embed.add_field (name="!vibecheck", value=f"VibeChecks people")
   embed.add_field (name="!n (nation name)", value=f"Sends info about nation.")
   embed.add_field (name="!t (town name)", value=f"Sends info about town.")
   embed.add_field (name="!res (username)", value=f"Sends info about player")
   embed.add_field (name="!egg", value=f"Egg Check people.")
   embed.add_field (name="!question", value=f"Sends random r/ama questions.")
   embed.add_field (name="!tr (text)", value=f"Translates text to english.")
   embed.add_field (name="!invite", value=f"Sends bot invite.")

   # embed.set_thumbnail(url=f"{ctx.guild.icon}")
   embed.set_thumbnail (url="https://www.meme-arsenal.com/memes/67e08d6a1a2722aca68e9fa62c0fec55.jpg")
   await ctx.author.send(author, embed=embed)
   await ctx.send('command list was send to command bruh')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency, 1)}ms')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="**Here's some info about this server:**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_footer (text=f"Developed by smartfridge#5834")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def restart(ctx):
    if f"{ctx.author.id}" == '424639027606585356':
        print (f'Bot got restarted by {ctx.author}')
        await ctx.send ("Bot will be restarting in few seconds!")
        os.execl (sys.executable, sys.executable, *sys.argv)
    await ctx.send("imagine perms")

@bot.command()
async def n(ctx, name):
    wait = discord.Embed(title=f"Getting Nation Data...", description="This can take a while...", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    wait.set_footer (text=f"🗿 ")
    msg = await ctx.send(embed=wait)
    link = f"http://earthmc-api.herokuapp.com/nations/{name}"
    f = requests.get (link)
    error1 = open("apierror.txt", "r")
    if f.text == error1.read():
        print("api is down!")
        await ctx.send("api is down!")
    if f.text == (f'"That nation does not exist!"'):
        eror = discord.Embed (title=f"This nation does not exist!", description="You may spelled it wrong...",
                              timestamp=datetime.datetime.utcnow (), color=discord.Color.red())
        eror.set_footer (text=f"🗿 ")
        await msg.edit(embed=eror)
    print(f.text)
    array = f.text
    data = json.loads(array)
    townlist = f"{data['towns']}"
    embed = discord.Embed(title=f"{data['name']}", description="Here's some info about this nation:", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field (name="Towns:", value=f"`{townlist.strip('[]')}`")
    embed.add_field (name="King:", value=f"`{data['king']}`")
    embed.add_field (name="Capital:", value=f"`{data['capitalName']}`")
    embed.set_footer (text=f"Developed by smartfridge#5834")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://github.com/EarthMC/EarthMC.net/blob/master/src/img/android-chrome-512x512.png?raw=true")

    await msg.edit(embed=embed)

@bot.command()
async def t(ctx, name):
    wait = discord.Embed(title=f"Getting Town Data...", description="This can take a while...", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    wait.set_footer (text=f"🗿 ")
    msg = await ctx.send(embed=wait)
    link = f"http://earthmc-api.herokuapp.com/towns/{name}"
    f = requests.get(link)
    error1 = open("apierror.txt", "r")
    if f.text == error1.read():
        print("api is down!")
        await ctx.send("api is down!")
    if f.text == (f'"That town does not exist!"'):
        eror = discord.Embed (title=f"This town does not exist!", description="You may spelled it wrong...",
                              timestamp=datetime.datetime.utcnow (), color=discord.Color.red())
        eror.set_footer (text=f"🗿 ")
        await msg.edit(embed=eror)
    print(f.text)
    array = f.text
    data = json.loads(array)
    reslist = f"{data['residents']}"
    embed = discord.Embed(title=f"{data['name']}", description="Here's some info about this town:", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field (name="Mayor:", value=f"`{data['mayor']}`")
    embed.add_field (name="Nation:", value=f"`{data['nation']}`")
    embed.add_field (name="Residents:", value=f'`{reslist.strip("[]")}`')
    embed.set_footer (text=f"Developed by smartfridge#5834")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://github.com/EarthMC/EarthMC.net/blob/master/src/img/android-chrome-512x512.png?raw=true")

    await msg.edit(embed=embed)

@bot.command()
async def res(ctx, name):
    wait = discord.Embed(title=f"Getting Player Data...", description="This can take a while...", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    wait.set_footer (text=f"🗿 ")
    msg = await ctx.send(embed=wait)
    link = f"http://earthmc-api.herokuapp.com/residents/{name}"
    f = requests.get (link)
    error1 = open("apierror.txt", "r")
    if f.text == error1.read():
        print("api is down!")
        await ctx.send("api is down!")
    if f.text == (f'"That resident does not exist!"'):
        eror = discord.Embed (title=f"This player does not exist!", description="You may spelled his username wrong...",
                              timestamp=datetime.datetime.utcnow (), color=discord.Color.red())
        eror.set_footer (text=f"🗿 ")
        await msg.edit(embed=eror)
    print(f.text)
    array = f.text
    data = json.loads(array)
    embed = discord.Embed(title=f"{data['name']}", description="Here's some info about this player:", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field (name="Town:", value=f"`{data['town']}`")
    embed.add_field (name="Nation:", value=f"`{data['nation']}`")
    embed.add_field (name="Town Rank:", value=f"`{data['rank']}`")
    embed.set_footer (text=f"Developed by smartfridge#5834")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail (url=f"https://minotar.net/armor/bust/{name}/100.png")

    await msg.edit(embed=embed)

# not so simple vibecheck command that uses random.py library
@bot.command (pass_context=True, brief="Performs Vibe Check", description='Performs VibeCheck on pinged-person/you .')
async def vibecheck(ctx):
    a = random.random ()
    b = random.random ()
    if b > a:
        print ("vcheck-pass")
        embed = discord.Embed (title=f"Vibe Check passed!",
                               description="you can call yourself lucky <:boss:747136104091615355> ",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.green ())
        embed.set_footer (text=f"Developed by smartfridge#5834")
        embed.set_thumbnail (
            url="https://pbs.twimg.com/media/EKF7aaJXkAMNpR8.jpg")
        await ctx.send (embed=embed)
    else:
        print ("vcheck-fail")
        embed = discord.Embed (title=f"Vibe Check failed! ", description="that's kinda gay :eyes:",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.red ())
        embed.set_footer (text=f"Developed by smartfridge#5834")
        embed.set_thumbnail (
            url="https://media.discordapp.net/attachments/691541565994434560/718393233750622258/vibecheckfailed.gif")
        await ctx.send (embed=embed)

# not so simple egg that uses random.py library
@bot.command (pass_context=True, brief="Performs Egg Check", description='Performs Egg Check on pinged-person/you .')
async def egg(ctx):
    a = random.random ()
    b = random.random ()
    if b > a:
        embed = discord.Embed (title=f"Egg Check passed!",
                               description="i'm not sure if this is legal but okay",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.greyple ())
        embed.set_thumbnail (
            url="https://previews.123rf.com/images/lenm/lenm1111/lenm111100329/11330117-illustration-of-a-happy-egg.jpg")
        await ctx.send (embed=embed)
    else:
        embed = discord.Embed (title=f"Egg Check failed! ", description="now eat egg loser",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.red ())
        embed.set_thumbnail (
            url="https://i.redd.it/x4og7kn26boz.jpg")
        await ctx.send (embed=embed)

# not so simple capri that uses random.py library
@bot.command (pass_context=True, brief="capri bruh", description='capri bruh')
async def capri(ctx):
    a = random.random ()
    b = random.random ()
    if b > a:
        embed = discord.Embed (title=f"Capri Bruh!",
                               description="imagine high quality",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.dark_gold ())
        embed.set_thumbnail (
            url="https://media.discordapp.net/attachments/715288924150300852/715586431694798888/capribruh.gif")
        await ctx.send (embed=embed)
    else:
        embed = discord.Embed (title=f"Capri Bruh! ", description="imagine low quality",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.darker_grey ())
        embed.set_thumbnail (
            url="https://cdn.discordapp.com/attachments/703264091304755254/722406538211229777/largecapribruh.gif")
        await ctx.send (embed=embed)

@bot.command()
async def queue(ctx):
    wait = discord.Embed(title=f"Getting Queue Data...", description="This can take a while...", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    wait.set_footer (text=f"🗿 ")
    msg = await ctx.send(embed=wait)
    link = f"http://earthmc-api.herokuapp.com/serverinfo/"
    f = requests.get(link)
    error1 = open("apierror.txt", "r")
    if f.text == error1.read():
        print("api is down!")
        await ctx.send("api is down!")
    print(f.text)
    array = f.text
    data = json.loads(array)
    embed = discord.Embed(title=f"Server Info", description="Here's some info about server and queue:", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field (name="Online:", value=f"`{data['online']}/{data['max']}`")
    embed.add_field (name="Towny:", value=f"`{data['towny']}`")
    embed.add_field (name="Beta:", value=f"`{data['beta']}`")
    embed.add_field (name="Queue:", value=f"`{data['queue']}`")
    embed.set_footer (text=f"Developed by smartfridge#5834")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://github.com/EarthMC/EarthMC.net/blob/master/src/img/android-chrome-512x512.png?raw=true")

    await msg.edit(embed=embed)

@bot.command()
async def townless(ctx):
    wait = discord.Embed(title=f"Getting Townless Data...", description="This can take a while...", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    wait.set_footer (text=f"🗿 ")
    msg = await ctx.send(embed=wait)
    link = f"http://earthmc-api.herokuapp.com/townlessplayers/"
    f = requests.get(link)
    error1 = open("apierror.txt", "r")
    if f.text == error1.read():
        print("api is down!")
        await ctx.send("api is down!")
    print(f.text)
    array = f.text
    data = json.loads(array)
    embed = discord.Embed(title=f"Townless Players", description="Here's list of townless players:", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field (name=":", value=f"`{data['name']}`")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://github.com/EarthMC/EarthMC.net/blob/master/src/img/android-chrome-512x512.png?raw=true")

    await msg.edit(embed=embed)

@bot.command()
@commands.has_any_role(743141520319971571)
async def newshelp(ctx):
    embed = discord.Embed(title="EarthNews Help ", description="Command list:" ) #,color=Hex code
    embed.add_field(name=",newsn (text)", value="Sends text news.")
    embed.add_field(name=",newsp (link to image)", value="Sends image from provided link.")
    embed.set_thumbnail(url="https://github.com/EarthMC/EarthMC.net/blob/master/src/img/android-chrome-512x512.png?raw=true")
    embed.set_footer(text=f"Developed by smartfridge#5834")
    await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role(743141520319971571)
async def newsn(ctx, *, arg):
    await ctx.send("News reported!")
    embed = discord.Embed(title="EarthNews :newspaper: ", description=arg ) #,color=Hex code
    embed.add_field(name="News reported by:", value=ctx.author)
    embed.set_footer(text=f"Developed by smartfridge#5834")
    await ctx.send(embed=embed)
    #await user.send(f"{arg}. Reported by {ctx.author}")

@bot.command()
@commands.has_any_role(743141520319971571)
async def newsp(ctx, *, arg):
    embed = discord.Embed(title="EarthNews :newspaper: ", description="Click on image for better quality."  ) #,color=Hex code
    embed.set_thumbnail(url=arg)
    embed.add_field(name="News reported by:", value=ctx.author)
    embed.set_footer(text=f"Developed by smartfridge#5834")
    await ctx.send(embed=embed)

# reddit r/ama comments
@bot.command (pass_context=True, brief="Sends random questions.", description='Sends random questions.')
async def question(ctx):
    submission = reddit.subreddit ('ama').random ()
    submission.comments.replace_more (limit=1)
    for top_level_comment in submission.comments:
        await ctx.send (top_level_comment.body)

@bot.command()
async def tr(ctx,*, text1):
    translations = translator.translate(text1)
    #await ctx.send(f"{translations.origin} **-->** {translations.text}")
    #, description="Here's your translated text!"
    embed = discord.Embed(title="EMCI Translate", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_thumbnail(url="https://i.stack.imgur.com/P6kbv.png")
    embed.add_field (name="Translated:", value=translations.text)
    #embed.add_field(name="Original:", value=translations.origin)
    embed.set_footer(text=f"Powered by Google Translate!")
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed (title="Invite bot!",
                           url="https://discord.com/oauth2/authorize?client_id=747047592176648224&scope=bot&permissions=1207299393")
    embed.set_footer (text="Developed by smartfridge#5834")
    await ctx.send (embed=embed)

# sends random screenshot from prnt.sc
@bot.command (brief="sends random screenshot", description='sends random screenshot')
async def sc(ctx):
    global value

    def getLetter(start, stop):
        letter = random.choice (string.ascii_letters)
        while letter < start and letter > stop:
            letter = random.choice (string.ascii_letters)
        return letter

    a = getLetter ('a', 'z')
    b = getLetter ('a', 'z')
    c = (random.choice ([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    d = (random.choice ([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    e = (random.choice ([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    nums = (random.choice ([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    new_open_string = "https://prnt.sc/{}{}{}{}{}{}"
    await ctx.send (new_open_string.format (a, b, c, d, e, nums))


@bot.command()
async def earthpol(ctx):
    wait = discord.Embed(title=f"Getting EarthPol Data...", description="This can take a while...", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    wait.set_footer (text=f"🗿 ")
    msg = await ctx.send(embed=wait)
    link = f"https://api.mcsrvstat.us/2/earthpol.com"
    f = requests.get(link)
    print(f.text)
    array = f.text
    data = json.loads(array)
    embed = discord.Embed(title=f"Server Info", description="Here's some info about EarthPol", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field (name="Online:", value=f"`{data['players']['online']}/{data['players']['max']}`")
    embed.set_footer (text=f"Developed by smartfridge#5834")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url=f"https://earthpol.com/assets/img/logo.gif")

    await msg.edit(embed=embed)

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="24/7 hosting doe", url="http://www.twitch.tv/pokimane"))
    print('My body is ready!')
from discord.ext.commands import CommandNotFound

@bot.event
async def on_command_error(ctx, error):
    if isinstance (error, CommandNotFound):
        embed = discord.Embed (title=f"unknown command", description="mom pick me i'm scared",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.dark_gold ())
        embed.set_thumbnail (
            url="https://media.tenor.com/images/68f04cc74afa63bdb6756eb43ec0c2b3/tenor.gif")

        await ctx.send (embed=embed, delete_after=5.0)

        return
    raise error


bot.run(TOKEN)
