#Bot made for AvatarRP server that sadly shut down :(
#this version is old and not what final product looked like
#i will try to track final version soon
import sys
import discord
from discord.ext import commands
import traceback
from discord.ext.commands import CommandNotFound
import os

description = '''Cool bot made for AvatarRP server.'''
bot = commands.Bot(command_prefix='/', description=description)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="dynmap."))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed = discord.Embed(title="Command not found :flushed: ", description="Nothing to see here folks!")  # ,color=Hex code
        await ctx.send(embed=embed)
    raise error

@bot.command()
@commands.has_any_role("staff")
async def restart(ctx):
    print(f'Bot got restarted by {ctx.author}')
    await ctx.send("Bot will be restarting in few seconds!")
    user = bot.get_channel(734344710142951474)
    await user.send('Bot log:')
    await user.send(f"**Bot got restarted by {ctx.author}.**")
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.command()
@commands.has_any_role(734394752522387550)
async def newshelp(ctx):
    embed = discord.Embed(title="AvatarNews Help ", description="Command list:" ) #,color=Hex code
    embed.add_field(name=",newsn (text)", value="Sends text news.")
    embed.add_field(name=",newsp (link to image)", value="Sends image from provided link.")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/734114429649551371/734131237576376320/rsz_avatarrp-logo-white.png")
    embed.set_author(name="Dynmap",url="http://78.46.93.214:25104/")
    embed.set_footer(text=f"Developed by smartfridge#5834")
    await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role(734394752522387550)
async def newsn(ctx, *, arg):
    await ctx.send("News reported!")
    user = bot.get_channel(734395530695802880)
    embed = discord.Embed(title="AvatarNews :newspaper: ", description=arg ) #,color=Hex code
    embed.add_field(name="News reported by:", value=ctx.author)
    embed.set_footer(text=f"Developed by smartfridge#5834")
    await user.send(embed=embed)
    #await user.send(f"{arg}. Reported by {ctx.author}")

@bot.command()
@commands.has_any_role(734394752522387550)
async def newsp(ctx, *, arg):
    user = bot.get_channel(734395530695802880)
    embed = discord.Embed(title="AvatarNews :newspaper: ", description="Click on image for better quality."  ) #,color=Hex code
    embed.set_thumbnail(url=arg)
    embed.add_field(name="News reported by:", value=ctx.author)
    embed.set_footer(text=f"Developed by smartfridge#5834")
    await user.send(embed=embed)

@bot.event
async def on_error(event, ctx, *args, **kwargs):
    await ctx.send("It seems that you don't have permission for that command or you forgot to mention someone.")
    embed = discord.Embed(title=':x: Bot error!', colour=0xe74c3c) #Red
    embed.add_field(name='Event', value=event)
    embed.description = '```py\n%s\n```' % traceback.format_exc()
    user = bot.get_user(424639027606585356)
    await user.send(embed=embed)

@bot.group(pass_context=True)
async def nation(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Please use this command like /nation fire/water/air/earth')

@nation.command(pass_context=True)
async def water(ctx):
    await ctx.send('Added you to Water Nation list')
    f = open(f"wiki/Nations/{ctx.author}nation.txt", "w+")
    f.write(f"Water")
    f.close()

@nation.command(pass_context=True)
async def fire(ctx):
    await ctx.send('Added you to Fire Nation list')
    f = open(f"wiki/Nations/{ctx.author}nation.txt", "w+")
    f.write(f"Fire")
    f.close()

@nation.command(pass_context=True)
async def air(ctx):
    await ctx.send('Added you to Air Nation list')
    f = open(f"wiki/Nations/{ctx.author}nation.txt", "w+")
    f.write(f"Air")
    f.close()

@nation.command(pass_context=True)
async def earth(ctx):
    await ctx.send('Added you to Earth Nation list')
    f = open(f"wiki/Nations/{ctx.author}nation.txt", "w+")
    f.write(f"Earth")
    f.close()

@bot.group(pass_context=True)
async def minecraft(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Available sub-commands: link')

@minecraft.command(pass_context=True)
async def link(ctx, arg):
    await ctx.send('Linked your Minecraft account')
    f = open(f"wiki/Players/{arg}.txt", "w+")
    f.write(f"{ctx.author}\r\n")
    f.close()
    f = open(f"wiki/Players/{arg}id.txt", "w+")
    f.write(f"{ctx.author.id}\r\n")
    f.close()



bot.run('TOKEN')
