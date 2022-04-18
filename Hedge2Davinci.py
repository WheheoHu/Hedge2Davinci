
import argparse
from datetime import datetime

import os
import re
from pybmd import Bmd

def import_to_resolve(footage_path:str,task_name:str,bin_name:str,reel_counter:int, daycount:int,data:datetime):
    
    
    
    LOCAL_DAVINCI = Bmd() # create a new BMD object
    current_project = LOCAL_DAVINCI.get_project_manager().get_current_project()
    project_media_pool = current_project.get_media_pool()

    
    #Add bin
    card_name=re.findall(r'CAM_([A-Z])',task_name)[0]+"%03d" % reel_counter
    camera_name=re.findall(r"(CAM_[A-Z])",task_name)[0]
    day_folder=project_media_pool.add_sub_folder(project_media_pool.get_root_folder().folder,"Day%02d"%daycount+f"_{data.strftime('%Y%m%d')}")
    project_media_pool.add_sub_folder(project_media_pool.add_sub_folder(day_folder.folder,camera_name).folder,card_name)
    
    
    time_clips=project_media_pool.import_media(footage_path)
    timeline=project_media_pool.create_timeline_from_clips(card_name,time_clips)


if __name__ == "__main__":
    des = "help about Hedge to dacinvi script"
    paser = argparse.ArgumentParser(description=des)

    paser.add_argument('--volPath', '-vP', default=' ', required=True,help="path to footage")
    paser.add_argument('--tskName', '-tN', default='Untitled',
                       help="task name used to create bin in davinci resolve")
    paser.add_argument('--dayCount','-dC',type=int,help="day count")
    paser.add_argument('--reelCounter','-rC',type=int,help="reel counter")
    paser.add_argument('--date','-d',help="date")
    args = paser.parse_args()

    print("Import Footages to Davinci....\npath is "+args.volPath)

    footagePath = args.volPath
    binName = os.path.basename(footagePath)
    reelCounter = args.reelCounter
    tskName=args.tskName
    dayCount = args.dayCount
    date=datetime.strptime(args.date,'%Y-%m-%d')
    print(f"footage path is {footagePath},bin name is {binName},task name is {tskName},day count is {dayCount},date is {date}")
    import_to_resolve(footage_path=footagePath,task_name=tskName,bin_name=binName,daycount=dayCount,data=date,reel_counter=reelCounter)