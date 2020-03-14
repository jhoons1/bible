import pandas as pd


# 27 tables
tblList = ['tbl_bible','tbl_bible2','tbl_bibleJoint','tbl_bibleModern',
    'tbl_bibleModernL','tbl_bibleNIV','tbl_bibleNKJV','tbl_bibleNRSV',
    'tbl_bibleStandard','tbl_findbible','tbl_findhymn','tbl_kbible',
    'tbl_kbibleEnglish','tbl_khymn','tbl_KindBible','tbl_songChildGospel',
    'tbl_songEnglishHymn','tbl_songGospel','tbl_songHymn','tbl_songPoetry',
    'tbl_songPraise2000','tbl_songPraiseBow','tbl_songPraiseJesus','tbl_versicle',
    'tbl_bibleKJV','tbl_bibleRevision','tbl_KindSong']

# read 'tblList[i]'+'.pkl' and check the contents

# tblIndex = 5
# tblName = tblList[tblIndex]
# tblFile = './'+tblName+'.pkl'
# df = pd.read_pickle(tblFile)
# print(df.iloc[10000]['구'])


for tblIndex in range(len(tblList)):
    tblName = tblList[tblIndex]
    tblFile = './'+tblName+'.pkl'
    df = pd.read_pickle(tblFile)

    try:
        print(tblName+':'+df.iloc[0]['구'])
        print(tblName+':'+df.iloc[1]['구'])
        print(tblName+':'+df.iloc[2]['구'])

        # print('새번역1: 태초에 하나님이 천지를 창조하셨다.')
        # print('새번역2: 땅이 혼돈하고 공허하며, 어둠이 깊음 위에 있고, 하나님의 영은 물 위에 움직이고 계셨다.')
        # print('새번역3: 하나님이 말씀하시기를 “빛이 생겨라” 하시니, 빛이 생겼다.')

        #print('개역개정:'+'태초에 하나님이 천지를 창조하시니라'+'\n'+'땅이 1)혼돈하고 공허하며 흑암이 깊음 위에 있고 하나님의 영은 수면 위에 운행하시니라'+'\n'+'하나님이 이르시되 빛이 있으라 하시니 빛이 있었고')

        print('NIV:'+'In the beginning God created the heavens and the earth.'+'\n'+'Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.'+'\n'+'And God said, "Let there be light," and there was light')


        print('\n')
    except:
        print(tblName+' error')

'''
결론:
+ tbl_bibleStandard : 새번역
+ tbl_bibleRevision : 개역개정
+ tbl_bibleNIV: NIV

'''