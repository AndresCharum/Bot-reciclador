import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Diccionario que contiene información sobre los objetos y su impacto en el medio ambiente
recycling_info = {
    'plastico': {'recyclable': True, 'impacto': 'Malo'},
    'vidrio': {'recyclable': True, 'impacto': 'bueno'},
    'papel': {'recyclable': True, 'impacto': 'bueno'},
    'cartón': {'recyclable': True, 'impacto': 'bueno'},
    'metal': {'recyclable': True, 'impacto': 'bueno'},
    'bateria': {'recyclable': True, 'impacto': 'Malo'},
    'pilas': {'recyclable': True, 'impacto': 'Malo'},
    'electronicos': {'recyclable': True, 'impacto': 'Malo'},
    'organico': {'recyclable': False, 'impacto': 'bueno'},
    'basura': {'recyclable': False, 'impacto': 'Malo'},
    # Agrega más objetos y su información aquí
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def recicla(ctx, objeto: str):
    objeto = objeto.lower()
    if objeto in recycling_info:
        if recycling_info[objeto]['recyclable']:
            respuesta = f'¡Sí! El {objeto} es reciclable.'
        else:
            respuesta = f'Lo siento, el {objeto} no es reciclable.'
        if recycling_info[objeto]['impacto'] == 'bueno':
            respuesta += f' Además, es bueno para el medio ambiente.'
        else:
            respuesta += f' Sin embargo, es malo para el medio ambiente.'
    else:
        respuesta = f'Lo siento, no tengo información sobre el {objeto}.'
    await ctx.send(respuesta)

bot.run("MTI0NTE1NTQ3NzQyODUwMjUyOA.GkL5Pk.FQdOn5pkTxGBRZ_QWlVuaIxmh2Kg6-76nftuSc")
