import pandas as pd

def getDataFrame(request):

    tblNames = {'새번역':'FinalBibleStandard','개역개정':'FinalBibleRevision','NIV':'FinalBibleNIVSorted'}

    dfList = []
    for version in request['version']:
	    pklName = tblNames[version]
	    fileName = './database/'+pklName+'.pkl'
	    df = pd.read_pickle(fileName)
	    df['version'] = tblNames[version]
	    dfList += [df]

    return dfList


    