## 说明  
### 安装  
```
pip3 install scrapy
```

### 运行并保存文件
```
#豆瓣电影
scrapy crawl douban -o movice.json -s FEED_EXPORT_ENCODING=utf-8
#豆瓣活动
scrapy crawl event -o event.json -s FEED_EXPORT_ENCODING=utf-8
#推酷文章列表
scrapy crawl tuicool -o tuicool.json -s FEED_EXPORT_ENCODING=utf-8
#支付宝账单
scrapy crawl alipay -o tuicool.json -s FEED_EXPORT_ENCODING=utf-8
```

### 配置代理地址池
- settings.py  PROXY_IP_POOL = []   
