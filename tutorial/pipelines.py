# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os
from openpyxl import Workbook

'''
默认
'''
class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

'''
保存为excel表格
'''
class ExcelPipeline(object):

    dir = 'output'
    file = 'doubanMovies_' + time.strftime('%Y-%m-%d',time.localtime()) + '.xlsx'
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['电影', '评分', '海报', '上映时间','国家','导演','主演','投票'])  # 设置表头

    def process_item(self, item, spider):
        line = [item['title'], item['score'], item['pic_url'], item['year'],item['region'],item['director'],item['actors'],item['votecount']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        self.wb.save(self.dir+'/'+self.file)  # 保存xlsx文件
        return item
