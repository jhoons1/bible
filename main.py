import pandas as pd
import bibleFunction as bf
import tistory as ts
import subprocess 

# book 이름과 chapter 리스트를 입력받음. 
request = {'book':'삿', 'chapter':['1','2','3']}

# 새번역본 성경 텍스트를 입력 받음.
bibleFile = "SaeBunYuk.txt"

# bibleFunction.py에 있는 bibleRead method로 string object 생성
data = bf.bibleRead(bibleFile)

# pandas Dataframe 생성
df = bf.getDataFrame(data)


# 생각보다 오래걸려서 dataframe 피클 시켜두고, 재사용시 dataframe 명령 주석처리 하고 pkl 사용 
df.to_pickle('./bible.pkl')

# pkl 읽기
df = pd.read_pickle('./bible.pkl')

# df에서 티스토리에 복붙할 html 코드 생성 
html = ts.getHTMLdoc(df, request)

print(html)

# 코드 돌리고 나면 macOS clip보드에 붙이려고 하는데 잘 안됨..
subprocess.run("pbcopy", universal_newlines=True, input=html)

