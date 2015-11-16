import csv
import collections
import os

###load cluster file
pas="D:/Lresult/model/test_p/"
ifile=open(pas+"V6csWcyvwOg_E2ni3V_CgA.csv","r")
idata=csv.reader(ifile)
ilist=collections.Counter()
for line in idata:
    ilist[line[0],line[4]]=line[6]
#print ilist
#print ilist

#os.mkdir("D:/Lresult/ks/hoge")
wfile=open("D:/Lresult/ks/hoge/V6csWcyvwOg_E2ni3V_CgA.csv","wb")
writer=csv.writer(wfile)
writer.writerow(["revid","userid","busid","star","date","text","sentnum","clus"])
rfile=open("D:/Lresult/ks/NVrevrawsent.csv","r")
rdata=csv.reader(rfile)
for line in rdata:
    if((line[0],line[6]) in ilist):
        doc=line
        doc=doc+[ilist[line[0],line[6]]]
        writer.writerow(doc)

ifile.close()
rfile.close()
wfile.close()
