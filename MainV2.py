import csv
from keyword_search import search_keyword
from writer import write


def choose():
    print("Enter y if you want to add a new quote and keyword\nEnter n if you want to find a quote based of a keyword.")
    choice = input("")

    if choice == 'y':
        write()
        choose()

    elif choice == 'n':
        search_keyword()
        choose()

    else:
        print('invalid input()')


choose()
