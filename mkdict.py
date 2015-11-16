def main(clus_):
	from gensim import corpora, models, similarities
	import csv
	import textedit
	import time
	pas="D:/Lresult/ks/hoge/"
	clus=str(clus_)

	print "mkcorpus_start",time.ctime()
	# remove common words and tokenize
	#stopfile=open("stopwords_en.csv","r")
	#stopdata=csv.reader(stopfile)
	#stoplist=[]
	#for line in stopdata:
	#	stoplist.append(line[0])
	#stopfile.close()
	#print stoplist

	##make documents
	for clus in range(0,10):
		clus=str(clus)
		dlist=[]
		dfile=open("D:/Lresult/ks/hoge/V6csWcyvwOg_E2ni3V_CgA.csv","r")
		#dfile=open("testrev.csv")
		ddata=csv.reader(dfile)
		ddata.next()
		dnum=0
		for line in ddata:
			if(line[7]==clus):
						te=line[5]
						doc=textedit.textedit(te)
						dlist.append(doc)
		dfile.close()
		print "dfile fin",time.ctime()

		texts = [[word for word in document.lower().split()] for document in dlist]
		print "text fin",time.ctime()
		# remove words that appear only once
		#all_tokens = sum(texts, [])
		#tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
		#texts = [[word for word in text if word not in tokens_once] for text in texts]

		#print(texts)
		#print("texts fin")

		dictionary = corpora.Dictionary(texts)
		print "dictionary fin",time.ctime(),len(dictionary.token2id)
		#dictionary.filter_extremes(no_below=10,no_above=0.5)
		#print "dictionary cut fin",time.ctime(),len(dictionary.token2id)

		#dictionary.save("clus"+clus+".dict")
		dictionary.save_as_text(pas+"clus"+clus+"_text.dict")

	#corpus=[dictionary.doc2bow(text) for text in texts]
	#corpora.MmCorpus.serialize(pas+"nNVreview.mm", corpus)
	#print corpus
	#print "mk_corpus fin",time.ctime()


if __name__ == '__main__':
	print "clus"
	clus_=raw_input()
	main(clus_)
