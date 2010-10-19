'''
Created on Oct 13, 2010

@author: 516026
'''

import csv
import string
from wxPython.wx import *

stopwords_file = 'C:\\Documents and Settings\\516026\\Desktop\\stopwords.txt'
outfile = 'C:\\Documents and Settings\\516026\\Desktop\\outwords.txt'

if __name__ == '__main__':
    stopwords = []
    for item in open(stopwords_file).readlines():
        stopwords.append(item.rstrip())
    print stopwords
    application = wxPySimpleApp()
    # Create an open file dialog
    dialog = wxFileDialog ( None, style = wxOPEN )

    # Show the dialog and get user input
    if dialog.ShowModal() == wxID_OK:
        csv_file = dialog.GetPath()
        print 'Selected:' + csv_file
        # The user did not select anything
    else:
        print 'Nothing was selected.'
    # Destroy the dialog
    dialog.Destroy()
    my_reader = csv.reader(open(csv_file))
    out_words = []
    exclude = set(string.punctuation)
    for item in my_reader:
        print item
        s = item[5] 
        s = ''.join(ch for ch in s if ch not in exclude)
        s = s.lower()
        print "My String:"
        print s
        for words in string.split(s):
            if stopwords.count(words) == 0:
                print words
                out_words.append(words)
    my_file = open(outfile, 'w')
    for word in out_words:
        my_file.write(word)
        my_file.write('\n')
    my_file.close()

        