import csv
import collections
import numpy

pas="D:/Lresult/ks/hoge/"
dic=collections.Counter()
sumt=collections.Counter()
for num in range(0,10):
    dic[num]=collections.Counter()
    sumt[num]=0
dicall=collections.Counter()

for num in range(0,10):
    ifile=open(pas+"clus"+str(num)+"_text.dict","r")
    idata=csv.reader(ifile,delimiter="\t")
    for line in idata:
        dic[num][line[1]]=int(line[2])
        sumt[num]=sumt[num]+int(line[2])
        dicall[line[1]]=dicall[line[1]]+1
    print dic[num].most_common(3),sumt[num]
    ifile.close()

for num in range(0,10):
    wfile=open(pas+"tfidf"+str(num)+".csv","wb")
    writer=csv.writer(wfile)
    writer.writerow(["word","tfidf"])
    for word in dic[num]:
        score=1.0*dic[num][word]/sumt[num]*numpy.log(1.0/dicall[word]+1.0)
        writer.writerow([word,score])
    wfile.close()
