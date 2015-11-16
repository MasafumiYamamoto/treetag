import csv
import collections

pas="D:/Lresult/"
o4file=open(pas+"stopwords/stopwords_ranksnl.csv","r")
o4data=csv.reader(o4file)
stoplist=collections.Counter()
for line in o4data:
    stoplist[line[0]]=1

o4file.close()



ipas="D:/Lresult/ks/hoge/"

wfile=open(ipas+"tfidfmix.csv","wb")
writer=csv.writer(wfile)

for num in range(0,10):
    ifile=open(ipas+"tfidf"+str(num)+".csv","r")
    idata=csv.reader(ifile)
    ilist=collections.Counter()
    idata.next()
    for line in idata:
        if(line[0] not in stoplist):
            ilist[line[0]]=float(line[1])
    ifile.close()

    writer.writerow(["cluster",num])
    writer.writerows(ilist.most_common(10))
wfile.close()
