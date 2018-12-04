# Final_Year_Project

This project is a program that creates highlight reels from sport videos.

--------------------------------------------------------------------------

The project is written using python and is feature driven. "Video skimming"
is used to create a reel from already existing clips. The video will be 
uploaded and then split into ten second clips. These clips will be examined 
for their volume level and brightness level. This will be mostly preformed
in the SplitFile file though it will use Split to get frames and use FindBrightness
and FindVolume to analyse the features

--------------------------------------------------------------------------

For finding the volume of a clip, the program will extract the audio from the
clip into a wav file, which will be analysed and have its values saved. This will
be done using the FindVolume file. It will return an array containg the max volume 
from each clip

-------------------------------------------------------------------------

For finding the brightness of a clip, one frame will be taken for one second per
clip. These 10 frames from the ten second clip will be examined for brightness by 
converting them to a grey scale and finding the level of whiteness. The brightest
value will be returned and used to find a highlight. This will be done using the
FindBrightness file.

--------------------------------------------------------------------------

The program will then use these values to pick out the best clips. These clips
will then be concatenated and displayed. This will be done using the Rejoin file.

-------------------------------------------------------------------------- 

The project has a front-end created by FLASK that will allow a user to interact with it.
Two button are displayed, one that lets a user choose a video for submission and
another that will upload the video and then call the program to run and analyse
the video. This is done using the Application file. 

--------------------------------------------------------------------------

The project front-end design is made by the HTML files home and upload. Both files
use a tempate file so that code is not repeated over and over. The code will
create two buttons so that a file may be uploaded and processed.
