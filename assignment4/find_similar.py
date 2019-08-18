import numpy as np
from gensim import models
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import logging



'''
获取一个圆形的mask
'''
def get_mask():
    x,y = np.ogrid[:300,:300]
    mask = (x-150) ** 2 + (y-150)**2 > 130 ** 2
    mask = 255 * mask.astype(int)
    return mask
 
'''
绘制词云
'''
def draw_word_cloud(word_cloud):
    wc = WordCloud(font_path='./SimHei.ttf', background_color="white",mask=get_mask())
    wc.generate_from_frequencies(word_cloud)
    #隐藏x轴和y轴
    plt.axis("off")
    plt.imshow(wc,interpolation="bilinear")
    plt.show()


def get_wordcloud(word):
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    similar_words = model.most_similar(word, topn=20)
    word_dict = dict()
    for sim in similar_words:
        word_dict[sim[0]] = sim[1]

    draw_word_cloud(word_dict)
    return word_dict


def similarity(word_1, word_2):
    similar = model.similarity(word_1, word_2)
    print('similarity: %.4f'%similar)



if __name__=='__main__':
    model = models.Word2Vec.load('./wiki_corpus.model')

    similar_words = get_wordcloud('说')
    
    #words = ['说','说道']
    words = ['腾讯','阿里巴巴']
    similarity(words[0], words[1])


