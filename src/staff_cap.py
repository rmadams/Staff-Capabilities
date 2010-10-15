'''
Created on Oct 13, 2010

@author: 516026
'''

import csv
from wxPython.wx import *



if __name__ == '__main__':
    application = wxPySimpleApp()
    # Create an open file dialog
    dialog = wxFileDialog ( None, style = wxOPEN )

    # Show the dialog and get user input
    if dialog.ShowModal() == wxID_OK:
        print 'Selected:', dialog.GetPath()

        # The user did not select anything
    else:
        print 'Nothing was selected.'
    # Destroy the dialog
    dialog.Destroy()