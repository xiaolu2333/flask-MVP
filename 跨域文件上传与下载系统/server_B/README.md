跨域文件上传与下载系统——ubuntu 文件上传服务器 server_B。

## 1，环境
```bash
$ lsb_release -a  # check ubuntu version
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.1 LTS
Release:	22.04
Codename:	jammy

$ python3 -V      # check python version
Python 3.10.6
```

## 2，安装
```bash
$ pip install -r requirements.txt
```

## 3，配置
```bash
$ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.90.129  netmask 255.255.255.0  broadcast 192.168.90.255
        inet6 fe80::adb4:abb9:d21d:3007  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:1a:76:6d  txqueuelen 1000  (以太网)
        RX packets 12255719  bytes 17508572877 (17.5 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 553818  bytes 39053335 (39.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
文件上传服务器 host=192.168.90.129 port=8000

## 4，运行
```bash
$ flask run
```