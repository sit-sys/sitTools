## README

### sitTools
###### 適用 Python 版本
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sitTools)](https://pypi.python.org/pypi/sitTools/)

Useful tools module for S.I.T. project use.
本公司勝和科技 ( Success Integration Technology ) 內部專案常用函式集

### Installation ( 安裝套件 )
```bash
pip install sitTools
```

### Dependencies ( 相依套件 )
- numpy
- pandas
- smtplib
- configparser

### Module & Function

#### gTools

#### cTools

`r_get(url, header, param, times, sec)`   
  
  HTTP GET request function.  
  You can define fail retry times and wait sec. by yourself.  
  Default retry request 3 times, wait 5 second between 2 requests.  
  可自訂 HTTP GET 請求異常重試次數與等待秒數的函式  
  預設重試 3 次請求, 每次請求間等待 5 秒
  
  Example:
  ```python
  ctool = tools.cTools()
  url = 'http://www.gotest.com'
  head = {}
  par = {}
  
  ctool.r_get(url, head, par)
  ```
  
  Result:
  ```
  2023-07-25 23:00:24 Connect to http://www.gotest.com err, retry after 5 sec...
  2023-07-25 23:00:37 Connect to http://www.gotest.com err, retry after 5 sec...
  2023-07-25 23:00:50 Connect to http://www.gotest.com err, retry after 5 sec...
  ```
