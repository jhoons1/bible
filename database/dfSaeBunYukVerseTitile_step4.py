import pandas as pd 

x = pd.read_pickle('bible.pkl')
y1 = pd.read_pickle('Finaltbl_bibleStandard.pkl')
y2 = pd.read_pickle('Finaltbl_bibleRevision.pkl')
y3 = pd.read_pickle('Finaltbl_bibleNIV.pkl')

shortBookList = ['창','출','레','민','신','수','삿','룻','삼상','삼하','왕상','왕하','대상','대하','스','느','에',
                '욥','시','잠','전','아','사','렘','애','겔','단','호','욜','암','옵','욘','미','나','합',
                '습','학','슥','말','마','막','눅','요','행','롬','고전','고후','갈','엡','빌','골','살전',
                '살후','딤전','딤후','딛','몬','히','약','벧전','벧후','요일','요이','요삼','유','계']

shortBookDict = {}

for index_1 in range(len(shortBookList)):
    index = str(index_1+1)
    shortBookDict[shortBookList[index_1]] = index

x['book']= x['book'].replace(shortBookDict)

xTitle = x[ x['verseTitle']!='' ]

y1['verseTitle']=''
y2['verseTitle']=''
y3['verseTitle']=''

numError1 = 0
numError2 = 0

yList = [y1,y2,y3]
yTitle = ['./FinalBibleStandard.pkl','./FinalBibleRevision.pkl','./FinalBibleNIV.pkl']

for yInd, y in enumerate(yList):
    for ind, row in xTitle.iterrows():
        title = row.verseTitle 
        book = row.book
        chapter = row.chapter
        verse = row.verse
        try:
            dfFilter = (y['index']==book) & (y['chapter']==chapter) & (y['verse']==verse)
            y.loc[dfFilter, ['verseTitle']] = title
        except:
            numError2 += 1

    #print('Error1 occurred '+str(numError1)+' times')
    #print('Error2 occurred '+str(numError2)+' times')

    y = y[['index', 'book', 'chapter', 'verseTitle', 'verse', 'sentence', 'etc', 'key']]
    y = y.to_pickle(yTitle[yInd])









