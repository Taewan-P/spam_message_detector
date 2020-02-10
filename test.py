import csv
from collections import defaultdict
from krwordrank.word import KRWordRank


def count_keywords(word): # returns [spam_count, ham_count]
  result = [0,0]
  for i in total: # i is ['message content', 'ham/spam']
    if word in i[0]:
      if i[1] == "spam":
        result[0] += 1
      else: # ham
        result[1] += 1
  return result

def probability_calc(condition, total, k):
  return (condition + k) / (total + 2 * k)


with open('messages.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  analysis = []
  total = []
  for row in spamreader: # row is a list ['message content', 'ham/spam']
    a = row[0].replace('\n', ' ') # Delete new lines
    row[0] = a # Only content
    total.append(row) # Whole data
    if row[1] == 'spam':
      analysis.append(a) # Analysis for only spam messages
    
  wordrank_extractor = KRWordRank(
    min_count = 5,
    max_length = 10,
    verbose = True
  )
  beta = 0.85
  max_iter = 10

  keywords, rank, graph = wordrank_extractor.extract(analysis, beta, max_iter)
  spam_keywords = list(keywords)
  top_spam_keywords = spam_keywords[1:6] # This keyword list should be changed depending on what you wish to train.

  counted_keywords = {}
  counted_spam_probability = {}
  # counted = [spam, nonspam]
  for k in top_spam_keywords:
    counted = count_keywords(k)
    newkey = {k: counted}
    counted_keywords.update(newkey)
    spamprob = {k: probability_calc(counted[0], len(analysis), 0.5)}
    counted_spam_probability.update(spamprob)

  # P(c)
  prob_spam = probability_calc(len(analysis), len(total), 0)
  # P(~c)
  prob_not_spam = 1 - prob_spam

  log_prob_spam = math.log(probability_calc(len(analysis), len(total), 0))
  log_prob_not_spam = math.log(1 - probability_calc(len(analysis), len(total), 0))
  print(prob_spam)
  print(prob_not_spam)
  print(log_prob_spam)
  print(log_prob_not_spam)
  print(counted_spam_probability) # P(x|c)s
  # P(c)

  
  

