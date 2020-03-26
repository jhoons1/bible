# 성경 통독 프로젝트

+ 성경 통독을 돕기 위한 html 생성 프로젝트입니다.

## Current version  
+ (Mar, 17th, 2020 기준): 
  * 가독성 향상! 
  * 성경 mdb 파일 받아서, pandas DataFrame으로 변환, 데이터 클리닝해서, 티스토리에 붙일 html 생성!  
  * [기존](https://jhoons.tistory.com/108)에 복붙으로 생성한 페이지가 넘 읽기 힘들어서,
  * 지금은 [이렇게](https://jhoons.tistory.com/117)까지 만들었습니다.
  * 아래 코드 블럭은 `main.py` 구조.
  
``` python
import pandas as pd
import bibleFunction as bf
import tistory as ts
import subprocess

# 성격판본, book 이름, chapter 리스트를 입력받음.
# version 선택지: 새번역, 개역개정, NIV

request = { 'version':['새번역','NIV'], 
            'book':'사무엘상', 
            'chapter':['4','5','6','7','8']}

# DataFrame 해당 버전 가져오기
dfList = bf.getDataFrame(request)

# df에서 티스토리에 복붙할 html 코드 생성
html = ts.getHTMLdoc(dfList, request)

print(html)

# 코드 돌리고 나면 macOS clip보드에 붙이기.
subprocess.run("pbcopy", universal_newlines=True, input=html)
```  
## Next version?
1. 구절별 like 기능도 넣을 수 있나?
2. 현재는 html블럭을 만들어서 tistory에 붙여넣고 있는데, github static webstie (=jekyll)로 바꿀 수 있나? 티스토리의 유튜브링크 기능, 이미지 게시 기능을 구현할 수 있으면 전용웹을 만드는 것도 좋을 것 같음. 
3. 월별 통독표를 가지고 자동으로 html 페이지를 생성해줄 수 있게?
4. 확 앱을 만들어 버려? Swift 프로젝트 고고싱!


