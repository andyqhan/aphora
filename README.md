# aphora

## aphora.py
I wrote this script in order to convert my list of quotes (I call them
aphora lol) to a Notion database (table). The input data is copy-pasted from a
plaintext document I had with quotes from books of the form

QUOTE
- AUTHOR, SOURCE

I copy-pasted this into a temporary Notion page (stored at `page`). The script
returns a database with the quote, author, and source in their own columns.

## aphora-org.py
After writing aphora.py and converting to Notion, I noticed that my table
of some 300+ quotes was very slow in the Electron (🤢)-based Notion client. By
this time, I had begun to become enamoured with Emacs and org-mode. So this is
a tiny script that converts a CSV file (downloaded from the Notion database) to
an org-mode file.

I used `pandas` to wrangle the CSV, because I wanted more practice with it.
To make the script more efficient, I could just import the CSV- and dataframe-related
modules.
