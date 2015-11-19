import csv
import os
import collections
import textedit
import numpy

busname="IjcKyB-LUnev2iapzyJ11w"

pas="D:/Lresult"
pas2="//kaede/PPTShare/masafumi/musc/20151117"
ifile=open(pas+"/ks/busclus/"+busname+".csv","r")
idata=csv.reader(ifile)
idata.next()
cluslist=collections.Counter()
for line in idata:
    ####revid,sent,clus
    cluslist[line[0],line[1]]=int(line[2])
ifile.close()
ifile=open(pas2+"/ks/bussent/"+busname+".csv","r")
idata=csv.reader(ifile)
wlist=collections.Counter()
for num in range(0,10):
    wlist[num]=collections.Counter()
for line in idata:
    doc=textedit.textedit(line[5])
    doc=doc.split()
    for t in doc:
        wlist[cluslist[line[0],line[6]]][t]=wlist[cluslist[line[0],line[6]]][t]+1
ifile.close()

tflist=collections.Counter()
wordlen=[]
wordsum=collections.Counter()
for t in range(0,10):
    wordlen.append(len(wlist[t]))
    wordsum[t]=sum(wlist[t].values())
    for w in wlist[t]:
        tflist[w]=tflist[w]+1
print wordlen,max(wordlen)

#wfile=open(pas+"/ks/busclusword/"+busname+".csv","wb")
wfile=open(pas+"/ks/busclusword/hoge.csv","wb")
writer=csv.writer(wfile)
header=[]
for num in map(str,range(0,10)):
    header=header+["c"+num+"word","c"+num+"num","c"+num+"tfidf"]
writer.writerow(header)
for num in range(0,max(wordlen)):
    wwlist=[]
    for t in range(0,10):
        if(len(wlist[t])<=num):
            wwlist=wwlist+[" "," "," "]
        else:
            tmp=wlist[t].items()
            wwlist.append(tmp[num][0])
            wwlist.append(tmp[num][1])
            wwlist.append(1.0*tmp[num][1]/wordsum[t]*numpy.log(10/tflist[tmp[num][0]]))
    writer.writerow(wwlist)
'''
for t in wlist:
    wwlist=["clus","word"]
    wwlist=wwlist+wlist[t].keys()
    writer.writerow(wwlist)
    wwlist=[t,"num"]
    wwlist=wwlist+wlist[t].values()
    writer.writerow(wwlist)
    wwlist=[t,"tfidf"]
    for w in wlist[t]:
        wwlist.append(1.0*wlist[t][w]/wordsum*numpy.log(10/tflist[w]))
    writer.writerow(wwlist)
    #writer.writerow([t,"sum",wordsum])
'''


wfile.close()
