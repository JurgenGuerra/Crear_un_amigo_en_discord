from discord.ext import commands
from settings_files._global import *

class ComandosBasicos(commands.Cog):
    def __init__(self, bot):
        self.bot=bot



    @commands.command(brief=": Genera una invitación para ingresar a este servidor.")
    async def invitar(self, ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)

def setup(bot):
    bot.add_cog(ComandosBasicos(bot))

