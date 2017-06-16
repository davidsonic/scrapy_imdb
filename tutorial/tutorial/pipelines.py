# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from tutorial.items import TutorialItem
from scrapy.http import Request
from slugify import slugify
import os, os.path
from scrapy.utils.project import get_project_settings
from scrapy.contrib.pipeline.images import ImagesPipeline
import spiders.crawler as sp
import subprocess


class TutorialPipeline(object):
    def __init__(self):
        addj=sp.DmozSpider.add_j
        self.file = open(add_j, 'wb') #modify 1

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode("unicode_escape"))
        #subprocess.Popen(cp_add , shell=True)
        return item

class imagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['photo']
        print image_url
        yield Request(image_url.replace("[u'",""))

    def item_completed(self, results, item, info):
        for result in [x for ok, x in results if ok]:
            path = result['path']
            slug = slugify(item['id'])
            #item['hash'] = path.replace('full/','')

            settings = get_project_settings()
            storage = settings.get('IMAGES_STORE')

            #print path.replace('full/','')
            #item['hash'] = path.replace('full/','')
            target_path = os.path.join(storage, slug, os.path.basename(path))
            path = os.path.join(storage, path)

            # If path doesn't exist, it will be created
            if not os.path.exists(os.path.join(storage, slug)):
                os.makedirs(os.path.join(storage, slug))


            if not os.rename(path, target_path):
                raise TutorialItem("Could not move image to target folder")
        if self.IMAGES_RESULT_FIELD in item.fields:
            item[self.IMAGES_RESULT_FIELD] = [x for ok, x in results if ok]
        return item
