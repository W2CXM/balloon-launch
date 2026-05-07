#!/usr/bin/python

import subprocess
import sys, time
from datetime import datetime

def create_sstv():
   subprocess.run(["rpicam-still", "--width", "320", "--height", "240", "-o", "latest_raw.jpg", "-n"])
   print("Image captured")

   subprocess.run([sys.executable, "telemetry.py"])
   subprocess.run(["pysstv", "--mode", "Robot36", "latest_pro.jpg", "sstv.wav"])
   print("SSTV file created")
   
   time.sleep(2)

# Main program
# Take initial picture
create_sstv()


while True:
    # Start sending the audio - call a separate script that opens the PTT and sends a wav file
    # Pass the wav file name as a parameter, so we can change the "filename" variable  after that process starts
    # process = subprocess.popen(["pysstv", "--mode", "robot36", "latest_pro.jpg", "sstv.wav"])

    process = subprocess.Popen([sys.executable, "serialout.py"])
    #The audio is now playing, let's create the next image in a new filename
    #filename = datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".wav"
    #take_picture_and_convert(filename)
    create_sstv()
    process.wait() # Now block until it the aplay finishes
    print("Picture done.  Sleeping a few secs.")
    # At this point, we have a new picture, and we finished playing the previous one
    # Sleep for a few seconds between transmissions
    time.sleep(2)
    # Lather, rinse, repeat
