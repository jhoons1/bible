import pandas as pd
import bibleFunction as bf

# 성격판본, book 이름, chapter 리스트를 입력받음.
# version 선택지: 새번역, 개역개정, NIV

request = {	'version':['새번역'],}


# DataFrame 해당 버전 가져와서 csv로 저장하기
dfList = bf.getDataFrame(request)
for df in dfList:
	df.to_csv('./database/FinalBibleStandard1.csv', encoding = 'utf-8')
	df.to_csv('./database/FinalBibleStandard2.csv', encoding = 'cp949')
	df.to_csv('./database/FinalBibleStandard3.csv', encoding = 'euc-kr')
	df.to_csv('./database/FinalBibleStandard4.csv', encoding = 'utf-8-sig')