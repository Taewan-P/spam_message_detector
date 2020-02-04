# spam_message_detector
Distinguish Korean spam messages with Machine Learning.

## Begining

Recently, I got annoyed with spam messages that keeps coming to my phone. I have seen several articles about how some data scientists put deep learning into distinguishing spam messages in Korean. I thought it would be cool to make your own spam detector since I recently seen some patterns of spam messages. So I decided to make one. However, this is my first time with Machine Learning. I do not know **anything** about it. I had no clue where to start before I read an article about Naive Bayes classifier. After reading this, I thought this is what I should use for my project.

## First Guess

In my phone, I had about 1500 received messages. And about 10% of them were spam messages. While looking at the spam messages in my phone, I found some patterns. Spam messages are likely to include:

1. Special Characters
2. Weird website address
3. To unsubscribe, call XXXXXXXXXX
4. [Sent from Web], (Advertisement), Sent from overseas
5. ID and PW for weird website

I would definitely say that Pattern number 4 is not typically true, not really all messages with number 4 is spam. But, my phone has been repetitively receiving messages with pattern number 4 whis is a spam message, so I decided to put this one too.