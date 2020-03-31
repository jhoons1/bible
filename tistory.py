import pandas as pd

def getHTMLdoc(dfList, req):


    dfChapsList = []

    for dfInd, df in enumerate(dfList):

        dfBook = df[ df['book'] == req['book'] ]

        dfChaps = dfBook[ dfBook['chapter'].isin(req['chapter']) ]

        dfChapsList += [dfChaps]

    finalHTMLtxt = ''

    finalHTMLtxt += getTitle(req)


    #header
    finalHTMLtxt += getImage(req)
    finalHTMLtxt += getYoutubeVD(req)
    finalHTMLtxt += getYoutbePL(req)


    lenChaps = [ item.shape[0] for item in dfChapsList ]
    maxlen = max(lenChaps)

    for index in range(maxlen):
        for dfInd, dfChaps in enumerate(dfChapsList):
            finalHTMLtxt += generateHtmlLine(dfChaps.iloc[index])

    #footer


    return finalHTMLtxt


def getTitle(req):
    title = req['Title']
    prefix = req['book']+req['chapter'][0]+'-'+req['chapter'][-1]+': '
    line = '<p>'+prefix+title+'</p>'
    return line

def getImage(req):
    image = req['image']
    line = ''
    if image == '사무엘':
        line += '<p>[##_Image|kage@ckDtw8/btqCWLsKT4G/vK8qIM5wiIKLmeYjvRlU40/img.jpg|alignCenter|data-filename="11-12-Samuel-FNL.jpg" data-origin-width="5950" data-origin-height="3850"|바이블 프로젝트 사무엘서 포스터||_##]</p>' 
    return line

def getYoutubeVD(req):
    videos = req['youtubeVD']
    line = ''
    for video in videos:
        if video != '':
            line += '<p>&nbsp;</p><figure data-ke-type="video" data-ke-style="alignCenter" data-video-host="youtube" data-video-url="https://www.youtube.com/watch?v='+video+'" data-video-thumbnail="https://scrap.kakaocdn.net/dn/lDSO6/hyFqPKXn2c/CSj3wGUD4NUk1dgSn0CGMK/img.jpg?width=480&amp;height=360&amp;face=0_0_480_360" data-video-width="480" data-video-height="360"><iframe src='+'"https://www.youtube.com/embed/'+video+'"'+' width="480" height="360" frameborder="0" allowfullscreen="true"></iframe><figcaption>바이블 프로젝트 영상</figcaption></figure>'
    return line

def getYoutbePL(req):
    playlist = req['youtubePL']
    line = ''
    if playlist != '':
        line =  '<p><iframe width="50%" height="50" src="' +\
                'https://www.youtube.com/embed/videoseries?list='+\
                playlist+\
                '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"></iframe></p>'
    return line

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

