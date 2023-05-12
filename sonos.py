from errbot import BotPlugin, botcmd
import soco
import argparse
from soco import SoCo
import sys
import morningReminders

class ErrSonos(BotPlugin):
    """
    Limited controlling of your Sonos speakers.
    """

    @botcmd
    def sonos_list(self, msg, args):
        """
        List available players 
        """

        prettyDevices = ''

        for device in soco.discover():

            state = device.get_current_transport_info()['current_transport_state']
            track = device.get_current_track_info()

            if state == 'PLAYING':
                prettyDevices += device.player_name + ' - Playing *' + track['title'] + '* by ' + track['artist'] + '\n'
            else:
                prettyDevices += device.player_name + ' - ' + state.title() + '\n'

        return prettyDevices


    @botcmd(split_args_with=' ')  # flags a command
    def sonos_play(self, msg, args):  # a command callable with !
        """
        Play [player name] from list command, use " " around spaced players.
        """

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
    def sonos_pause(self, msg, args):  # a command callable with !
        """
        Pause [player name] from list command, use " " around spaced players.
        """

        player_name = args[0]

        if player_name is not None:
            from soco.discovery import by_name
            sonos = by_name(player_name)
            sonos.pause()

            return 'Paused'

        else:
            return 'No Player Name Specified'


    @botcmd(split_args_with=' ')  # flags a command
    def sonos_volume(self, msg, args):  # a command callable with !
        """
        Increment Volume [player name] [up/down]
        """

        player_name = args[0]
        direction = args[1]

        if player_name is not None:
            from soco.discovery import by_name
            sonos = by_name(player_name)

            if direction == 'up':
                sonos.volume += 5

                return 'Adjusted Up'

            elif direction == 'down':
                sonos.volume -= 5

                return 'Adjusted Down'

        else:
            return 'No IP Specified'

    @botcmd(split_args_with=' ')  # flags a command
    def morning(self, msg, args):  # a command callable with !
        """
        Run morning routine on [player name] from list command, use " " around spaced players.
        """

        player_name = args[0]

        if player_name is not None:
            from soco.discovery import by_name
            device = by_name(player_name)

            print("Player name: " + player_name)
            morningReminders.morningReminder()

            track = device.get_current_track_info()
            return('Playing *' + track['title'] + '*')

        else:
            return 'No Player Name Specified'

"""
	Coming Some Day
        elif sys.argv[1] == 'next':
            sonos.next()
        elif sys.argv[1] == 'previous':
            sonos.previous()
"""
