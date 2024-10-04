import csv


def search_keyword():
    keyword_input = input('enter the keyword you want to search with ')
    cleaned_keyword = []
    dic = []
    quote = []

    with open('Data.csv', "a+", newline='') as Datafile:
        Datafile.seek(0)
        reader = csv.DictReader(Datafile)

        for row in reader:
            keyword = row['keyword']
            keyword_list = keyword.split()
            cleaned_keyword = [i for i in keyword_list if i is not None]

            quote = row['quote']

            dic = (quote, cleaned_keyword)
            #print(dic)

            for i in cleaned_keyword:
                #print(i)
                if keyword_input == i:
                    #print(dic)
                    print(f'The keyword was found in the quote: "{quote}"')
                    break
            else:
                print('The keyword was not found')
