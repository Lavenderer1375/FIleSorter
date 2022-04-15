import os
import glob


filesList = glob.glob("*")
extentionsSet = set()

for eachFile in filesList:
    try:
        extention = eachFile.split(".")[1]
        extentionsSet.add(extention)
    except:
        continue
    
    
def createsFolders():
    for eachExt in extentionsSet:
        if eachExt == "py":
            continue
        try:
            os.makedirs(eachExt + " Files")
        except:
            continue
        
        
def movesFiles():
    for eachFile in filesList:
        extention = eachFile.split(".")[1]
        os.rename(eachFile, extention + " Files/" + eachFile)

createsFolders()
movesFiles()