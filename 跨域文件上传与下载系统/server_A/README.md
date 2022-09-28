跨域文件上传与下载系统——windows 文件下载服务器。

## 1，环境
```bash
> msinfo32    # 查看windows系统信息

> python -V   # 查看python版本
Python 3.9.12
```

## 2，安装
```bash
> pip install -r requirements.txt
```

## 3，配置
```bash
> ipconfig

Windows IP 配置                                                      
以太网适配器 以太网:                                                                                                          
   连接特定的 DNS 后缀 . . . . . . . :                             
   本地链接 IPv6 地址. . . . . . . . : fe80::41bc:5314:****:****%**
   IPv4 地址 . . . . . . . . . . . . : 172.28.79.101  为本机IP
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . : 172.28.79.254
```
文件下载服务器 host=本机IP port=8000

## 4，运行
```bash
> flask run
```