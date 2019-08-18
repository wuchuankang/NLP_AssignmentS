# 作业流程
- 下载wiki中文语料库
- 使用wikiextracor 来提取并分割语料库
- 用opencc_bat.py 批处理opencc 繁简转换
- 用 parse_wiki.py ，再次用re过滤多余内容并用jieba分词，并使用了哈工大停用词，将文本处理成一篇文章占据一行
- 用 merge_files.py 来批处理来合并 parse_wiki.py 生成的多个文本
- 用 train_word2vec.py 来训练词向量
- 用 find_similar.py 来查找相近的词语并生成词云图
