import re
import jieba
import logging


def get_stopwords():
    stopwords = set()
    with open('/home/wck/Repos/NLP_AssignmentS/assignment_4/哈工大停用词表.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.add(line.strip('\n'))
    return stopwords

def read_sohu(input_path, save_path):
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
    pattern = re.compile('^<content>(.*)</content>')
    save = open(save_path, 'w', encoding='utf-8')
    stopwords = get_stopwords()
    with open(input_path, 'r',encoding='gb18030') as f:
        all_lines = f.readlines()
        print(len(all_lines))
        for line in all_lines:
            content = ''
            match_content = pattern.findall(line)
            if len(match_content)>0:
                match_content  = match_content[0].strip('\n').strip(' ')
                match_content = jieba.cut(match_content)
                for word in match_content:
                    if word not in stopwords:
                        content += word+' '
                save.write(content+'\n')
    save.close()

if __name__=='__main__':

    input_path = './news_tensite_xml.dat'
    save_path = './save_sohu_nes_cut.txt'
    read_sohu(input_path, save_path)



