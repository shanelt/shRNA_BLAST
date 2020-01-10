import Tkinter,tkFileDialog
import csv
import os

#Open input files
root = Tkinter.Tk()
root.withdraw()
root.update()
print 'Please choose files to convert: '
in_filenames = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')
in_filenames_len = len(in_filenames)
print "You are opening files: "
for x in xrange(0, in_filenames_len):
	print in_filenames[x].split('/')[-1]
print '\n'
print "You are opening %d files" % (in_filenames_len)
print '\n'

# Test inputs
#in_filenames=["/Volumes/Adam/1326971/seq/9_GAG_Plate_ag_test_plate_A02.seq","/Volumes/Adam/1326971/seq/70_GAG_Plate_ag_test_plate_F09.seq"]
#in_filenames_len=2
#out_filename="testout.fasta"

# Redirect to input directory
fPath=in_filenames[0][0:(len(in_filenames[0])-1-len(in_filenames[0].split("/")[-1]))]
os.chdir(fPath)

# Create output file
out_filename = raw_input("Please enter output filename: ")
print 'You are creating output file: %s'% out_filename
print '\n'

#Read file into temperarory storage and write in output file

with open (out_filename, 'w') as fout:
    wfout=csv.writer(fout)
    for x in xrange (0, in_filenames_len):
        with open(in_filenames[x], "r") as fin:
            rfin = csv.reader(fin)
            for row in rfin:
                row=str(row[0])
                if (">" in row):
                    wfout.writerow([row])
                    #print row
                else:
                    n=int(len(row)/80)
                    for i in xrange(0,n):
                        wfout.writerow([row[i*80:(i+1)*80]])
                    if n*80<len(row):
                        wfout.writerow([row[n*80:]])

print "Your files have been successfully concatenated. (@w@)"
