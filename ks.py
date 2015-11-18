import treetaggerwrapper
import csv
import collections
import time

tagger=treetaggerwrapper.TreeTagger(TAGLANG="en",TAGDIR="C:/TreeTagger")
#doc="I used to love it so much I can't rate it that low.\n\n Part of me hopes it gets better."

list1=""
nlist=["NN","NNS","NP","NPS"]##norm
vlist=["VV","VVG","VVD","VVN","VVP","VVZ"]###verb
jlist=["JJ","JJS","JJR"]##adjecttive
snum=0

'''
for t in tgs:
    t_kind=t.split()[1]
    if(t_kind!="SENT"):
        if(t_kind in jlist):
            #list1.append(t.split()[0])
            list1=list1+" "+t.split()[0]
    else:
        if(len(list1.split())>0):
            #list1=list1+" "+t.split()[0]
            print snum,len(list1.split()),list1
            list1=""
            snum=snum+1
        else:
            list1=""
'''
subfile=open("D:/Lresult/NV_s5/subrev_1000.csv","r")
subdata=csv.reader(subfile)
subidlist=collections.Counter()
for line in subdata:
    subidlist[line[0]]=1
print "subid",len(subidlist)
subfile.close()

l=0
nplist=collections.Counter()
ifile=open("D:/Lresult/ks/NVrevraw.csv","r")
idata=csv.reader(ifile)
for line in idata:
    if(line[0] in subidlist):
        l=l+1
        doc=line[5]
        tgs=tagger.TagText(doc)
        for t in tgs:
            kind=t.split()
            if(kind[1]=="NP" or kind[1]=="NPS"):
                nplist[kind[0]]=nplist[kind[0]]+1
        if(l%10==0):
            print l,len(nplist),time.ctime()

print "nplist",len(nplist)
wfile=open("D:/Lresult/stopwords/NPlist.csv","wb")
writer=csv.writer(wfile)
writer.writerow(["npword","num"])
for t in nplist:
    writer.writerow([t,nplist[t]])
wfile.close()
