import unittest
import os

from src.dataset import Collector

DEFAULT_TEST_DATA_DIR = "test_data"

class TestCollector(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_simple_build_collector(self):
        collector = Collector(data_dir = DEFAULT_TEST_DATA_DIR)
        assert collector.data_dir == DEFAULT_TEST_DATA_DIR

    def test_check_dir_created(self):
        pass
        
    def tearDown(self):
        pass


