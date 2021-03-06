import csv
import re
from seo.items import SeoItem, ExpectedSeo

class SeoVerifyPipeline(object):

	expected_seos = {}

	def __init__(self):
		reader = csv.reader(open("/Users/kplu/workspace/casa/iam-ba/seo/seo/csv/#353.csv"), delimiter=";")
		for url,title,h1,desc in reader:
			seo = ExpectedSeo(url, title, h1, desc)
			self.expected_seos[str(url)] = seo

	def process_item(self, item, spider):
		parsed_title = item["title"]
		parsed_h1 = item["h1"]
		# if item["desc"]:
		# 	parsed_desc = item["desc"]

		expected_title = self.expected_seos[item["url"]].title
		expected_h1 = self.expected_seos[item["url"]].h1
		expected_desc = self.expected_seos[item["url"]].desc

		if parsed_title != expected_title:
			print "title parsed: " + item["title"] + "."
			print "title expected: " + expected_title + "."
			print "title wrong url: " + item["url"]
		elif parsed_h1 != expected_h1:
			print "h1 parsed: " + item["h1"] + "."
			print "h1 expected: " + expected_h1 + "."
			print "h1 wrong url: " + item["url"]
		else:
			print "equals."

		return item