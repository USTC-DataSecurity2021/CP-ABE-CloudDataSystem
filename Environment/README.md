## charm-crypto环境安装流程

##### 系统

+ Ubuntu16.04
+ Ubuntu18.04
+ Ubuntu20.04

##### python版本

+ python3.7

+ python3.8

##### 依赖环境

+ gmp-6.1.2

+ pbc-0.5.14

+ openssl-1.0.2

+ pythonlib - pyparsing



解压缩4个安装包

+ charm-dev.zip

+ gmp-6.1.2.tar.bz2

+ openssl-1.0.2s.tar.gz

+ pbc-0.5.14.tar.gz

  

分别执行以下命令进行安装

#### python

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update 
sudo apt install python3.7
python3.7 --version

sudo rm /usr/bin/python 
sudo rm /usr/bin/python3 
sudo ln -s /usr/bin/python3.7 /usr/bin/python
sudo apt-get install python3.7-dev # 必须装, 否则会提示没有python.h

# install pip for python3.7 通用方法
sudo apt-get install curl
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo apt install python3.7-distutils
python get-pip.py

echo 'export PATH=$PATH:/home/falca/.local/bin' >>~/.bashrc
source ~/.bashrc

```



#### Pyparsing

```bash
sudo apt-get update 
python -m pip install pyparsing
```



#### GMP

```bash
sudo apt-get update
sudo apt-get install flex bison
./configure
# sudo apt install make
make
sudo make install

make check # 最后再查看是否全部安装正确
```



#### PBC

```bash
./configure
make
sudo make install

make check #查看是否正确
```



#### OpenSSL

系统自带OpenSSL可以不需要安装, 如果后续安装提示OpenSSL出错, 需要执行以下过程安装更新版本

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt install build-essential checkinstall zlib1g-dev -y
cd /usr/local/src/
sudo wget https://www.openssl.org/source/openssl-1.1.1c.tar.gz
sudo tar -xf openssl-1.1.1c.tar.gz
cd openssl-1.1.1c
sudo ./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib
sudo make
sudo make test
sudo make install
cd /etc/ld.so.conf.d/
sudo nano openssl-1.1.1c.conf
# 填入以下内容, 不包括######
############
/usr/local/ssl/lib
############
# ctrl + o保存, ctrl + x退出

sudo ldconfig -v
sudo mv /usr/bin/c_rehash /usr/bin/c_rehash.backup
sudo mv /usr/bin/openssl /usr/bin/openssl.backup
sudo nano /etc/environment
# 在PATH之后添加以下内容, 不包括######, 直接覆盖原内容也可, 如果不是原型机环境就注意环境变量的差异
################
# PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
":/usr/local/ssl/bin"
################

source /etc/environment
echo $PATH

which openssl
openssl version -a
```



#### Charm-crypto

```bash
# 此时是默认python3.7进行安装操作
./configure.sh
sudo make install
```



具体安装流程可参考我的个人博客

https://blog.csdn.net/qq_33976344/article/details/115383904