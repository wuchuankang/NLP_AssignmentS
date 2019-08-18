'''
合并分词后的文件
'''
import os
def merge_corpus():
    output = open("./wiki_corpus","w",encoding="utf-8")
    input = "./zhwiki200/CC"
    file_list = os.listdir(input)

    for i in range(len(file_list)):
        file_path = os.path.join(input,file_list[i])
        file = open(file_path,"r",encoding="utf-8")
        line = file.readline()
        while line:
            output.writelines(line)
            line = file.readline()
        file.close()
    output.close()

if __name__ == "__main__":
    merge_corpus()
