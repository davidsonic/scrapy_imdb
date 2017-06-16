# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    photo = Field()
    id = Field()
    name = Field()
    year = Field()
    people = Field()
    topic = Field()
    born = Field()
    sex = Field()
    star = Field()
    hash = Field()

