import pandas as pd

def getHTMLdoc(df, req):


	dfBook = df[ df['book'] == req['book'] ]

	dfChaps = dfBook[ dfBook['chapter'].isin(req['chapter']) ]

	finalHTMLtxt = ''

	for index, line in dfChaps.iterrows():
		finalHTMLtxt += generateHtmlLine(line) 

	return finalHTMLtxt


def generateHtmlLine(line):

	#verseRow = 
	#{'book': book,'chapter':chapter,'verse':verseNum,
	# 'verseTitle':verseTitle,'sentence':sentence,
	# 'comments':comments,'comLocs':comLocs}

	book = line.book
	chapter = line.chapter
	verse = line.verse
	verseTitle = line.verseTitle
	sentence = line.sentence
	comments = line.comments
	comLocs = line.comLocs
	comList = line.comList

	HtmlLine =  ''
	
	if verse == '1':
		chapterHTML = '<p><span><h4 data-ke-size="size20"><b>' + '사사기' + '&nbsp;' + chapter +'장'+ '</b></h4></span>' + '<p>&nbsp;</p>'
		HtmlLine += chapterHTML


	if verseTitle != '':
		verseTitleHTML = '<p><span><b>' + verseTitle + '</b></span></p>' + '<p>&nbsp;</p>'
		HtmlLine += verseTitleHTML


	newSentence = sentence
	if comList != []:
		for com in comList: 
			newSentence = ' '.join(newSentence.split(com))
		sentence = newSentence

	if sentence != '':
		sentenceHTML = '<p><span>' + verse + '&nbsp;' + sentence + '</span></p>' + '<p>&nbsp;</p>'
		HtmlLine += sentenceHTML


	return HtmlLine

















