#!/usr/bin/env python

# Hopefully this can be fired by Errbot in Rocket Chat, but would also work from the CLI
# imports
import time
import datetime
import soco
from soco.discovery import by_name

def roundTime(dt=None, roundTo=900):
   """Round a datetime object to any time lapse in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

def morningReminder():
    # Find and (if needed) group together the downstairs speakers


    # Determine what time it is and how long it will be until the next multiple of 5.
    print(roundTime(dt=None, roundTo=900))



    # Wait that long and then
    count = 0
    while True:

        # Setup the Queue and get ready to play
        

        count = count + 1

        # Add a dire warning to the queue
        if count == 12:
            break
        
        # Play the appropriate mp3 for that time
        if count >= 14:
            break

        # Wait 5 minutes and then loop around and play the next appropriate time.
        print(count)
        time.sleep()

if __name__=="__main__":
    morningReminder()