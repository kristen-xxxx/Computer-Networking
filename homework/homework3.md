# 网络及分布式第三次作业

2017302580201-贺谷穗子

### 一、telnet whu.edu.cn 25

Telnet协议是TCP/IP协议族中的一员，是Internet远程登录服务的标准协议和主要方式。在终端使用者的电脑上使用telnet程序，用它连接到服务器。

下面是我使用SMTP协议手工发送邮件的步骤及结果截图：

![homework3-1](homework3-1.jpg)

### 二、telnet maths.whu.edu.cn 80

输入命令：

> telnet maths.whu.edu.cn 80
>
> GET / HTTP/1.1
>
> Host:maths.whu.edu.cn

下面是结果截图：

![homework3-2](homework3-2.jpg)

### 三、课本第二章习题选做两道

> P4.考虑当浏览器发送一个HTTP GET报文时，通过Wireshark俘获到下列ASCII字符串（即这是一个 HTTP GET报文的实际内容）。字符＜ cr＞ ＜lf＞是回车和换行符（即下面文本中的斜体字符串＜ cr〉 表示了单个回车符，该回车符包含在HTTP首部中的相应位置）。回答下列问题，指出你在下面HT TP GET报文中找到答案的地方。
>
> GET /cs453/index html HTTP/1.1<cr><lf>Host: gaia.cs.umass.edu<cr><lf>User-Agent: Mozilla/5.0 ( Windows;U; Windows NT 5.1; en-US; rv:1.7.2) Gecko/20040804 Netscape/7.2 (ax)<cr><lf> Accept:ext/xml, application/xml, application/xhtml+xml, text /html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0 5 <cr><lf>Accept-Language: en-us, en;q=0. 5<cr><lf>AcceptEncoding: zip,deflate<cr><lf>Accept-Charset: ISO-8859-1,utf-8;q=0.7 r*;q=0.7<cr><lf>Keep-Alive: 300 <cr><lf>Connection:keep-alive<cr><lf><cr><lf>
>
> a.由浏览器请求的文档的URL是什么？ 
>
> b. 该浏览器运行的是HTTP的何种版本？
>
>  c. 该浏览器请求的是一条非持续连接还是一条持续连接？ 
>
> d. 该浏览器所运行的主机的IP地址是什么？ 
>
> e. 发起该报文的浏览器的类型是什么？在一个HTTP请求报文中，为什么需要浏览器类型？

a)http://gaia.cs.umass.edu/cs453/index.html

b)HTTP1.1

c)持续连接的

d)看不到

e)Mozilla/5.0。服务器需要浏览器类型信息将同一对象的不同版本发送到不同类型的浏览器。

> P7.假定你在浏览器中点击一条超链接获得Web页面。相关联的URL的IP地址没有缓存在本地主机上, 因此必须使用DNS lookup以获得该IP地址。如果主机从DNS得到IP地址之前已经访问了 n个DNS 服务器；相继产生的RTT依次为RTT|、…、RTT“ 。 进一步假定与链路相关的Web页面只包含一个 对象，即由少量的HTML文本组成。令RTT。表示本地主机和包含对象的服务器之间的RTT值。假定该对象传输时间为零，则从该客户点击该超链接到它接收到该对象需要多长时间？

获取IP地址的总时间为$RTT_1+RTT_2+...+RTT_n$

从该客户点击该超链接到它接收到该对象的总响应时间为$2RTT_O+RTT_1+RTT_2+...+RTT_n$