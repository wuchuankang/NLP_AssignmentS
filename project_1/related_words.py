from collections import defaultdict
from gensim.models import Word2Vec


def get_related_words(initial_words, model):
    """get_related_words : 得到与输入的initial_words相近的至少500个词语

    :param initial_words: 要找相近词的对象，比如找 说 的相近单词，initial_words=['说']
    :param model: 是训练好的词向量
    """
    seen_words = defaultdict(int)   #已经找到的单词
    max_seen_words = 500    # 设置要找相近单词的个数
    # 待查询的单词
    unseen_words = initial_words
    # 当带查询单词已经查询完毕或者已经找到超过500 个单词，则终止
    while unseen_words and len(seen_words)<2000:
        if len(seen_words) % 100 == 0:
            print('the number of related words : {}'.format(len(seen_words)))

        seen_word = unseen_words.pop(0)
        extend_words = [w for w, i in model.most_similar(seen_word, topn=20)]
        for word in extend_words:
           # 将查询完毕的单词添加到字典中，字典的值是查询到的单词的频率
            seen_words[word] += 1
            if word not in seen_word:
                unseen_words.append(word) 

    return seen_words

if __name__=='__main__':
    model = Word2Vec.load('./sohu_wiki_model')
    related_words = get_related_words(['说','表示'], model)
    print(related_words)






