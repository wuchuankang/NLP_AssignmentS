import os

filepath = './zhwiki200/AA'
filepath_save = './zhwiki200/BB'
filelist = os.listdir(filepath)

for i in range(len(filelist)):
    path =os.path.join(filepath, filelist[i])
    save_path = os.path.join(filepath_save, filelist[i]+'_s')
    command = '/usr/bin/opencc' + ' '+ '-i'+' ' + path + ' '+ '-o'+' ' + save_path+ ' '+ '-c'+' ' + 't2s.json'
    os.system(command)
