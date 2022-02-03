# Hedge to Dacinvi

Hedge script to import footage in hedge offload task to Davinci Resolve and create Timeline 

## REQUEST
- Work on Mac **Only**
- Python 3.6


## How to Use
1. Open `Hedge2Davinci.scpt` in Script Editor 
2. edit `pythonScript`: path to the `Hedge2Davinci.py`
3. edit `sourceVolumePath`:  **Root** path to the volume that davinci resolve import clips
4. Save and Close the file 
5. In Hedge, go to `Preference->Scripting` ,At `File Copy Completed` Event,choose `Hedge2Davinci.scpt` 

## ATTENTION
- DaVinci Resolve needs to be **running** for a script to be invoked. 
- You should go into the project you want to add clips in Davinci Resolve


