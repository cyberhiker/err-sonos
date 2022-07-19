from errbot import BotPlugin, botcmd
import soco
from soco import SoCo
import sys

class ErrSonos(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd
    def list(self, msg, args):

        for zone in soco.discover():
            prettyDevices += zone.player_name + "\n"

        return prettyDevices


    @botcmd(split_args_with=' ')  # flags a command
    def play(self, msg, args):  # a command callable with !

        player_name = args[0]

        if player_name is not None:
            from soco.discovery import by_name
            sonos = by_name(player_name)

            sonos.play()
            track = sonos.get_current_track_info()

            return('Playing *' + track['title'] + '* by ' + track['artist'])

        else:
            return 'No Player Name Specified'


    @botcmd(split_args_with=' ')  # flags a command
    def pause(self, msg, args):  # a command callable with !

        player_name = args[0]

        if player_name is not None:
            from soco.discovery import by_name
            sonos = by_name(player_name)
            sonos.pause()

            return 'Paused'

        else:
            return 'No Player Name Specified'


    @botcmd(split_args_with=' ')  # flags a command
    def volume(self, msg, args):  # a command callable with !

        direction = args[0]

        if direction is not None:
            sonos = soco(ip_address)

            if direction == 'up':
                sonos.volume += 10

                return 'Adjusted Down'

            elif direction == 'down':
                sonos.volume -= 10

                return 'Adjusted Down'

        else:
            return 'No IP Specified'

"""
        elif sys.argv[1] == 'next':
            sonos.next()
        elif sys.argv[1] == 'previous':
            sonos.previous()

        else:
            print('Ran')
"""
