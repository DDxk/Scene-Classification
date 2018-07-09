#coding: utf-8
import os
import shutil
file = open('list.txt')
lines = file.readlines()
#print(lines)
print('======start======')
path = 'train/'
for line in lines:
    line = line.strip('\n') #去掉换行符
    temp = line.split(',')
    # print(line)
    # print(temp)
    isExists = os.path.exists(path + str(temp[1]))
    if not isExists:
         os.mkdir(path + str(temp[1]))
    srcfile = 'data/' + str(temp[0]) + '.jpg'
    dstfile = path + str(temp[1])
    #shutil.move(srcfile, dstfile)
    shutil.copy(srcfile, dstfile)

file.close()
print('======done======')
