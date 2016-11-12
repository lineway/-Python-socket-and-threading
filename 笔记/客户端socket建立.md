# 客户端socket建立

## socket的异常
### 异常类型：
  - `error`：套接字或与地址有关的错误
  - `herror`: error的子类，表示发生与地址有关的错误
  - `gaierror`: `getaddressinfo()`或`gethostinfo()`函数中与地址有关的错误
  - `timeout`: 套接字超时错误(仅在设置超时的时候出现)

**他们都是内置异常类OSError的子类**

### 处理异常：
  - try语句
  - 单独处理每种异常
  - **except语句截获异常时，如果各个异常之间具有继承关系，则子类应该写在前面**
  - 要求不高时，可以直接捕获`socket.error`异常进行相关处理
