import os
import random
from time import *

def genSizeFile(fileName, fileSize):
    #file path
    filePath="Data"+fileName+".txt"

    # 生成固定大小的文件
    # date size
    ds=0
    with open(filePath, "w", encoding="utf8") as f:
        while ds<fileSize:
            f.write(str(round(random.uniform(-1000, 1000),2)))
            f.write("\n")
            ds=os.path.getsize(filePath)
    # print(os.path.getsize(filePath))

# start here.
start_time = time()
genSizeFile("1k",1*1024)
end_time = time()
print(end_time - start_time)

start_time = time()
genSizeFile("10k",10*1024)
end_time = time()
print(end_time - start_time)

start_time = time()
genSizeFile("100k",100*1024)
end_time = time()
print(end_time - start_time)

start_time = time()
genSizeFile("1m",1024*1024)
end_time = time()
print(end_time - start_time)

start_time = time()
genSizeFile("10m",10*1024*1024)
end_time = time()
print(end_time - start_time)

start_time = time()
genSizeFile("100m",100*1024*1024)
end_time = time()
print(end_time - start_time)

start_time = time()
genSizeFile("1g",1024*1024*1024)
end_time = time()
print(end_time - start_time)