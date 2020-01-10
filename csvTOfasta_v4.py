import sys
import csv
import Tkinter
from Tkinter import Tk
from tkFileDialog import askopenfilename
import os

def toLower(listx):
    outlist = []
    for i in listx:
        outlist.append(i.lower())
    return outlist

#Open file
print 'Please find your input file: '
root = Tk()
root.withdraw()
root.update()
in_filename = askopenfilename()

print 'You are opening file: %s'% in_filename
print '\n'

#Redirect to input file directory
in_filePath="/".join(in_filename.split("/")[:-1])
os.chdir(in_filePath)

#Create output file
out_filename = raw_input("Please enter output filename: ")
print 'You are creating output file: %s'% out_filename
print '\n'

#Set keywords, creat lists to store keywords & corresponding column number of keywords in csv
print "Columnnames of input file:"
with open(in_filename, "r") as f:
    rf = csv.reader(f, delimiter=",")
    rfHead = next(rf)
    for i in rfHead:
        print i
your_key = raw_input("Please enter your key words seperated by comma: ")
print 'Your key words for sequences are: %s'% your_key
print '\n'
keyList = [x.strip() for x in your_key.split(',')]

#Test
#os.chdir("/Users/yolandatiao/Documents/0_Bioinformatics2017/05_TFlib_renameshRNA")
#in_filename="/Users/yolandatiao/Documents/0_Bioinformatics2017/05_TFlib_renameshRNA/Scripps_Mm_TF_LMP-d-miRe_Customer_1-78_test.csv"
#out_filename="test.fasta"
#keyList=["Plate","Position"]

#Transform
with open(in_filename, "r") as fin:
    rfin = csv.reader(fin, delimiter=",")
    finHead=next(rfin)
    keyListNumber=[]
    for i in keyList:
        keyListNumber.append(finHead.index(i))
    seqIdx=toLower(finHead).index("sequence")
    with open(out_filename, "w") as fout:
        wfout=csv.writer(fout, delimiter=",")
        for row in rfin:
            outRowHead = []
            for i in keyListNumber:
                outRowHead.append(row[i])
            outRowHeadStr="|".join(outRowHead)
            wfout.writerow([">%s"%outRowHeadStr])
            wfout.writerow
            
            rowSeq=row[seqIdx]
            n=int(len(rowSeq)/80)
            for i in xrange(0,n):
                wfout.writerow([rowSeq[i*80:(i+1)*80]])
            if n*80<len(rowSeq):
                wfout.writerow([rowSeq[n*80:]])



print "Your file has been successfully generated. (@w@)"
print '\n'
print '\n'