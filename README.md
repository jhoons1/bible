# 성경 통독 프로젝트

+ 성경 통독을 돕기 위한 html 생성 프로젝트입니다.

## 코드 구조 
+ (Mar, 8th, 2020 기준): 성경 txt 파일 받아서, 파싱해서, 티스토리에 붙일 html 생성 -> 가독성 향상!  
``` python
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
```  
## next version?
1. dataframe속의 book이름이 지금은 '사사기'를 '삿'처럼 한글자 혹은 '열왕기상'을 '왕상'처럼 두글자로 정리되어 있는데, 이를 풀네임으로 변경하기
2. 텍스트 파일 버전보다, 조금더 깔끔하게 정리된 데이터 베이스 찾아서 업데이트하기
3. 구절별 like 기능도 넣을 수 있나?
4. 현재는 html블럭을 만들어서 tistory에 붙여넣고 있는데, github static webstie (=jekyll)로 바꿀 수 있나? 티스토리의 유튜브링크 기능, 이미지 게시 기능을 구현할 수 있으면 전용웹을 만드는 것도 좋을 것 같음. 
5. 월별 통독표를 가지고 자동으로 html 페이지를 생성해줄 수 있게?
6. 확 앱을 만들어 버려? 
7. 다른 버전 성경 (특히 NIV)도 추가할 수 있나?






