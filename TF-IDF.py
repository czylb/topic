import numpy as np
import pandas as pd

data = pd.read_csv('try.csv')

num = data['regionID']
num = list(num.drop_duplicates())
data0 = np.array(data)
a = [[] for i in range(len(num))]

for i in range(len(num)):
	for j in range(len(data0)):
		if data0[j][9] == num[i]:
			a[i].append(data0[j][0])

import jieba #对name进行分词
import jieba.analyse as anls #关键词提取

text = [[] for i in range(len(a))]
for i in range(len(a)):
	text[i] = jieba.lcut(''.join(a[i]), cut_all=False)

# 二维转一维字符串数组
# l=[]
# for m in range(len(text)):
#     for i in text[m]:
#         l.append(i)

stopwords = ['云南','云南省','昆明','昆明市','NO','正宗','西山区']
final = [[] for i in range(len(a))]

for i in range(len(text)):
	for seg in list(text[i]):
		if seg not in stopwords:
			final[i].append(seg)

for i in range(len(final)):
	for x, w in anls.extract_tags(str(final[i]), topK=1, withWeight=True):
		print('%s %s' % (x, w))