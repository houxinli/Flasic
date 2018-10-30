运行方法（Windows）
下载之后，假设项目文件夹路径为D:/Flasic

在当前目录运行命令行

D:/Flasic> 
在当前目录输入命令
D:/Flasic> venv\Scripts\activate
以激活虚拟环境

进入虚拟环境后
输入 python crawler.py
(在crawler.py 第143行可以更改所需的网易云音乐歌单列表)
将会在本地下载歌曲

若无报错信息
正常下载完成之后会显示
下载完成! 本次共下载：xx首歌曲

下载完成后，输入 python flasic.py

命令行中最后一行显示
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
说明运行成功

在浏览器中输入localhost:5000进入网页

参考https://dormousehole.readthedocs.io/en/latest/installation.html#installation
