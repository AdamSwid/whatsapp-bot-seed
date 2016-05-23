from utils.media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity


class SuperViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("^/help", self.help),
        ]

    def help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(HELP_TEXT, to=message.getFrom())


HELP_TEXT = """ [HELP]
Commands:
/help - You just used it
/trihard - I'm a bot after all (Saul)
/niggroMode - For when you need a black friend
/poll [que]? [ans1] [ans2] ... - Creates a poll
/endpoll - Guess
/Overwatch - Are you Hyped? I am
/countdown - I told you I'm hyped
"""

