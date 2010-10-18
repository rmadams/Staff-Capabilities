'''
Created on Oct 13, 2010

@author: 516026
'''

import csv
from wxPython.wx import *

stopwords_file = 'C:\\Documents and Settings\\516026\\Desktop\\stopwords.txt'

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
    for item in my_reader:
        print item
        