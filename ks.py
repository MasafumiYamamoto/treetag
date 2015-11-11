import treetaggerwrapper
import csv

tagger=treetaggerwrapper.TreeTagger(TAGLANG="en",TAGDIR="C:/TreeTagger")
'''
ifile=open("hoge.csv","r")
idata=csv.reader(ifile)
for line in idata:
    tags=tagger.TagText(line[5])
    for t in tags:
        print t
ifile.close()
'''
doc="Let me just say that this used to be a place I loved.\n\nRemember when you'd go somewhere and have good food, great service and a general pleasant experience and then a few months you'd go back and have it all again? Well one day you decide to go back and you realized everything has changed in a way that you can't describe and the place is no longer familiar. To me, that is Bar Louie\n\nI can't say the food is bad. I had an order of the pretzel sticks for an appetizer and the cinnamon sauce tasted like water and the pretzels were stale. I will say I still ate them so shame on me. My  sandwich (the Mario) as always was very good.\n\nNow here comes the bad:\n\n1. There were fruit flies EVERYWHERE. I felt like we were eating on top of a garbage dump. At one point I had to get a new drink because one flew in my beer. I understand that the establishment is an indoor/outdoor place but there is no reason for 15 fruit flies to hover over my table.\n\n2. The place is enormous and they had one, very nice, but over worked server. The girl looked like she was about to have a heart attack because she never stopped moving.\n\n3. Because of number two our service in general was not good. I can't totally blame the girl she did the best we could. I mean. I've played Diner Dash on my iPad, I know what happens when a place fills up too quickly when you are the only one working.\n\nIt's sad when a place you love turns into a place you never want to go again. I think I'm being very generous by giving it two stars but because I used to love it so much I can't rate it that low.\n\n Part of me hopes it gets better, but like an absentee father it'll just let me down again."

doc="I used to love it so much I can't rate it that low.\n\n Part of me hopes it gets better."

#print doc
doc=doc.replace("\n"," . ")
#print doc
tgs=tagger.TagText(doc)

list1=""
nlist=["NN","NNS","NP","NPS"]
vlist=["VV","VVG","VVD","VVN","VVP","VVZ"]
jlist=["JJ","JJS","JJR"]
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

for t in tgs:
    print t
