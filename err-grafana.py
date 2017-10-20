from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class grafana(BotPlugin):
    """
    Plugin that searches for and renders panels from Grafana server
    """

    @botcmd()
    def graf(self, msg, args)
    """queries grafana for dashboards and starts a flow"""
        pass
    
     @botcmd()
    def open(self, msg, args)
    """selects dashboard from list, and returns panels from selected dashboard"""
        pass
    
     @botcmd()
    def render(self, msg, args)
    """renders selected panel using bytesIO object"""
        pass
   
class BotCmdFail(Exception):
    """
    Custom Exception for failed interactions with bot
    """
