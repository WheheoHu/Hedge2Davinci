
-- SETTINGS
set pythonScript to "/Users/wheheohu/Code/Hedge2Davinci/Hedge2Davinci.py"
set sourceVolumePath to "/"
## if paths not set , pick file to continue
--
set FileCopyCompleted_destinationPath to ""


if pythonScript is "" then
    tell application "Finder"
        set pythonScript to entire contents of (choose file with prompt "Choose python script location")
    end tell
end if
if sourceVolumePath is "" then
    tell application "Finder"
        set VolumePath to  choose folder with prompt "Choose Davinci Source Volume Path" 
        set sourceVolumePath to POSIX path of VolumePath as string
    end tell
end if

    
if runningFromHedge("FileCopyCompleted") then
    set FileCopyCompleted_destinationPath to "{FileCopyCompleted_destinationPath}"
    set FileCopyCompleted_sourceInfo to "{FileCopyCompleted_sourceInfo}"
    set FileCopyCompleted_sourcePaths to "{FileCopyCompleted_sourcePaths}"
    set FileCopyCompleted_presetName to "{FileCopyCompleted_presetName}"
end if

tell application "JSON Helper"
    set json to read JSON from FileCopyCompleted_sourceInfo
end tell

    set Counter to |Counter| of json
    set Date to |Date| of json
    set Daycount to |Daycount| of json

if FileCopyCompleted_destinationPath  start with sourceVolumePath then
    display dialog (do shell script "python3 "&pythonScript&" -vP "&FileCopyCompleted_destinationPath) with title "Davinci Go"
else
    display dialog "No Match Path \n"¬
            &"Source Volume is: "&sourceVolumePath&"\n"¬
            &"Footage Path is: "&FileCopyCompleted_destinationPath&"\n" with title "No Match Path"
end if
