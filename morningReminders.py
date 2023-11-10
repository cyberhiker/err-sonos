#!/usr/bin/env python3

from time import sleep
import datetime
import soco
from soco.discovery import by_name
from plexapi.server import PlexServer
from soco import SoCo
from soco.snapshot import Snapshot
from soco.plugins.plex import PlexPlugin

def roundTime(dt=None, date_delta=datetime.timedelta(minutes=5), to='up'):
    """
    Round a datetime object to a multiple of a timedelta
    dt : datetime.datetime object, default now.
    dateDelta : timedelta object, we round to a multiple of this, default 1 minute.
    from:  http://stackoverflow.com/questions/3463930/how-to-round-the-minute-of-a-datetime-object-python
    """
    round_to = date_delta.total_seconds()
    if dt is None:
        dt = datetime.datetime.now()
    seconds = (dt - dt.min).seconds

    if seconds % round_to == 0 and dt.microsecond == 0:
        rounding = (seconds + round_to / 2) // round_to * round_to
    else:
        if to == 'up':
            # // is a floor division, not a comment on following line (like in javascript):
            rounding = (seconds + dt.microsecond/1000000 + round_to) // round_to * round_to
        elif to == 'down':
            rounding = seconds // round_to * round_to
        else:
            rounding = (seconds + round_to / 2) // round_to * round_to

    return dt + datetime.timedelta(0, rounding - seconds, - dt.microsecond)

def morningReminder(speakerName="Family Room"):
    # Connect to Plex
    baseurl = 'http://192.168.0.150:32400'
    token = 'oNixAbW1SQ2fxb1pdSkH'
    server = PlexServer(baseurl, token)
    album = server.library.section('Music').get('Alarm Sounds').album('Clock Sounds')

    # Find and (if needed) group together the downstairs speakers
    device = by_name(speakerName)
    try:
        print(device.group.coordinator)
        s = device.group.coordinator
    finally:
        s = device.group.coordinator

    output = "Reminders will play on:\n"

    for player in s.group:
        output = player.player_name + "\n"    

    plugin = PlexPlugin(s)

    # Determine what time it is and how long it will be until the next multiple of 5.
    roundUpTime = roundTime()
    theseSeconds = roundUpTime - datetime.datetime.now()

    # Lower the Bass and Raise the Volume
    output = output + "Time reminders will start in " + str(round(theseSeconds.total_seconds(), 0)) + " seconds."
    print(output)
    
    # Wait that long and then
    sleep(theseSeconds.total_seconds())

    count = 0
    while True:
        # Setup the Queue and get ready to play
        # take snapshot of current state
        snap = Snapshot(s)  # 1) create a Snapshot class for this device
        snap.snapshot()  # 2) take a snapshot of this device's status

        # Clear what's there to play this.
        s.clear_queue()
        count = count + 1
        
        for sound in album:
            if sound.title == datetime.datetime.now().strftime('%-I%M'):
                device.group.volume = 65
                
                output = "Playing " + datetime.datetime.now().strftime('%-I:%M')
                print(output)
                
                # Play the appropriate mp3 for that time
                plugin.play_now(sound)

                # Wait for the Alert to Finish
                sleep(10)

                # Restore previous state of Sonos (with slow fade up)
                print("reinstating how it was before....")
                snap.restore(fade=True)

        # Stop after an hour and a quarter
        if count >= 12:
            output = "Routine Completed at " + datetime.datetime.now().strftime('%-I:%M')
            print(output)
            break

        # Wait 5 minutes and then loop around and play the next appropriate time.
        sleep(290)

    # End
    return output

if __name__=="__main__":
    print(morningReminder())
