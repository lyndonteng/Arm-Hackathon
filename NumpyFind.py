import numpy as np
def numpyFromDict(dictList):
    matches = ["x","y","z","Laser"]
    return[np.array(dict[list(dict)[0]]) for dict in dictList if list(dict)[0] in matches]