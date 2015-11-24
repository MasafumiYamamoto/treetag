
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
	lmodel=gensim.models.LsiModel.load(pas+"/model/"+model+"model/NVreview_o4b6t"+str(tnum)+"."+model)
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
	#ifile=open("//kaede/PPTShare/masafumi/musc/20151117/ks/topicmodeling/"+busname+".csv","r")
	ifile=open(pas+"/ks/busent_anv/"+busname+".csv","r")
	idata=csv.reader(ifile)
	revlist_p=collections.Counter()###review cluster positive
	revlist_n=collections.Counter()###review cluster negative
	revvec=collections.Counter()###review vector
	revlen=collections.Counter()###length of review vector
	n=0
	for line in idata:
		if(int(line[3])>3):###use only positive review
			doc=line[5].lower().split()####review data
			docset=set(doc)-stopset###remove stopwords
			vec_bow = dictionary.doc2bow(docset)
			vec_lmodel = lmodel[vec_bow]
			rlen=0
			revlist_p[line[0],line[6]]=[0]*tnum
			for num in range(0,len(vec_lmodel)):
				rlen=rlen+vec_lmodel[num][1]*vec_lmodel[num][1]
				revlist_p[line[0],line[6]][vec_lmodel[num][0]]=vec_lmodel[num][1]
			rlen=numpy.sqrt(rlen)
			if(rlen!=0):
				revlist_p[line[0],line[6]]=revlist_p[line[0],line[6]]/rlen
		elif(int(line[3])<3):
			doc=line[5].lower().split()####review data
			docset=set(doc)-stopset###remove stopwords
			vec_bow = dictionary.doc2bow(docset)
			vec_lmodel = lmodel[vec_bow]
			rlen=0
			revlist_n[line[0],line[6]]=[0]*tnum
			for num in range(0,len(vec_lmodel)):
				rlen=rlen+vec_lmodel[num][1]*vec_lmodel[num][1]
				revlist_n[line[0],line[6]][vec_lmodel[num][0]]=vec_lmodel[num][1]
			rlen=numpy.sqrt(rlen)
			if(rlen!=0):
				revlist_n[line[0],line[6]]=revlist_n[line[0],line[6]]/rlen
	ifile.close()
	print "input fin",len(revlist_p),len(revlist_n),time.ctime()

	##k-means
	kdata_p=numpy.array(revlist_p.values())
	kmeans_model_p=KMeans(n_clusters=cnum,random_state=1).fit(kdata_p)
	labels_p=kmeans_model_p.labels_
	kdata_n=numpy.array(revlist_n.values())
	kmeans_model_n=KMeans(n_clusters=cnum,random_state=1).fit(kdata_n)
	labels_n=kmeans_model_n.labels_

	print "k-means fin",time.ctime()
	wfile=open(pas+"/ks/busclus/"+busname+"_clus.csv","wb")
	writer=csv.writer(wfile)
	writer.writerow(["revid","sent","clus"])
	tmp=revlist_p.keys()
	for num in range(0,len(tmp)):
		writer.writerow(list(tmp[num])+[labels_p[num]+1])
	tmp=revlist_n.keys()
	for num in range(0,len(tmp)):
		writer.writerow(list(tmp[num])+[-1*labels_n[num]-1])
	wfile.close()
	print "fin",time.ctime()

if __name__ == '__main__':
	print "lmodel","topic_num","cluster_num"
	main("lsi",500,10)
