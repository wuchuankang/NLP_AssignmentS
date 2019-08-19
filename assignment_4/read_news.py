
# 将news-sentence-cut.txt 去除停用词

def get_stopwords():
    stopwords = set()
    with open('./哈工大停用词表.txt', 'r', encoding='utf-8') as f:
        for word in f:
            stopwords.add(word.strip('\n'))
    return stopwords


def del_stopwords(read_path, save_path):
    save = open(save_path, 'w', encoding='utf-8')
    stopwords = get_stopwords()
    with open(read_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            article = ''
            line = line.strip('\n').split(' ')
            for word in line:
                if word not in stopwords:
                    article += word+' '
            save.write(article+'\n')
            line = f.readline()
            
    save.close()

if __name__=='__main__':
    read_path = 'news-sentences-cut.txt'
    save_path = './final-news-sentences-cut.txt'
    del_stopwords(read_path, save_path)
    with open(save_path,'r',encoding='utf-8') as f:
        print(f.readline())
        
