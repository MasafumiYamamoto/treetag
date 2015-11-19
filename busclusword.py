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
for t in range(0,10):
    for w in wlist[t]:
        tflist[w]=tflist[w]+1
#print tflist

wfile=open(pas+"/ks/busclusword/"+busname+".csv","wb")
writer=csv.writer(wfile)
for t in wlist:
    wordsum=sum(wlist[t].values())
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
wfile.close()
