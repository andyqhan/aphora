from notion.client import NotionClient
from notion.block import TextBlock
from notion.block import BasicBlock

""" I wrote this script in order to convert my list of quotes (I call them
aphora lol) to a Notion database (table). The input data is copy-pasted from a
plaintext document I had with quotes from books of the form

QUOTE
- AUTHOR, SOURCE

I copy-pasted this into a temporary Notion page (stored at PAGE). The script
returns a database with the quote, author, and source in their own columns. """

client = NotionClient(
    token_v2 = "YOUR_NOTION_KEY")

page = client.get_block("NOTION_LINK_TO_TEMP_FILE")   # aphora temp


def remove_newlines():  # replace all newlines with spaces
    for line in page.children:
        line.title = line.title.replace("\n", " ")


'''def fix_citation():  # replace all implied citations with explicit ones DOESN'T WORK LOL
    for i in range(len(page.children) - 1, 0, -1):
        if page.children[i].title[0] != page.children[i - 2].title[0] and page.children[i].title[0] == '—':
            new_citation = page.children.add_new(TextBlock, title=page.children[i].title)
            new_citation.move_to(page.children[i-2], 'after')'''

collection_page = client.get_collection_view(
    'https://www.notion.so/273548f56de54913bd19638d2453975c?v=f0f2ae99e34d491ab8b99431fb73c59c')    # aphora


def get_author(cit_line):   # takes a string in the form '- author, source' and returns a tuple (author, source)
    cit_line = cit_line.strip('— ')
    slice_space = 0
    for char in range(len(cit_line)):
        if cit_line[char] == ',':   # check for the comma splice
            slice_space = char
            break
    if slice_space == 0:    # if there's no comma splice return tuple (author, '')
        author = cit_line
        return author, ''
    author = cit_line[:slice_space]
    source = cit_line[slice_space + 2:]
    return author.strip(' '), source.strip(' ')


def import_aphora():
    for i in range(len(page.children)):
        if page.children[i].title[0] != '—':
            new_row = collection_page.collection.add_row()
            new_row.quote = page.children[i].title
            new_row.author = get_author(page.children[i + 1].title)[0]
            new_row.source = get_author(page.children[i + 1].title)[1]


