# Final_Year_Project

This project is a program that creates highlight reels from sport videos.

--------------------------------------------------------------------------

The project is written using python and is feature driven. "Video skimming"
is used to create a reel from already existing clips. The video will be 
uploaded and then split into ten second clips. These clips will be examined 
for their volume level and brightness level. 

--------------------------------------------------------------------------

For finding the volume of a clip, the program will extract the audio from the
clip into a wav file, which will be analysed and have its values saved.

-------------------------------------------------------------------------

For finding the brightness of a clip, one frame will be taken for one second per
clip. These 10 frames from the ten second clip will be examined for brightness by 
converting them to a grey scale and finding the level of whiteness. The brightest
value will be returned and used to find a highlight.

--------------------------------------------------------------------------

The program will then use these values to pick out the best clips. These clips
will then be concatenated and displayed.

-------------------------------------------------------------------------- 

The project has a front-end created by FLASK that will allow a user to interact with it.
Two button are displayed, one that lets a user choose a video for submission and
another that will upload the video and then call the program to run and analyse
the video. 
