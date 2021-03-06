from unittest import mock

from django.test import Client
from django.test import TestCase

from mainapp.tests.live.helper import MockMainappSearch


class TestRSS(TestCase):
    fixtures = ['initdata']
    c = Client()

    def test_paper_feed(self):
        response = self.c.get('/paper/feed/').content.decode('utf-8').strip()
        self.assertIn('<rss', response)
        self.assertIn('Latest papers', response)
        self.assertIn('&lt;a href="/file/5/"&gt;Some obligatory cat content.&lt;/a&gt;', response)
        self.assertIn('Frank Underwood', response)

    @mock.patch("mainapp.functions.search_tools.MainappSearch.execute",
                new=MockMainappSearch.execute)
    def test_search_results(self):
        response = self.c.get('/search/query/complexity/feed/').content.decode('utf-8').strip()
        self.assertIn('<rss', response)
        self.assertIn('The latest search results', response)
        self.assertIn('File: Title', response)
        self.assertNotIn('Frank Underwood', response)
