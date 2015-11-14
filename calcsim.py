def main(model_,bnum_,tnum_,train_,pas_):
	from gensim import corpora, models, similarities
	import csv
	import textedit
	import time
	model=str(model_)
	bnum=int(bnum_)
	tnum=int(tnum_)
	train=str(train_)
	pas=str(pas_)

	print "start",time.ctime()

	#dictionary = corpora.Dictionary.load(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".dict")
    #corpus = corpora.MmCorpus(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".mm")
	dictionary = corpora.Dictionary.load(pas+"model/nNVreviewpl.dict")

	#use LSI
	#lsi = models.LsiModel.load(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".lsi")
	#if(model=="lda"):
	#	lsi=models.LdaModel.load(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".lda")
	lsi = models.LsiModel.load(pas+"model/nNVreview500.lsi")

	#calc topic sim
	header=[]
	header.append("rev_id")
	header.append("bus_id")
	header.append("stars")
	header.append("sentnum")
	header.append("date")
	for num in range(0,int(tnum)):
		header.append("t"+str(num).zfill(len(str(tnum))/10))

	#wfile=open(pas+train+model+"_o4b"+str(bnum)+"t"+str(tnum)+".csv","wb")
	wfile=open(pas+"model/hoge.csv","wb")
	writer=csv.writer(wfile)
	writer.writerow(header)

	"NVreview.csv:[review_id,user_id,business_id,stars,date,texts]"
	#test file
	ifile=open(pas+"ks/NVrevrawsent.csv","r")
	idata=csv.reader(ifile)
	idata.next()
	k=0
	for line in idata:
		wlist=[]
		wlist.append(line[0])
		wlist.append(line[2])
		wlist.append(line[3])
		wlist.append(line[6])###for revraw only
		wlist.append(line[4])

		doc=textedit.textedit(line[5])
		vec_bow = dictionary.doc2bow(doc.lower().split())
		vec_lsi = lsi[vec_bow]
		slist=[0]*int(tnum)
		for num in range(0,len(vec_lsi)):
			slist[vec_lsi[num][0]]=vec_lsi[num][1]
		wlist=wlist+slist
		writer.writerow(wlist)
	        k=k+1
		if(k%1000==900):
			print k,time.ctime()
			break
	ifile.close()
	wfile.close()
	print "fin",time.ctime()

if __name__ == '__main__':
	print "model"
	model_="lsi"
	print "bnum"
	bnum_=6
	print "tnum"
	tnum_=500
	print "train"
	train_="nNVreview"
	print "pas"
	pas_="D:/Lresult/"
	main(model_,bnum_,tnum_,train_,pas_)
