# TVHAT1982
A Python script to change TV HAT stream channels on a Raspberry Pi using VLC playlists and a button


This script sets up a Raspberry Pi to change TV channels being streamed from another Raspberry Pi on the same network running TVheadend and a Raspberry Pi TV HAT. 

Prerequisites
-------------

A second Raspberry Pi on the network running TVheadend (https://tvheadend.org/)
A folder named "channels" containing M3U playlists named to match the references in channelswitch.py, in the /home/pi/ folder.
An installation of VLC. A "standard" installation works OK for SD channels (SD Default can be set in TVheadend)). For better performance a hardware-accelerated version of VLC can (theoretically) be compiled.

Setup
-----

Save the channelswitch.py file to your /home/pi/folder

Create the "channels" folder in /home/pi/ and store in it the playlists for your selected channels. The script here is only looking for four playlists, named in sequence channel1.M3U, channel2.M3U, channel3.M3U, channel4.M3U. These playlists are created by clicking on the "i" next to a channel in TVheadend and downloading the .M3U file. The playlist file is per-channel but will contain the name of the programme playing when you downloaded it - this can be edited in a text editor to be something more meaningful, eg "BBC 1". 

Either run the script manually from the terminal...

  python channelswitch.py

... or set it to run on startup by editing...

  nano ~/.config/lxsession/LXDE-pi/autostart

...and entering the below at the bottom of the list of processes:

  @python /home/pi/channelswitch.py &

It doesn't need to have sudo at the front, in fact this will cause problems with VLC.

You'll also need a button connected to the GPIO - this script uses GPIO26 and a rotary switch, you can use whatever kind of button you like and change the GPIO pin to suit. 

After all of the above the Pi should display the channel1.M3U playlist after the first button press, and then work through the sequence 1-4 for subsequent presses. If more channels are needed you can just add more playlists and change the IF i > 4 part of the script to reflect the total number. 

It's a simple script but fun, check out my Pi Projects on 

Instructables at https://www.instructables.com/member/MisterM/instructables/ , subscribe to the 
Old Tech. New Spec. YouTube channel at https://www.youtube.com/channel/UCRrwSKYBu4N7P6HWZsWJ2MA ,join in on 
Twitter @OldTechNewSpec. 
Website: http://kyliemander.com/blog/


