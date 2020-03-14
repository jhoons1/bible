
# test 파일 버전 사용때 쓰던 코드. 이제 필요 없음. Mar. 11. 2020

import pandas as pd


def bibleRead(bibleFile):

    with open(bibleFile,'r', encoding='cp949') as file:
        dataTXT = file.read()
        data = dataTXT.split('\n')

    return data



def getDataFrame(data):

    

    df = pd.DataFrame()

    prevCh = 0

    # limit = 1000
    # chCount = 0

    for verse in data:

        if (len(verse)!=0):

            verseRow = verseParser(verse)

            df = df.append(verseRow,ignore_index=True)

            if verseRow['chapter'] != prevCh:
                print(verseRow['book']+':'+verseRow['chapter'])
                prevCh = verseRow['chapter']

            # chCount += 1

        # if (chCount > limit):
        #     break


    return df


def verseParser(verse):


    bookChapterVerse = verse.split(' ')[0]
    bookChapter = bookChapterVerse.split(':')[0]
    verseNum = bookChapterVerse.split(':')[1]

    nums = ['1','2','3','4','5','6','7','8','9']

   
    if bookChapter[1] in nums:
        book = bookChapter[0]
        chapter = bookChapter[1:]


    elif bookChapter[2] in nums:
        book =  bookChapter[:2]
        chapter = bookChapter[2:]

    sentLoc = verse.find(' ')+1
    
    sentTitleComm = verse[sentLoc:]

    verseTitle, sentence, comments, comLocs, comList = parseSentence(sentTitleComm)
    verseRow = {'book': book,'chapter':chapter,'verse':verseNum,'verseTitle':verseTitle,'sentence':sentence,'comments':comments,'comLocs':comLocs, 'comList': comList, }

    return verseRow




def parseSentence(sentTitleComm):


    isTitle = 0
    isComm = 0
    comLocs = []
    comList = []

    comms = ['a)','b)','c)','d)','e)','f)','g)','h)','i)','j)','k)','l)','m)']

    #check title

    t1Loc = sentTitleComm.find('<')
    t2Loc = sentTitleComm.find('>')

    verseTitle = ''
    sentComm = ''
    if (t1Loc != -1) and (t2Loc != -1):
        isTitle = 1
        verseTitle =  sentTitleComm[t1Loc+1:t2Loc]
        sentComm = sentTitleComm[:t1Loc]+sentTitleComm[t2Loc+1:]
    else:
        sentComm = sentTitleComm

    #check comms and comment location

    for com in comms:
        if com in sentComm:
            isComm = 1
            comLocs += [sentComm.find(com)]
            comList += [com]

    #check parethesis of comments

    if isComm == 1:
        loc =sentComm.rfind('. (')
        sentence = sentComm[:loc]+'.'
        comments = sentComm[loc+1:]
    else:
        sentence = sentComm
        comments = ''

    return (verseTitle, sentence, comments, comLocs, comList)


        











































