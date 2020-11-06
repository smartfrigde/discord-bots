# TwiliBot/FoxBot was created only for educational puproses. This code is messy and most things are unfinished
import datetime
import random
import string
import urllib
import urllib.request
import requests
import discord
import praw
from discord import Embed
from discord.ext import commands
from mcstatus import MinecraftServer

reddit = praw.Reddit (client_id="TOKEN",
                      client_secret="TOKEN",
                      user_agent="TOKEN")

bot = commands.Bot (command_prefix=',', description="FoxBot is the most salties bot you ever seen!")
bot.remove_command("help")


@bot.event
async def on_ready():
        await bot.change_presence (
            activity=discord.Streaming (name="update 1.3.1 buh! ,help", url="http://www.twitch.tv/24/7-hosting-is-gay"))
        print ('My body is ready')

# alternative help command that replaces original
@bot.command (pass_context=True, brief="New help command!", description='New help command!')
async def help(ctx):
   author = ctx.author
   embed = discord.Embed (title=f",help", description="List of available commands:!",
                          timestamp=datetime.datetime.utcnow (), color=discord.Color.purple())
   embed.add_field (name=",vibecheck", value=f"VibeChecks people")
   embed.add_field (name=",egg", value=f"EggChecks people")
   embed.add_field (name=",pp", value=f"shows pp size (100% real)")
   embed.add_field (name=",oneball [question]", value=f"you ask questions and it replies buh")
   embed.add_field (name=",payrespect", value=f"normie memes are here too")
   embed.add_field (name=",meme", value=f"Sends random meme")
   embed.add_field (name=",dankmeme", value=f"Sends random dank meme")
   embed.add_field (name=",food", value=f"Sends random food picture")
   embed.add_field (name=",pewdiepie", value=f"Sends random pewdiepie submission")
   embed.add_field (name=",youngyt", value=f"Sends random young ppl on yt submission buh")
   embed.add_field (name=",thatsdeep", value=f"Sends random im 14 thats deep submission")
   embed.add_field (name=",gif", value=f"Sends random gif")
   embed.add_field (name=",cursed", value=f"(nsfw channel required)Sends random cursed image")
   embed.add_field (name=",swag", value=f"swag command buh!")
   embed.add_field (name=",allah", value=f"this was requested buh!")
   embed.add_field (name=",alembic", value=f"this was also requested bruh")
   embed.add_field (name=",question", value=f"sends random questions (spamming this command can be considered as spam on servers)")
   embed.add_field (name=",sc", value=f"sends random screenshot from someone device")
   embed.add_field (name=",say", value=f"simple say command")
   embed.add_field (name=",emc", value=f"checks earthmc.net status")
   embed.add_field (name=",hypixel", value=f"checks hypixel status")
   embed.add_field (name=",sum", value=f"sums 2 provided numbers")
   embed.add_field (name=",ban", value=f"ban command yo!")
   embed.add_field (name=",kick", value=f"kick command yo!")
   embed.add_field (name=",info", value=f"shows info about server")
   embed.add_field (name=",ping", value=f"pong")
   # embed.set_thumbnail(url=f"{ctx.guild.icon}")
   embed.set_thumbnail (url="https://www.meme-arsenal.com/memes/67e08d6a1a2722aca68e9fa62c0fec55.jpg")

   await ctx.author.send(author, embed=embed)
   await ctx.send('command list was send to command author buh')






# ping command used to check is bot responding
@bot.command (pass_context=True, brief="Pong!", description='Pong! (used to see how fast bot responds).')
async def ping(ctx):
    await ctx.send ('Pong!')




# simple + commmand
@bot.command (brief="Sums numbers. Usage : ,sum 20 10 ", description='Sums numbers.')
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send (numOne + numTwo)


# server info command
@bot.command (brief="Shows info of server", description='Shows info about server.')
async def info(ctx):
    embed = discord.Embed (title=f"{ctx.guild.name}", description="Here's info about this server!",
                           timestamp=datetime.datetime.utcnow (), color=discord.Color.blue ())
    embed.add_field (name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field (name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field (name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field (name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail (url="https://cdn.pixabay.com/photo/2013/07/12/14/15/info-148099_960_720.png")

    await ctx.send (embed=embed)


# Events



# when bot crashes this happens\/
@bot.event
async def on_error(ctx=None):
    await bot.change_presence (
        activity=discord.Streaming (name="oof i crashed", url="http://www.twitch.tv/smartfrigde0"))
    print ('oh shiet i crashed!')
    await ctx.send ('umm i think i crashed :eyes: ')
    await bot.start ()


# not so simple vibecheck command that uses random.py library
@bot.command (pass_context=True, brief="Performs Vibe Check", description='Performs VibeCheck on pinged-person/you .')
async def vibecheck(ctx):
    a = random.random ()
    b = random.random ()
    if b > a:
        print ("vcheck-pass")
        embed = discord.Embed (title=f"Vibe Check passed!",
                               description="you can call yourself lucky <:pog:707182319739338773> ",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.green ())
        embed.set_thumbnail (
            url="https://pbs.twimg.com/media/EKF7aaJXkAMNpR8.jpg")
        await ctx.send (embed=embed)
    else:
        print ("vcheck-fail")
        embed = discord.Embed (title=f"Vibe Check failed! ", description="that's kinda gay :eyes:",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.red ())
        embed.set_thumbnail (
            url="https://media.discordapp.net/attachments/691541565994434560/718393233750622258/vibecheckfailed.gif")
        await ctx.send (embed=embed)


# f command
@bot.command (brief="F command", description='F command')
async def payrespect(ctx):
    await ctx.send (file=discord.File ('f.jpg'))
    await ctx.send ('**Press F to pay respects!**')


# swag command
@bot.command (brief="This command is swag buh.", description='swag commmand bruh')
async def swag(ctx):
    embed = discord.Embed (title=f"Swag!",
                           timestamp=datetime.datetime.utcnow (), color=discord.Color.blue ())
    embed.set_thumbnail (
        url="https://media.discordapp.net/attachments/679671608838848546/719335965369565265/putinwalk2.gif")

    await ctx.send (embed=embed)


# downloads to do list from website using urllib module
@bot.command (brief="Sends to-do list to command author.", description='Sends to-do list to command author.')
async def todo(ctx):
    await ctx.send ('To Do list was send to command author <:heheboi:719173324466290698>')
    for line in urllib.request.urlopen ("https://twilipl.neocities.org/twilibot/todo.txt"):
        await ctx.author.send (line.decode ('utf-8'))


# displays earthmc.net status using dinnerboone module
@bot.command (brief="Displays EarthMC.net status.", description='Displays EarthMC.net status.')
async def emc(ctx):
    # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
    server = MinecraftServer.lookup ("play.earthmc.net:25565")

    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status ()
    queue = format (status.players.online - 150)
    # await ctx.send("The server has {0} players and replied in {1} ms, queue is {3} long.".format(status.players.online), status.latency, queue)
    embed = discord.Embed (title=f"EarthMC.net", description="**Queue and player count**",
                           timestamp=datetime.datetime.utcnow (), color=discord.Color.green ())
    embed.add_field (name="Total players:", value=f"{format (status.players.online)}")
    embed.add_field (name="Latency:", value=f"{status.latency}")
    embed.add_field (name="Queue:", value=f"{queue}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail (
        url="https://github.com/EarthMC/EarthMC.net/blob/master/src/img/android-chrome-512x512.png?raw=true")

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


from discord.ext.commands import CommandNotFound


@bot.event
async def on_command_error(ctx, error):
    if isinstance (error, CommandNotFound):
        embed = discord.Embed (title=f"unknown command", description="mom pick me i'm scared",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.dark_gold ())
        embed.set_thumbnail (
            url="https://media.tenor.com/images/68f04cc74afa63bdb6756eb43ec0c2b3/tenor.gif")

        await ctx.send (embed=embed)

        return
    raise error


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


# allah command for c08_
@bot.command (brief="this was requested buh", description='allah commmand bruh')
async def allah(ctx):
    embed = discord.Embed (title=f"allah buh", description=" :pray: :kaaba: :mosque: ",
                           timestamp=datetime.datetime.utcnow (), color=discord.Color.gold ())
    embed.set_thumbnail (url="https://twilipl.neocities.org/twilibot/images/allahmeme.jpg")

    await ctx.send (embed=embed)


# reddit r/dankmemes
@bot.command (pass_context=True, brief="Sends random reddit dankmeme.", description='Sends random reddit dankmeme.')
async def dankmeme(ctx):
    memes_submissions = reddit.subreddit ('dankmemes').hot ()
    post_to_pick = random.randint (1, 100)
    for i in range (0, post_to_pick):
        submission = next (x for x in memes_submissions if not x.stickied)

    await ctx.send (submission.url)


# displays hypixel status using dinnerboone module
@bot.command (brief="Displays hypixel status.", description='Displays hypixel status.')
async def hypixel(ctx):
    # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
    server = MinecraftServer.lookup ("proxy.hypixel.net:25565")

    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status ()
    queue = format (status.players.online - 85000)
    # await ctx.send("The server has {0} players and replied in {1} ms, queue is {3} long.".format(status.players.online), status.latency, queue)
    embed = discord.Embed (title=f"Hypixel", description="**Queue and player count**",
                           timestamp=datetime.datetime.utcnow (), color=discord.Color.green ())
    embed.add_field (name="Total players:", value=f"{format (status.players.online)}")
    embed.add_field (name="Latency:", value=f"{status.latency}")
    embed.add_field (name="Queue:", value=f"{queue}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail (
        url="https://user-images.githubusercontent.com/49322497/70186527-61601080-16ec-11ea-8e0e-49c0f5e4edde.png")

    await ctx.send (embed=embed)


# reddit r/memes
@bot.command (pass_context=True, brief="Sends random reddit meme.", description='Sends random reddit meme.')
async def meme(ctx):
    memes_submissions = reddit.subreddit ('memes').hot ()
    post_to_pick = random.randint (1, 100)
    for i in range (0, post_to_pick):
        submission = next (x for x in memes_submissions if not x.stickied)

    await ctx.send (submission.url)


# reddit r/food
@bot.command (pass_context=True, brief="Sends random reddit food image.", description='Sends random reddit food image.')
async def food(ctx):
    memes_submissions = reddit.subreddit ('food').hot ()
    post_to_pick = random.randint (1, 100)
    for i in range (0, post_to_pick):
        submission = next (x for x in memes_submissions if not x.stickied)

    await ctx.send (submission.url)


# reddit r/gifs
@bot.command (pass_context=True, brief="Sends random reddit gif.", description='Sends random reddit gif.')
async def gif(ctx):
    memes_submissions = reddit.subreddit ('gifs').hot ()
    post_to_pick = random.randint (1, 100)
    for i in range (0, post_to_pick):
        submission = next (x for x in memes_submissions if not x.stickied)

    await ctx.send (submission.url)


# reddit r/ama comments
@bot.command (pass_context=True, brief="Sends random questions.", description='Sends random questions.')
async def question(ctx):
    submission = reddit.subreddit ('ama').random ()
    submission.comments.replace_more (limit=1)
    for top_level_comment in submission.comments:
        await ctx.send (top_level_comment.body)


# simple say command
@bot.command (pass_context=True, brief="Simple say command.",
              description='Nothing to see here folks,just simple say command.')
async def say(ctx, *args):
    mesg = ' '.join (args)
    await ctx.send (mesg)


# shows pp size
@bot.command (brief="shows pp size", description='shows pp size')
async def pp(ctx):
    global value
    value = (random.choice ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 69, 420, 99]))
    await ctx.send ("**Your pp has {0} cm**".format (value), )


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


# alembic command for urakuk
@bot.command (brief="this was requested buh", description='alembic commmand bruh')
async def alembic(ctx):
    embed = discord.Embed (title=f" :alembic: alembic buh :alembic: ",
                           description=" :pray: :alembic: :alembic: :pray: ",
                           timestamp=datetime.datetime.utcnow (), color=discord.Color.blue ())
    embed.set_thumbnail (
        url="https://steamuserimages-a.akamaihd.net/ugc/361780126225179483/EAEA04804866066181EC2E6BBF72031C73283D1F/")

    await ctx.send (embed=embed)

# not so simple egg that uses random.py library
@bot.command (pass_context=True, brief="Performs oneball", description='Performs oneball .')
async def oneball(ctx, *args):
    a = random.random ()
    b = random.random ()
    no = ['No', 'Thats gay', 'ummm no', 'are you stupid?', 'maybe']
    yes = ['im not sure', 'yes', 'one day', 'buh', 'i wanna die seing those questions']
    answeryes = random.choice (yes)
    answerno = random.choice (no)
    if b > a:
        embed = discord.Embed (title='heres my answer',
                               description="lemme check",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.greyple ())
        embed.add_field (name="my dump answer:", value=f"{answerno}")
        embed.set_thumbnail (
            url="https://media1.giphy.com/media/d6DgWX8JepXeuftjjl/giphy.gif")
        await ctx.send (embed=embed)
    else:
        embed = discord.Embed (title='heres my answer buh', description="lemme check this",
                               timestamp=datetime.datetime.utcnow (), color=discord.Color.red ())
        embed.add_field (name="my proffesional answer:", value=f"{answeryes}")
        embed.set_thumbnail (
            url="https://media1.giphy.com/media/d6DgWX8JepXeuftjjl/giphy.gif")
        await ctx.send (embed=embed)

# fake ban command
@bot.command (pass_context=True, brief="bans pinged person", description='bans pinged person')
async def ban(ctx):
    await ctx.send ('alexa! he thinks we implemented gay commands')

# fake kick command
@bot.command (pass_context=True, brief="kicks pinged person", description='kicks pinged person')
async def kick(ctx):
    await ctx.send ('alexa! he thinks we implemented gay commands')


# reddit r/crappydesign
@bot.command (pass_context=True, brief="Sends random reddit crappy design post.", description='Sends random reddit crappy design post.')
async def crappydesign(ctx):
    memes_submissions = reddit.subreddit ('CrappyDesign').hot ()
    post_to_pick = random.randint (1, 100)
    for i in range (0, post_to_pick):
        submission = next (x for x in memes_submissions if not x.stickied)

    await ctx.send (submission.url)

# reddit r/cursedimages nsfw
@bot.command (pass_context=True, brief="(18+)Sends random cursed image", description='(18+)Sends random cursed image.')
async def cursed(ctx):
    if ctx.channel.is_nsfw ():
        return ctx.send ("buh this command is nsfw. use it in nsfw channel only")
        memes_submissions = reddit.subreddit ('cursedimages').hot ()
        post_to_pick = random.randint (1, 100)
        for i in range (0, post_to_pick):
            submission = next (x for x in memes_submissions if not x.stickied)

        await ctx.send (submission.url)
    else:
     await ctx.send ("buh this command is nsfw. use it in nsfw channel only")


# reddit r/youngpeopleyoutube
@bot.command (pass_context=True, brief="Sends random r/youngpeopleyoutube submission.", description='Sends random r/youngpeopleyoutube  submission.')
async def youngyt(ctx):
    memes_submissions = reddit.subreddit ('youngpeopleyoutube').hot ()
    post_to_pick = random.randint (1, 100)
    for i in range (0, post_to_pick):
        submission = next (x for x in memes_submissions if not x.stickied)

    await ctx.send (submission.url)

# reddit r/pewdiepiesubmissions
@bot.command (pass_context=True, brief="Sends random r/pewdiepiesubmissions submission.", description='Sends random r/pewdiepiesubmissions  submission.')
async def pewdiepie(ctx):
    memes_submissions = reddit.subreddit ('pewdiepiesubmissions').hot ()
    post_to_pick = random.randint (1, 100)
    for i in range (0, post_to_pick):
        submission = next (x for x in memes_submissions if not x.stickied)

    await ctx.send (submission.url)

# reddit r/im14andthisisdeep
@bot.command (pass_context=True, brief="Sends random r/im14andthisisdeepsubmission.", description='Sends random r/im14andthisisdeep  submission.')
async def thatsdeep(ctx):
    memes_submissions = reddit.subreddit ('im14andthisisdeep').hot ()
    post_to_pick = random.randint (1, 100)
    for i in range (0, post_to_pick):
        submission = next (x for x in memes_submissions if not x.stickied)

    await ctx.send (submission.url)


# shows how gay
@bot.command (brief="shows how gay you are", description='shows how gay you are')
async def howgay(ctx):
    global gay
    gay = (random.choice ([0, 25, 50, 75, 100]))
    await ctx.send ("**You are {0}% gay.**".format (gay), )



bot.run ('TOKEN')
