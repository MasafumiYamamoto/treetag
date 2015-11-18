import numpy
import csv
from sklearn.cluster import KMeans
import collections
import glob
import os
import numpy
import gensim
import textedit
import time

pas="D:/Lresult"
model="lda"
tnum=10
cnum=100

####prepare model
lmodel=gensim.models.LdaModel.load(pas+"/model/"+model+"model/NVreview_o4b6t"+str(tnum)+".lda")
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

ifile=open(pas+"/ks/testrev.csv","r")
idata=csv.reader(ifile)
idata.next()
revlist=collections.Counter()
revvec=collections.Counter()
revlen=collections.Counter()
n=0
for line in idata:
	doc=textedit.textedit(line[5])
	doc=doc.lower().split()
	docset=set(doc)-stopset
	vec_bow = dictionary.doc2bow(docset)
	vec_lmodel = lmodel[vec_bow]
	rlen=0
	revlist[line[0],line[6]]=[0]*tnum
	for num in range(0,len(vec_lmodel)):
		rlen=rlen+vec_lmodel[num][1]*vec_lmodel[num][1]
		revlist[line[0],line[6]][vec_lmodel[num][0]]=vec_lmodel[num][1]
	#revlen[line[0],line[6]]
	rlen=numpy.sqrt(rlen)
	#print revlist[line[0],line[6]]
	revlist[line[0],line[6]]=revlist[line[0],line[6]]/rlen
	#print revlist[line[0],line[6]]
print len(revlist)/3

kdata=numpy.array(revlist.values())
kmeans_model=KMeans(n_clusters=len(revlist)/3,random_state=1).fit(kdata)
labels=kmeans_model.labels_

wfile=open(pas+"/ks/busclus/"+line[2]+".csv","wb")
writer=csv.writer(wfile)
writer.writerow(["revid","sent","clus"])

for num in range(0,len(revlist)):
	writer.writerow(list(revlist.keys()[num])+[labels[num]])
