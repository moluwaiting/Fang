# ubuntu SVN
- [Reference](https://blog.csdn.net/sinat_34322082/article/details/80310751)

- 一.安装
```shell
apt-get install subversion
```
- 二.基本命令

1.选择好自己的文件夹，将文件更新到本地： svn checkout path
```shell
svn checkout svn://tech-gennesisi.club/underwater 
```
首次登录时需要输入密码。

注意：此时会在/home/usr目录下生成underwater文件夹，即是svn目录。其中，usr为个人电脑名称，如lanrf11,则svn文件夹为/home/lanrf11/underwater。

2.添加新文件： svn add file
eg:
在/home/lanrf11/underwater路径下：svn add lanrf/1

在/home/lanrf11/underwater/lanrf11路径下：svn add 2
注意：如出现——svn: E155007: “/home/lanrf11”不是工作副本，则可能是路径问题。



3.上传：svn commit -m “LogMessage“ [-N] [--no-unlock] PATH
```shell
svn commit -m "添加" *.*
```
