import logging
from gensim.models import word2vec
import multiprocessing
from time import time

def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    begin = time()
    sentences = word2vec.LineSentence("wiki_corpus")
    # size：单词向量的维度
    model = word2vec.Word2Vec(sentences,size=250, window=5, min_count=5,workers=multiprocessing.cpu_count())
    #保存模型
    model.save("wiki_corpus.model")
    print('save model complete !')
    end = time()
    print('total processing time : {}'.format(begin-end))

if __name__ == "__main__":
    main()
