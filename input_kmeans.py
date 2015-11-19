
def main(model_,topic,cluster):
	import numpy
	import csv
	from sklearn.cluster import KMeans
	import collections
	import os
	import numpy
	import gensim
	import textedit
	import time

	pas="D:/Lresult"
	model=model_
	tnum=int(topic)
	cnum=int(cluster)

	####prepare model
	lmodel=gensim.models.LdaModel.load(pas+"/model/"+model+"model/NVreview_o4b6t"+str(tnum)+"."+model)
	dictionary=gensim.corpora.Dictionary.load(pas+"/model/dict/NVreview_o4b6.dict")

	##load stoplist
	stoplist=collections.Counter()
	stopfile=open("D:/Lresult/stopwords/over4word.csv","r")
	stopdata=csv.reader(stopfile)
	for line in stopdata:
		stoplist[line[0]]=1
	stopfile.close()
	stopfile=open("D:/Lresult/stopwords/b6list.csv","r")
	stopdata=csv.reader(stopfile)
	for line in stopdata:
		stoplist[line[0]]=1
	stopfile.close()
	stopset=set(stoplist)
	print "stop fin",len(stoplist),time.ctime()

	#ifile=open(pas+"/ks/bussent/_L1SVry9jDzk6VLz75Z6Ow.csv","r")
	busname="4bEjOyTaDG24SY5TxsaUNQ"
	ifile=open("//kaede/PPTShare/masafumi/musc/20151117/ks/bussent/"+busname+".csv","r")
	idata=csv.reader(ifile)
	idata.next()
	revlist=collections.Counter()###review cluster
	revvec=collections.Counter()###review vector
	revlen=collections.Counter()###length of review vector
	n=0
	for line in idata:
		doc=textedit.textedit(line[5])
		doc=doc.lower().split()
		docset=set(doc)-stopset###remove stopwords
		vec_bow = dictionary.doc2bow(docset)
		vec_lmodel = lmodel[vec_bow]
		rlen=0
		revlist[line[0],line[6]]=[0]*tnum
		for num in range(0,len(vec_lmodel)):
			rlen=rlen+vec_lmodel[num][1]*vec_lmodel[num][1]
			revlist[line[0],line[6]][vec_lmodel[num][0]]=vec_lmodel[num][1]
		rlen=numpy.sqrt(rlen)
		if(rlen!=0):
			revlist[line[0],line[6]]=revlist[line[0],line[6]]/rlen
		#print revlist[line[0],line[6]]
	ifile.close()

	##k-means
	kdata=numpy.array(revlist.values())
	kmeans_model=KMeans(n_clusters=cnum,random_state=1).fit(kdata)
	labels=kmeans_model.labels_

	wfile=open(pas+"/ks/busclus/"+busname+".csv","wb")
	writer=csv.writer(wfile)
	writer.writerow(["revid","sent","clus"])
	for num in range(0,len(revlist)):
		writer.writerow(list(revlist.keys()[num])+[labels[num]])
	wfile.close()
	print "fin",time.ctime()

if __name__ == '__main__':
	print "lmodel","topic_num","cluster_num"
	main("lda",500,10)
