
import argparse

import os
from pybmd import Bmd

des = "help about Hedge to dacinvi script"
paser = argparse.ArgumentParser(description=des)

paser.add_argument('--volPath', '-vP', default=' ', help="path to footage")
paser.add_argument('--tskNa`me', '-tN', default='Untitled',
                   help="task name used to create bin in davinci resolve")
args = paser.parse_args()

print("Import Footages to Davinci....\npath is "+args.volPath)

footagePath = args.volPath
binName = os.path.basename(footagePath)

LOCAL_DAVINCI = Bmd() ##TODO change after api finished
current_project = LOCAL_DAVINCI.get_project_manager().get_current_project()
project_media_pool = current_project.get_media_pool()

print("\nProject Name:"+current_project.GetName())

project_media_pool.add_sub_folder(project_media_pool.get_root_folder().folder,binName)
time_clips=project_media_pool.import_media(footagePath)
timeline=project_media_pool.create_timeline_from_clips(binName,time_clips)
