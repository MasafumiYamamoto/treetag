import csv
import re

ifile=open("D:/Lresult/ks/NVrevraw.csv","r")
idata=csv.reader(ifile)
wfile=open("D:/Lresult/ks/NVrevrawsent.csv","wb")
wri=csv.writer(wfile)
wri.writerow(["revid","userid","busid","star","date","sent","sentnum"])
for line in idata:
    doc=line[5]
    doc=doc.replace("\n"," ")
    doc=re.split("[.!?:;]",doc)
    sentnum=0
    for sent in doc:
        if(len(sent)>0):
            wlist=[]
            wlist.append(line[0])
            wlist.append(line[1])
            wlist.append(line[2])
            wlist.append(line[3])
            wlist.append(line[4])
            wlist.append(sent)
            wlist.append(sentnum)
            sentnum=sentnum+1
            wri.writerow(wlist)

ifile.close()
wfile.close()
