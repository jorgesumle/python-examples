#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest, os, threading
from app.crawler import Crawler
 
class TddCrawler(unittest.TestCase):
    def test_crawler_downloadInit_method_returns_correct_result(self):
        c = Crawler("http://www.gnu.org")
        self.assertEqual(c.url, "http://www.gnu.org")
        self.assertEqual(c.title, "The GNU Operating System and the Free Software Movement")        

    def test_crawler_downloadOneUrl_method_returns_correct_result(self):
        c = Crawler("http://www.urjc.es")
        c.downloadOneUrl("urjc.html")
        self.assertEqual(os.path.exists("urjc.html"), True)

    def test_crawler_downloadOneUrlThread_method_returns_correct_result(self):
        c = Crawler("http://www.elpais.es")
        c.downloadOneUrlThread("elpais.html")
        self.assertEqual(os.path.exists("elpais.html"), True)
            
        
if __name__ == '__main__':
    unittest.main()
