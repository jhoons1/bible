import pandas as pd

def getHTMLdoc(dfList, req):


    dfChapsList = []

    for dfInd, df in enumerate(dfList):

        dfBook = df[ df['book'] == req['book'] ]

        dfChaps = dfBook[ dfBook['chapter'].isin(req['chapter']) ]

        dfChapsList += [dfChaps]

    finalHTMLtxt = ''

    lenChaps = [ item.shape[0] for item in dfChapsList ]
    maxlen = max(lenChaps)

    for index in range(maxlen):
        for dfInd, dfChaps in enumerate(dfChapsList):
            finalHTMLtxt += generateHtmlLine(dfChaps.iloc[index])

    return finalHTMLtxt


def generateHtmlLine(line):

    #verseRow = 
    #{'book': book,'chapter':chapter,'verse':verseNum,
    # 'verseTitle':verseTitle,'sentence':sentence,
    # 'comments':comments,'comLocs':comLocs}

    #verseRow = 
    # [ 'index', 'book', 'chapter', 'verseTitle', 'verse', 'sentence', 'etc', 'key']

    version = line.version

    book = line.book
    chapter = line.chapter
    verseTitle = line.verseTitle
    verse = line.verse
    sentence = line.sentence
    etc = line.etc
    key = line.key

    HtmlLine =  ''
    
    if verse == '1' and version == 'FinalBibleStandard':
        lineHTML = '<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style6" />'
        chapterHTML = '<p><span><h4 data-ke-size="size20"><b>' + book + '&nbsp;' + chapter +'장'+ '</b></h4></span>' + '<p>&nbsp;</p>'
        HtmlLine += lineHTML + chapterHTML


    if verseTitle != '' and version == 'FinalBibleStandard':
        verseTitleHTML = '<p><span><b>' + verseTitle + '</b></span></p>' + '<p>&nbsp;</p>'
        HtmlLine += verseTitleHTML


    if sentence != '' and version == 'FinalBibleStandard':
        sentenceHTML = '<p><span>' +  chapter +':' + verse + '&nbsp;' + sentence + '</span></p>'
        HtmlLine += sentenceHTML

    if sentence != '' and version == 'FinalBibleNIVSorted':
        sentenceHTML = '<p><span style="color: #7e98b1;">' + '<i>( ' + sentence + ')</i>' + '</span></p>' + '<p>&nbsp;</p>'
        HtmlLine += sentenceHTML


    return HtmlLine

