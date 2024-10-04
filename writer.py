import csv


def write():
    quote_input = input('Enter the quote you want to add: ')
    keyword_input = input('Enter the keyword/s you want to add: ')

    # Split keywords into a list and strip any leading/trailing spaces
    keywords = [keyword.strip() for keyword in keyword_input.split(',')]

    # Join keywords into a single string without commas
    joined_keywords = ' '.join(keywords)  # Change here to space between keywords

    # Open the CSV file in append mode
    with open('Data.csv', "a", ) as datafile:
        writer = csv.writer(datafile)

        # Write the quote and the joined keywords as a single row
        writer.writerow([quote_input, joined_keywords])




