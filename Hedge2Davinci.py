
import argparse
from ast import parse
import importlib.machinery

import os
from pkgutil import ModuleInfo
des="help about Hedge to dacinvi script"
paser=argparse.ArgumentParser(description=des)

paser.add_argument('--volPath','-vP',default='/Users/wheheohu/Desktop/TestFiles',help="path to footage")
paser.add_argument('--tskName','-tN',default='Untitled',help="task name used to create bin in davinci resolve")
args=paser.parse_args()

print("path is "+args.volPath+"\ntask name (bin name) is "+args.tskName)

def load_dynamic(module,path):
    loader = importlib.machinery.ExtensionFileLoader(module,path)
    module=loader.load_module()
    return module

def bmd():
    pylib = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
    return load_dynamic('fusionscript',pylib)


footagePath=args.volPath
binName=os.path.basename(footagePath)

LOCALE_DAVINCI=bmd().scriptapp('Resolve','127.0.0.1')
Current_Project=LOCALE_DAVINCI.GetProjectManager().GetCurrentProject()
Project_Mediapool=Current_Project.GetMediaPool()  

print(Current_Project.GetName())

Project_Mediapool.AddSubFolder(Project_Mediapool.GetRootFolder(), binName)
timeline_clips=Project_Mediapool.ImportMedia(footagePath)
timeline=Project_Mediapool.CreateTimelineFromClips(binName, timeline_clips)      
