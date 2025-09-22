# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class ScrapeadvisorPipeline:
    def open_spider(self, spider):
        self.file = None
        self.writer = None
        self.output_file = getattr(spider, 'output_file', None)
        self.fieldnames = ['url', 'status_code', 'antibot', 'check_field']
        if self.output_file:
            self.file = open(self.output_file, 'w', newline='', encoding='utf-8')
            self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
            self.writer.writeheader()

    def close_spider(self, spider):
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        if self.writer:
            self.writer.writerow({
                'url': item.get('url', ''),
                'status_code': item.get('status_code', ''),
                'antibot': item.get('antibot', ''),
                'check_field': item.get('check_field', '')
            })
        return item
