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
- Script create **bin name** in Davinci Resolve By the folder name. eg.clips in `/XX/A001/`,the bin name in Davinci will be set to `A001`,It works better when use Hedge to manage offload folder correctly


