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
async def kodland(ctx):
    await ctx.send('Hola, quieres algun dato de la contaminacion?, eligen entre ambiental, suelo o agua.')

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




token = ''
bot.run(token)