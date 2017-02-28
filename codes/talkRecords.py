import jieba
import numpy
import codecs
import  pandas
import  matplotlib.pyplot as plt
from wordcloud import WordCloud
'''
pip install jieba
pip install wordcloud
generator wordcloud from text by idf

'''
file = codecs.open(u"alice.txt",'r')
content =file.read()
file.close()
segment =[]
segs =jieba.cut(content)
for seg in segs:
    if len(seg)>1 and seg!='\r\n':
        segment.append(seg)
words_pf =pandas.DataFrame({'segment':segment})
words_pf.head()
# stopwords =pandas.read_csv('stopwords.txt',index_col=False,quoting=3,seq='\t',names=['stopword'],)
# # words_pf =words_pf[~words_pf.segment.isin(stopwords.stopword)]

word_state =words_pf.groupby(by=['segment'])['segment'].agg({'number':numpy.size})
word_state =word_state.reset_index().sort(columns='number',ascending=False)
print word_state
def wordcloudGenerator():
    wordcloud =WordCloud(background_color='black')
    wordcloud=wordcloud.fit_words(word_state.head(100).itertuples(index=False))
    plt.imshow(wordcloud)
    plt.show()

from scipy.misc import imread
from wordcloud import ImageColorGenerator
bimg =imread('1520824.jpg')
bimgColors =ImageColorGenerator(bimg)
wordcloud = WordCloud(background_color='black')
wordcloud = wordcloud.fit_words(word_state.head(100).itertuples(index=False))
plt.axis('off')
plt.imshow(wordcloud.recolor(color_func=bimgColors))
plt.show()
