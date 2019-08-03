import logging
from gensim.models import word2vec
import multiprocessing

def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    sentences = word2vec.LineSentence("wiki_corpus")
    # size：单词向量的维度
    model = word2vec.Word2Vec(sentences,size=250, window=5, min_count=5,workers=multiprocessing.cpu_count())
    #保存模型
    model.save("wiki_corpus.model")

if __name__ == "__main__":
    main()
