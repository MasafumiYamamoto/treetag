import csv

ifile=open("D:/Lresult/model/hoge.csv","r")
idata=csv.reader(ifile)
idata.next()
for line in idata:
    wfile=open("D:/Lresult/model/test/"+line[2]+".csv","ab")
    wri=csv.writer(wfile)
    wri.writerow(line)
    wfile.close()
ifile.close()
