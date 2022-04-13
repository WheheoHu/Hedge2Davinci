
import argparse

import os
from pybmd import Bmd

def import_to_resolve(footage_path:str,bin_name:str):
    LOCAL_DAVINCI = Bmd() # create a new BMD object
    current_project = LOCAL_DAVINCI.get_project_manager().get_current_project()
    project_media_pool = current_project.get_media_pool()

    project_media_pool.add_sub_folder(project_media_pool.get_root_folder().folder,bin_name)
    time_clips=project_media_pool.import_media(footage_path)
    timeline=project_media_pool.create_timeline_from_clips(bin_name,time_clips)


if __name__ == "__main__":
    des = "help about Hedge to dacinvi script"
    paser = argparse.ArgumentParser(description=des)

    paser.add_argument('--volPath', '-vP', default=' ', required=True,help="path to footage")
    paser.add_argument('--tskName', '-tN', default='Untitled',
                       help="task name used to create bin in davinci resolve")
    args = paser.parse_args()

    print("Import Footages to Davinci....\npath is "+args.volPath)

    footagePath = args.volPath
    binName = os.path.basename(footagePath)

    import_to_resolve(footagePath,binName)