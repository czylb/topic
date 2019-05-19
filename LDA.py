#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

data = pd.read_csv('try0.csv',error_bad_lines=False)


# In[3]:


num = data['regionID']
num = list(num.drop_duplicates())
data0 = np.array(data)
a = [[] for i in range(len(num))]

for i in range(len(num)):
    for j in range(len(data0)):
        if data0[j][9] == num[i]:
            a[i].append(data0[j][0])


# In[5]:


import jieba #对name进行分词
import jieba.analyse as anls #关键词提取

text = [[] for i in range(len(a))]
for i in range(len(a)):
	text[i] = jieba.lcut(''.join(a[i]), cut_all=False)


# In[39]:


#二维转一维字符串数组
# l=[]
# for m in range(len(texts)):
#     for i in texts[m]:
#         l.append(i)

#停用词列表        
stopwords = ['云南','云南省','昆明','昆明市','NO','正宗','.','西山区','五华区','卫平']
final = [[] for i in range(len(a))]

for i in range(len(text)):
     for seg in list(text[i]):
        if seg not in stopwords:
            final[i].append(seg)


# In[40]:


import codecs
from gensim import corpora
from gensim.models import LdaModel
from gensim.corpora import Dictionary


# In[56]:


dictionary = [[] for i in range(len(a))]
for i in range(len(final)):
    dictionary[i] = corpora.Dictionary([final[i]])
    
corpus = [[] for i in range(len(a))]
for i in range(len(final)):
    corpus[i] = [ dictionary[i].doc2bow(text) for text in [final[i]]]
    
lda = [[] for i in range(len(a))]
for i in range(len(final)):
    lda[i] = LdaModel(corpus=corpus[i], id2word=dictionary[i], num_topics=1)
    
topic_list = [[] for i in range(len(a))]  
for i in range(len(final)):
    topic_list[i]=lda[i].print_topics()

f = open('b.txt','w')
for i in range(len(final)):   
    for topic in topic_list[i]:
        f.write(lda[i].print_topic(0) + ';' + str(num[i]) +'\n')
f.close()


# In[53]:


topic_list


# In[ ]:




