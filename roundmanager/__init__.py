from .ss13roundmanager import SS13RoundManager

def setup(bot):
    bot.add_cog(SS13RoundManager(bot))