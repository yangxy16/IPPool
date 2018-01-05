## 开发初衷
```
    别人的设计太复杂，还有坑，还不注意细节，已经失去了撸Python的兴趣  
```  

## 环境
* Require Python >= 3.6.0
* pip install beautifulsoup4
* pip install requests
* pip install pymysql
* pip install lxml

```
windows平台下请先安装Tools文件夹下面的pywin32模块
MySQL用的5.7版本，表结构查看Tools目录下的ippool.sql，直接导入即可，具体配置请查看Lib/Config.py  
```  
  
## HTTP接口
```
    ①http://127.0.0.1:8080/getip/
    ②http://127.0.0.1:8080/delip/?hash=****
```
  
## 引擎启动
* python Http.py
* 修改IPPool_Crawler.xml、IPPool_DBChecker.xml里面的路径、用户等信息，运行wintask.bat创建定时任务