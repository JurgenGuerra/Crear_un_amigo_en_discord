from discord.ext import commands
from settings_files._global import *
import random

class Miscelánea(commands.Cog):
    def __init__(self, bot):
        self.bot=bot



    @commands.command(brief=": Respuestas aleatorias a una pregunta aleatoria",aliases=['8ball', 'luck', 'suerte'])# se define el alias de la función
                                            # _ is cause python doesnt allow start a function with a number
    async def Pregunta(self, ctx, *, question):
    #  question is something that this function needs
        responses = ['Como lo veo, si.',
                 'Preguntame de nuevo después.',
                 'Mejor no te lo digo ahora.',
                 'No puedo predecirlo ahora.',
                 'Concentrate y pregunta de nuevo.',
                 'No cuentes con ello.',
                 'No es seguro.',
                 'Eso es más que seguro.',
                 'Es lo más probable.',
                 'Mi respuesta es que no.',
                 'Mis fuentes me dicen que no.',
                 'En la generalidad creo que no.',
                 'Todo parece decir que si.',
                 'Trata de nuevo.',
                 'Los signos indican que si.',
                 'Muy dudoso que suceda.',
                 'Sin ninguna duda.',
                 'Si.',
                 'Si – definitivamente.',
                 'Puedes estar seguro de eso.'
                 ]
        await ctx.send(f'Pregunta: {question}\n Respuesta: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(Miscelánea(bot))

