###write top fwords

def main(cluster,fwords):
    import csv
    import os
    import collections
    import textedit
    import numpy
    import time

    busname="4bEjOyTaDG24SY5TxsaUNQ"
    pas="D:/Lresult"
    pas2="//kaede/PPTShare/masafumi/musc/20151117"
    fewords=int(fwords)####feature word num
    cnum=int(cluster)###cluster_num

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

    ifile=open(pas+"/ks/busclus/"+busname+"_clus.csv","r")
    idata=csv.reader(ifile)
    idata.next()
    cluslist=collections.Counter()
    for line in idata:
        ####revid,sentiment_num,clus
        cluslist[line[0],line[1]]=int(line[2])
    ifile.close()

    ifile=open(pas+"/ks/busent_anv/"+busname+".csv","r")
    idata=csv.reader(ifile)
    wlist=collections.Counter()####word dictionary for each cluster
    for num in range(-1*cnum,cnum+1):
        wlist[num]=collections.Counter()
    for line in idata:
        if((line[0],line[6]) in cluslist):
            doc=set(line[5].lower().split())-stopset
            for t in doc:
                wlist[cluslist[line[0],line[6]]][t]=wlist[cluslist[line[0],line[6]]][t]+1
    ifile.close()
    print "input fin",time.ctime()

    wfile=open(pas+"/ks/busclusword/"+busname+"_clusword.csv","wb")
    writer=csv.writer(wfile)
    header=[]
    for num in map(str,range(-1*cnum,cnum+1)):
        header=header+["c"+num+"word","c"+num+"tfidf"]
    writer.writerow(header)

    tflist_p=collections.Counter()
    tflist_n=collections.Counter()
    wordlen=[]
    wordsum=collections.Counter()
    for t in range(-1*cnum,cnum+1):
        wordlen.append(len(wlist[t]))
        wordsum[t]=sum(wlist[t].values())
    print wordlen,max(wordlen)
    fewords=max(wordlen)
    for t in range(0,cnum+1):
        for w in wlist[t]:
            tflist_p[w]=tflist_p[w]+1
        for w in wlist[-1*t]:
            tflist_n[w]=tflist_n[w]+1

    toplist=collections.Counter()
    for t in range(1,cnum+1):
        tmp=collections.Counter()
        for w in wlist[t]:
            tmp[w]=1.0*wlist[t][w]/wordsum[t]*numpy.log(1+1.0*cnum/tflist_p[w])
        toplist[t]=tmp.most_common(fewords)
        tmp=collections.Counter()
        for w in wlist[-1*t]:
            tmp[w]=1.0*wlist[-1*t][w]/wordsum[-1*t]*numpy.log(1+1.0*cnum/tflist_n[w])
        toplist[-1*t]=tmp.most_common(fewords)


    for num in range(0,fewords):
        wrlist=[]
        for t in range(-1*cnum,cnum+1):
            if(len(wlist[t])<=num):
                wrlist=wrlist+["_",0]
            else:
                tmp=toplist[t]
                wrlist.append(tmp[num][0])
                wrlist.append(tmp[num][1])
        writer.writerow(wrlist)
    print "fin",time.ctime()

if __name__ == '__main__':
    print "cluster_num,feature_words"
    main(10,10)
