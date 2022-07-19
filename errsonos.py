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

        devices = {device.player_name: device for device in soco.discover()}

        return devices


    @botcmd(split_args_with=' ')  # flags a command
    def play(self, msg, args):  # a command callable with !

        ip_address = args[0]

        if ip_address is not None:
            sonos = soco(ip_address)

            sonos.play()
            track = sonos.get_current_track_info()

            return('Playing ' + track['title'] + ' by ' + track['artist'])

        else:
            return 'No IP Specified'


    @botcmd(split_args_with=' ')  # flags a command
    def pause(self, msg, args):  # a command callable with !

        ip_address = args[0]

        if ip_address is not None:
            sonos = soco(ip_address)
            sonos.pause()

            return 'Paused'

        else:
            return 'No IP Specified'


    @botcmd(split_args_with=' ')  # flags a command
    def volume(self, msg, args):  # a command callable with !

        direction = args[0]

        if direction is not None:
            sonos = soco(ip_address)

            if direction == 'up':
                sonos.volume += 10

            elif direction == 'down':
                sonos.volume -= 10

                return 'Adjusted Down'

        else:
            return 'No IP Specified'

"""
        if sys.argv[1] == 'play':
            sonos.play()
        elif sys.argv[1] == 'pause':
            sonos.pause()
        elif sys.argv[1] == 'next':
            sonos.next()
        elif sys.argv[1] == 'previous':
            sonos.previous()
        elif sys.argv[1] == 'vol_up':
            sonos.volume += 10
        elif sys.argv[1] == 'vol_down':
            sonos.volume -= 10
        else:
            print('Ran')

        track = sonos.get_current_track_info()
        print(track['title'])
"""
