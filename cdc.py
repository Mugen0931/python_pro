import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event 
async def on_ready():
    print(f'La maquina {bot.user.name} está en línea!')

@bot.command()
async def saludo(ctx):
    await ctx.send('Holaaa, como estas? yo bien, quieres algun dato de la contaminacion? si quieres saber como funciono, intenta escribiendo !ayuda')

@bot.command()
async def dato(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if 'ambiental' in mensaje:
        
        await ctx.send('La contaminacion ambiental es un problema serio, como se provoca? ya sea por el uso de combustibles fosiles, o por la industria que emite gases contaminantes. Como se puede resolver? se puede resolver reduciendo el uso de combustibles fosiles y dejar de quemar basura y tambien reducir el uso de fabricas.')
        
    elif 'suelo' in mensaje:
        
        await ctx.send('La contaminacion del suelo tambien es otro problema serio, como se provoca? por la basura que se tira al suelo. Como se puede resolver? se puede resolver con el reciclaje de plasticos, y seguridad para la basura en sitios publicos.')

    elif 'agua' in mensaje:

        await ctx.send('La contaminacion del agua es un problema serio, como se provoca? ya sea tirando basura al mar, o por el uso de petroleo, o por el uso de productos quimicos que se filtran al agua. Como se puede resolver? se puede resolver con el reciclaje de plasticos, y seguridad para la basura en sitios publicos.')
        
    else:
        
        await ctx.send('que?')

@bot.command()
async def despedida(ctx):
    await ctx.send('Adios, que te vaya bien! vuelve pronto! :(')


@bot.command()
async def ayuda(ctx):
    mensaje = (
        "Hola, soy un bot de Discord. Aquí tienes algunos comandos que puedes usar:\n"
        "!Hola - Te saludo y te pregunto sobre la contaminacion.\n"
        "!dato <mensaje> - Te doy un dato sobre la contaminacion dependiendo del mensaje que me envíes, de agua, ambiental o del suelo.\n"
        "!ayuda - Te muestro este mensaje de ayuda. :)\n"
        "!Despedida - Te digo adiós... :(\n"
    )
    await ctx.send(mensaje)



token = ''
bot.run(token)
