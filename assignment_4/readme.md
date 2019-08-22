# 作业流程
- 下载wiki中文语料库
- 使用wikiextracor 来提取并分割语料库
- 用opencc_bat.py 批处理opencc 繁简转换
- 用 parse_wiki.py ，再次用re过滤多余内容并用jieba分词，并使用了哈工大停用词，将文本处理成一篇文章占据一行
- 用 merge_files.py 来批处理来合并 parse_wiki.py 生成的多个文本
- 用 train_word2vec.py 来训练词向量
- 用 find_similar.py 来查找相近的词语并生成词云图
- 添加较小的语料库 ，进行增量训练，训练出的模型 enhance_model 效果更差了，就以 ‘说‘ 相近的词，不靠谱了。
- 增加了1.5G 的搜狐新闻语料库 news_tensite_xml.dat，没用增量训练，和 wiki_corpus 一起训练，训练模型为 sohu_wiki_model, 效果要比单独的 wiki_corpus 训练出的模型 wiki_corpus.model 要好

