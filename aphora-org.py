#!/usr/bin/env python3

import pandas as pd

""" After writing aphora.py and converting to Notion, I noticed that my table
of some 300+ quotes was very slow in the Electron (🤢)-based Notion client. By
this time, I had begun to become enamoured with Emacs and org-mode. So this is
a tiny script that converts a CSV file (downloaded from the Notion database) to
an org-mode file.

I used pandas to wrangle the CSV, because I wanted more practice with pandas.
To make it more efficient, I could just import the CSV- and dataframe-related
modules. """

data = pd.read_csv('aphora.csv')

def convert_org(data_in):
    """
    Takes a pd.DataFrame DATA_IN and converts it to an org format.
    """
    with open('output.org', 'w') as file:
        for row in range(len(data) - 1):
            this_row = data_in.iloc[row, :]
            file.write(f"* {row}\n")  # creates heading. starts at 0
            file.write("#+BEGIN_VERSE:\n")  # verse keeps whitespace
            file.write(str(this_row['quote']) + "\n")
            file.write("#+END_VERSE\n")
            file.write(str(this_row['author']) + "\n")
            file.write(str(this_row['source']) + "\n")
            file.write(str(this_row['created time']) + "\n")
