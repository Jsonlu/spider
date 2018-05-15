## 说明  
### 安装  
```
pip3 install scrapy
```

### 运行并保存文件
```
#豆瓣电影
scrapy crawl douban -o movice.json
#豆瓣活动
scrapy crawl event -o event.json
#推酷文章列表，需要登录后的cookie
scrapy crawl tuicool -o tuicool.json
#支付宝账单，需要登录后的cookie
scrapy crawl alipay -o alipay.json
#中国支付网信息爬取
scrapy crawl paynews -o paynews.json
#杭州/深圳/天津小汽车摇号信息爬取
scrapy crawl applay -o applayCar.json
#广州小汽车摇号信息爬取
scrapy crawl applyGZ -o applayCar.json
```

### 配置代理地址池
- settings.py  PROXY_IP_POOL = []   
