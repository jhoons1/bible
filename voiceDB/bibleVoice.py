import os
import sys
import pandas as pd
#os.system('ls')


def fetchBookVoice(bookInd):
	
	# Find book titles
	bookDB = '../database/FinalBibleStandard.pkl'
	df = pd.read_pickle(bookDB)
	books = []
	#df.info()
	for ind in bookInd:
	 	books += df.loc[df["index"]==ind]["book"].unique().tolist()
	#print(books)

	# Find last chapters in each book
	last = '1'
	for book in books:
		print(book)
		chapters = df.loc[df["book"]==book]['chapter'].unique().tolist()
		for chap in chapters:
			if int(last) <= int(chap):
				last = chap  
		#print(last)

	# Generate mpsyt command
	loc = "~/Downloads/mps/"
	prog = "mpsyt "
	prefix = "/드라마 바이블 "
	postfix = "장"
	endfix = ","
	line = ''
  
	last='1'

	for book in books:
		for chap in range(int(last)):
			chap = str(chap+1)
			line += prog 
			#Search
			line += prefix+book+' '+chap+postfix+endfix

			#Download
			line +='d 1,2'

			#m4a option and exit
			#line +=' q'

			#Execute
			print(line)
			#os.system(line)

			#Rename
			file = os.listdir(loc)
			print(file)







def main(bookInd):

	#Fetch m4a for books in 'books' list
	
	fetchBookVoice(bookInd)



if __name__ == '__main__':
	
	bookInd = ['9']
	
	main(bookInd)