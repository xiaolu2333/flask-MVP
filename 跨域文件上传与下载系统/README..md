跨域文件上传与下载系统——仅用于测试跨域文件传输。

```
                      下载
windows文件下载服务器 --------> windows客户端
            |                          |
            |下载                       | 上传
            v                          v
            ----> ubuntu客户端 -----> ubuntu文件上传服务器
                               上传
```

文件上传部分基于这篇文章 [Python实现大文件分片上传](https://blog.csdn.net/jinixin/article/details/77545140) 提供的思路。
