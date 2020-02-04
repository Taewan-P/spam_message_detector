import csv
with open('messages.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader: # row is a list ['message content', 'ham/spam']
        a = row[0].replace('\n', ' ') # Delete new lines
        row[0] = a
        print(row)
