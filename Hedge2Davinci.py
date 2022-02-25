
import argparse

import os
from pybmd.bmd import Bmd

des = "help about Hedge to dacinvi script"
paser = argparse.ArgumentParser(description=des)

paser.add_argument('--volPath', '-vP', default=' ', help="path to footage")
paser.add_argument('--tskNa`me', '-tN', default='Untitled',
                   help="task name used to create bin in davinci resolve")
args = paser.parse_args()

print("Import Footages to Davinci....\npath is "+args.volPath)

footagePath = args.volPath
binName = os.path.basename(footagePath)

LOCAL_DAVINCI = Bmd.get_local_davinci() ##TODO change after api finished
Current_Project = LOCAL_DAVINCI.GetProjectManager().GetCurrentProject()
Project_Mediapool = Current_Project.GetMediaPool()

print("\nProject Name:"+Current_Project.GetName())

# Project_Mediapool.AddSubFolder(Project_Mediapool.GetRootFolder(), binName)
# timeline_clips = Project_Mediapool.ImportMedia(footagePath)
# timeline = Project_Mediapool.CreateTimelineFromClips(binName, timeline_clips)
