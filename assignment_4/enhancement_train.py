"""
在 ./wiki_corpus.model 基础上，添加 ./final-news-sentences-cut.txt 语料库，继续训练
"""
import os
from gensim.models.word2vec  import Word2Vec

def enhancement_train(new_corpus):
    if os.path.exists('./wiki_corpus.model') and os.path.isfile('./wiki_corpus.model'):
        model = Word2Vec.load('./wiki_corpus.model')
        model.build_vocab(new_corpus, update=True)
        model.train(new_corpus, total_examples=len(new_corpus), epochs=model.iter)
        model.save('./enhance_model')

    else:
        print("cann't enhance train, without the base model")

if __name__=='__main__':
    with open('./final-news-sentences-cut.txt','r',encoding='utf-8') as f:
        new_corpus = f.readlines()
        

    enhancement_train(new_corpus)




