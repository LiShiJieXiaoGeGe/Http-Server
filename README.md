# Http-Server
### 纯c语言实现的基于Linux的轻量级多线程Web服务器，应用层实现了一个简单的HTTP服务器，支持静态资源访问与动态消息回显。

### 特点：1、实现快速地址再分配，避免紧急情况下服务器因宕机而引起的服务失效；
###       2、实现get/post两种请求解析，采用cgi脚本进行post请求响应；
###       3、利用多线程机制提供服务，增加并行服务数量；
###       4、利用双管道进行不同进程间通信与数据交换，及时关闭无用管道。

