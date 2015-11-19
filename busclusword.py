

def main(cluster,fwords):
    import csv
    import os
    import collections
    import textedit
    import numpy

    busname="4bEjOyTaDG24SY5TxsaUNQ"
    pas="D:/Lresult"
    pas2="//kaede/PPTShare/masafumi/musc/20151117"
    fewords=int(fwords)####feature word num
    cnum=int(cluster)###cluster_num

    ifile=open(pas+"/ks/busclus/"+busname+".csv","r")
    idata=csv.reader(ifile)
    idata.next()
    cluslist=collections.Counter()
    for line in idata:
        ####revid,sentiment_num,clus
        cluslist[line[0],line[1]]=int(line[2])
    ifile.close()
    ifile=open(pas2+"/ks/bussent/"+busname+".csv","r")
    idata=csv.reader(ifile)
    wlist=collections.Counter()####word dictionary for each cluster
    for num in range(0,cnum):
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
    for t in range(0,cnum):
        wordlen.append(len(wlist[t]))
        wordsum[t]=sum(wlist[t].values())
        for w in wlist[t]:
            tflist[w]=tflist[w]+1
    print wordlen,max(wordlen)

    wfile=open(pas+"/ks/busclusword/"+busname+".csv","wb")
    writer=csv.writer(wfile)
    header=[]
    for num in map(str,range(0,cnum)):
        header=header+["c"+num+"word","c"+num+"tfidf"]
    writer.writerow(header)

    toplist=collections.Counter()
    for t in range(0,cnum):
        tmp=collections.Counter()
        for w in wlist[t]:
            tmp[w]=1.0*wlist[t][w]/wordsum[t]*numpy.log(1.0*cnum/tflist[w])
        toplist[t]=tmp.most_common(fewords)

    for num in range(0,cnum):
        wwlist=[]
        for t in range(0,fewords):
            if(len(wlist[t])<=num):
                wwlist=wwlist+["_",0]
            else:
                tmp=toplist[t]
                wwlist.append(tmp[num][0])
                wwlist.append(tmp[num][1])
        writer.writerow(wwlist)
    wfile.close()

if __name__ == '__main__':
    print "cluster_num,feature_words"
    main(10,10)
