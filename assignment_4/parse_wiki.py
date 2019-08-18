import logging
import jieba
import re
import os


def get_stopwords():
    stopwords = set()
    with open('哈工大停用词表.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.add(line.strip('\n'))
    return stopwords

def parse_zhwiki(read_file_path, save_file_path):

    pattern_1 = re.compile('^<doc.*>')
    pattern_2 = re.compile('^</doc>')

    input = open('read_file_path', 'r', encoding='utf-8')
    output = open('save_file_path', 'w+', encoding='utf-8')

    stopwords = get_stopwords()

    article_content = ''
    line = input.readline()

    match_flag = 0      #用于去掉<doc ...>后面一行的标题
    while line:
        match_obj = pattern_1.match(line)
        line = pattern_1.sub('', line)
        line = pattern_2.sub('', line)
        line = line.strip('\n')

        if match_obj:
            match_flag = 1
            if len(article_content)>0:
                output.write(article_content+'\n')
                article_content = ''    #恢复为空，用于存储下一篇文章

        if len(line)>0:
            if match_flag:
                match_flag = 0
            else:
                words = jieba.cut(line)
                for word in words:
                    if word not in stopwords:
                        article_content += word + ' '
        line = input.readline()
    output.write(article_content)   #读取最后一篇文章

    input.close()
    input.close()
if __name__=='__main__':
    input_path = './zhwiki200/BB'
    out_path = './zhwiki200/CC'
    file_list = os.listdir(input_path)
    for i in range(len(file_list)):
        read_file_path = os.path.join(input_path, file_list[i])
        save_file_path = os.path.join(out_path, file_list[i]+'_jieba')
        parse_zhwiki(read_file_path, save_file_path)
    



