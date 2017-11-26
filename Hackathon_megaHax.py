#import csv
import tempfile
import subprocess
import pandas as pd


def openLocation(filepath):
    "Opens file in explorer at specified path"
    subprocess.Popen(r'explorer /select,{}'.format(filepath))
    

def getDictList(valSet):
    """headers,vals,vals...vals10
    Input:
        valSet: string containing sets of values to be parsed
    Output:
        dictList: list of dictionaries key:[values]
    """

    a = valSet.split(",")
    b = [singarray.strip().split(" ") for singarray in a]
    headers = ["Temperature","Humidity","x","y","z","AirQuality"] #"Laser"
    dictList = [{header: b[index]} for index, header in enumerate(headers)]
    return dictList

def writeDictList(dictList,filename = "myCsv", filepath = ""):
    """Converts a list of dictionaries to panda, then exports to csv
       Input:
        dictList: string in format "  val1 val2 val3 , val4 val5 val6  "
                values stored in equal length lists
        [filename]: optional, DO NOT INCLUDE FILETYPE, default "myCsv"
        [filepath]: optional, path to csv save location, %temp% used by default
       Output:
        Full path to file
    """
    dataFrame = pd.concat(list(map(pd.DataFrame, dictList)), axis=1)
    if filepath == "":
        filepath = tempfile.gettempdir()
    filepath+="\{}.csv".format(filename)
    dataFrame.to_csv(filepath)  
    return filepath