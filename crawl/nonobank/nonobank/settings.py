# -*- coding: utf-8 -*-

# Scrapy settings for nonobank project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'nonobank'

SPIDER_MODULES = ['nonobank.spiders']
NEWSPIDER_MODULE = 'nonobank.spiders'
ITEM_PIPELINES={
    'nonobank.pipelines.NonobankPipeline':400,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tianyan (+http://www.yourdomain.com)'