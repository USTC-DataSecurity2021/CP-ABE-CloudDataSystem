## 测试

性能测试分为两类测试

+ CP-ABE关于属性个数的加解密时间
+ 对称密码关于文件大小的加解密时间



#### CP-ABE加解密时间测试

​		依据从5个属性到100个属性, 5个属性一个步长, 共20组测试集, 对随机生成的Key参数进行加解密测试, 每组测量30次, 取平均值作为每组的测试结果

```py
cd ./Benchmark/CP-ABE
python Test-CP-ABE.py
```



#### 对称密码加解密时间测试

生成特定大小的文件, 可以生成1k, 10k, ..., 至1G以上的文件

```bash
cd ./Benchmark/Symmetry
python file-gen.py
```

测试文件加解密时间

​		分别取1k, 10k, 100k, 1m, 10m, 100m, 以量级为步长, 共6组用户数据进行对称密码算法的加解密时间测试, 每组测量10次取平均值作为测试结果

```bash
python Test-SymmetricCrypto.py
```













