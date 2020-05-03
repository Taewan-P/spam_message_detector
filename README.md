# spam_message_detector
Distinguish Korean spam messages with Machine Learning.

**Well, Right now this is not a detector, but close to an analysis report. Please read the whole README.md to see what is going on.😄**

## Beginning

Recently, I got annoyed with spam messages that keeps coming to my phone. I have seen several articles about how some data scientists put deep learning into distinguishing spam messages in Korean. I thought it would be cool to make your own spam detector since I recently seen some patterns of spam messages. So I decided to make one. However, this is my first time with Machine Learning. I do not know **anything** about it. I had no clue where to start before I read an article about **Naive Bayes classifier**. After reading this, I thought this is what I should use for my project.



## First Guess

In my phone, I had about 1500 received messages. I made a csv file of all my messages that were in my phone and classified spam/ham. And about 10% of them were spam messages. While looking at the spam messages in my phone, I found some patterns. Spam messages are likely to include:

1. Special Characters
2. Weird website address
3. To unsubscribe, call XXXXXXXXXX
4. [Sent from Web], (Advertisement), Sent from overseas
5. ID and PW for weird website

I would definitely say that Pattern number 4 is not typically true, not really all messages with number 4 is spam. But, my phone has been repetitively receiving messages with pattern number 4 whis is a spam message, so I decided to put this one too.



## First Try

First of all, I used [KRWordBank](https://github.com/lovit/kr-wordrank) Library to find out the words that are mostly in spam messages. The top 5 words that spam messages include:

1. ```"[Web 발신]" - meaning that it is sent from the web.```
2. ```"[국제발신]" - meaning that it is sent from overseas.```
3. ```"무료거부" - meaning "To stop subscribing this message(FREE)."```
4. ```"ld" - Tricky one. The robots would detect the word "ID", so the sender switched capital i to lowercase L.```
5. ```"(광고)" - meaning that this is an advertisement.```



Based on this statistics, I came up with the code of counting messages that includes common words in spam messages.

```python
  def count_keywords(word): # returns [spam_count, ham_count]
    result = [0,0]
    for i in total: # i is ['message content', 'ham/spam']
      if word in i[0]:
        if i[1] == "spam":
          result[0] += 1
        else: # ham
          result[1] += 1
    return result
```

*I coded the old way though, I will change the code later*.

After running this code, I found out that the word that is common in spam messages **can** be common in ham messages too. 

```reStructuredText
1. "[Web발신]":[95, 942]
2. "[국제발신]":[54, 46]
3. "무료거부":[31, 5]
4. "lD":[9, 0]
5. "(광고)":[45, 22]
```



The most common word "[Web발신]" is more common in regular ham messages. Well this is because the data I have for ham messages are way more than spam messages, and that phrase will be always in front of your message when you send a message via internet. Well, I decided to use the sixth most common word instead of  "[Web발신]" : ```"PW" - meaning password.```



### The Probability of P(x|c)

If I picked a spam message, The probability of the message including "A" = spam A word count / total spam.

For example, number 2, "[국제발신]". The probability of the picked spam message including that word being a spam is ```54/150 = 36%```.  If you include Laplace Smoothing, it would be ```54+0.5/150+1 = 36.09% ```. Pretty much the same. Let's calculate the rest of the probability.

```reStructuredText
1. "[국제발신]" : 0.3609271523178808
2. "무료거부" : 0.20860927152317882
3. "lD" : 0.06291390728476821
4. "(광고)" : 0.30132450331125826
5. "PW" : 0.06291390728476821
```



### P(c)s

In my case, the P(c)s are the probability of a message being a spam.

```python
  # P(c) is the probability of the message being a spam
  # len(analysis) is the value of total spam messages out of the data extracted from my csv.
  # len(total) is the value of total messages including spam and ham message.
  prob_spam = probability_calc(len(analysis), len(total), 0)
  # P(~c)
  prob_not_spam = 1 - prob_spam
```

#### Result

```
P(c) : 0.1038781163434903
P(~c) : 0.8961218836565097
```



### The Mighty Formula

What is this title about? I am talking about the Naive Bayes Classifier formula!

```P(c|x) = P(x|c) P(c) / { P(x|c) P(c) + P(x|~c) P(~c) }```

I am using this formula because I did not assume ```P(c) = P(~c) = 0.5```. That's why the denominator is longer that usual.



### Calculation Finished.

Well... I calculated the results for the top 5 spam words that spam messages include. The probability of the message being a spam when a message includes this word is...

```
"[국제발신]" : 0.538144824492084
"무료거부" : 0.8506066969512376
"lD" : 0.949720339750663
"(광고)" : 0.6678162925754492
"PW" : 0.8629433434994991
```

Pretty interesting huh? You can see that not all the top rank words have high probabilities.



### To Be Continued...

Well, I guess this is it for now. I do not have enough data to train the model I wanted to make. Not only there is no Korean Spam message dataset in the Internet, but also the dataset that exists is quite different from what I am looking for. The dataset I used for analysis is extracted from **MY PHONE**, so I guess I have to wait again to get some spam messages stacked. Haha

If you have spam messages dataset in Korean, feel free to open an issue or email me through swimingtw@gmail.com. If there is something wrong with my article, feel free to open an issue and correct me. As I mentioned above, I am new to Machine Learning and I am in a process of learning new things. Thank you for reading.
