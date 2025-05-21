import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def en_linea():
    print(f'Tu bot {bot.user.name} esta en linea!')
    
@bot.command()
async def kodland(ctx):
    
    await ctx.send('Hola, que te parece el curso de python pro?')
    

@bot.command()
async def saludar(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if 'hola' in mensaje:
        
        await ctx.send('Hola, ¿cómo estás?')
        
    elif 'klk' in mensaje:
        
        await ctx.send('Como te trata la vida?')
        
    else:
        
        await ctx.send('No entiendo lo que dices, pero te saludo de todas formas!')

@bot.command()
async def despedida(ctx):

    await ctx.send('Adios, que te vaya bien!')

@bot.command()
async def generar_contraseña(ctx, longitud: int):
    import random
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    await ctx.send(f'Tu contraseña generada es: {contraseña}')

@bot.command()
async def ayuda(ctx):
    mensaje = (
        "Hola, soy un bot de Discord. Aquí tienes algunos comandos que puedes usar:\n"
        "?kodland - Te saludo y te pregunto sobre el curso de python pro.\n"
        "?saludar <mensaje> - Te saludo dependiendo del mensaje que me envíes.\n"
        "?despedida - Te digo adiós.\n"
        "?generar_contraseña <longitud> - Genero una contraseña aleatoria de la longitud que me indiques.\n"
    )
    await ctx.send(mensaje)

token = ''
bot.run(token)
