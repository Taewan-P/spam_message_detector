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

def naivebayes_classifier(pxc,px_nc, pc):
  return (pxc*pc) / (pxc*pc + px_nc*(1-pc))


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

  # What we want to do : (p(x|c)p(c)) / (p(x|c)p(c) + p(x|ㄱc)p(ㄱc))
  keywords, rank, graph = wordrank_extractor.extract(analysis, beta, max_iter)
  spam_keywords = list(keywords)
  top_spam_keywords = spam_keywords[1:6] # This keyword list should be changed depending on what you wish to train.

  counted_keywords = {}
  counted_spam_probability = {}
  counted_ham_probability = {}
  # counted = [spam, nonspam]
  for k in top_spam_keywords:
    counted = count_keywords(k)
    newkey = {k: counted}
    counted_keywords.update(newkey)
    spamprob = {k: probability_calc(counted[0], len(analysis), 0.5)} # P(x|c)
    hamprob = {k: probability_calc(counted[1], len(total) - len(analysis), 0.5)} # P(x|ㄱc)
    counted_spam_probability.update(spamprob)
    counted_ham_probability.update(hamprob)

  # P(x|ㄱc) is the probability of a ham message including the "word" not being a spam message=(ham).


  # P(c) is the probability of the message being a spam
  prob_spam = probability_calc(len(analysis), len(total), 0)
  # P(~c)
  prob_not_spam = 1 - prob_spam

  # log_prob_spam = math.log(probability_calc(len(analysis), len(total), 0))
  # log_prob_not_spam = math.log(1 - probability_calc(len(analysis), len(total), 0))
  
  answer = {}
  for p in top_spam_keywords:
    temp = {p: naivebayes_classifier(counted_spam_probability[p], counted_ham_probability[p], prob_spam)}
    answer.update(temp)
  
  print(answer)