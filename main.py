import pandas as pd
import bibleFunction as bf
import tistory as ts
import subprocess

# 성격판본, book 이름, chapter 리스트를 입력받음.
# version 선택지: 새번역, 개역개정, NIV

request = {	'version':['새번역','NIV'], 
			'book':'사무엘상', 
			'chapter':['4','5','6','7','8']}

# DataFrame 해당 버전 가져오기
dfList = bf.getDataFrame(request)

# df에서 티스토리에 복붙할 html 코드 생성
html = ts.getHTMLdoc(dfList, request)

print(html)

# 코드 돌리고 나면 macOS clip보드에 붙이려고 하는데 잘 안됨..
subprocess.run("pbcopy", universal_newlines=True, input=html)

