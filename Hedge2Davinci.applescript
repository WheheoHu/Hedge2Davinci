
-- SETTINGS
set pythonScript to "/Users/wheheohu/Code/Hedge2Davinci/Hedge2Davinci.py"
set sourceVolumePath to "/"
## if paths not set , pick file to continue
--
set FileCopyCompleted_destinationPath to ""


if pythonScript is "" then
    tell application "Finder"
        set pythonScript to entire contents of (choose file name with prompt "Choose python script location")
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
    set Counter to "{Counter}"
    set FileCopyCompleted_sourcePaths to "{FileCopyCompleted_sourcePaths}"
end if




if FileCopyCompleted_destinationPath  start with sourceVolumePath then
    display dialog do shell script "python3 "&pythonScript&" -vP "&FileCopyCompleted_destinationPath
else
    display dialog "Not Match \n"¬
            &sourceVolumePath&"\n"¬
            &FileCopyCompleted_destinationPath&"\n"
end if


on runningFromHedge(theEvent)
	if theEvent is "FileCopyCompleted" then
		if "{FileCopyCompleted_state}" is "Success" then
			return true
		else
			return false
		end if
	end if
end runningFromHedge