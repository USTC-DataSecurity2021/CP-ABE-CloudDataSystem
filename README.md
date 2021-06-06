# CP-ABE-CloudDataSystem
2021-USTC-信息安全作品赛数据安全CP-ABE云数据系统项目, 基于CP-ABE方案实现安全的数据存储和访问服务的数据系统.



## 使用说明



### 环境

+ 系统: linux (于ubuntu20.0.4上测试通过)

+ python == 3.7
  + charm-crypt
+ php > 7 + apache2

> 注：关于charm-cryto的安装，详见 https://blog.csdn.net/qq_33976344/article/details/115383904





### setup

+ apache使用默认目录/var/www/html，目录需有完全读入读写权限(chmod 777)

+ 将html下文件复制至/var/www/html下
+ 启动apache2 ( service apache2 start)
+ 将解密脚本(decrypt.py)下载至本地






### 使用

#### 注册

+ 输入用户名,密码,学校,身份
+ 复制返回的pk,sk并保存至本地文件中

+ 将解密脚本中下面两项换成pk, sk的路径。

~~~python
pk_path = 'your pk path'
sk_path = 'your sk path'
~~~



#### 登陆

+ 输入用户名密码登陆



#### 下载

+ 点击右侧的下载按钮下载文件
+ 用本地的解密脚本解密，解密方式:

~~~shell
python decript.py <cfile>
~~~



#### 上传

+ 通过界面上方的"选择文件"选择要上传的文件。
+ 通过"访问结构"输入指定的访问结构(括号分隔，使用and 或 or 连接)。

>  e.g :  ((A and B) and (C or D))

+ 点击 Submit上传。

  





