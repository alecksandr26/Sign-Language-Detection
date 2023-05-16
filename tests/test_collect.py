import unittest
import os

from src.dataset import Collector

DEFAULT_TEST_DATA_DIR = "test_data"
DEFAULT_TEST_AMOUNT_CLASSES = 3
DEFAULT_TEST_AMOUNT_PIC = 100

class TestCollector(unittest.TestCase):
    def setUp(self):
        self.collector = Collector(data_dir = DEFAULT_TEST_DATA_DIR,
                                   amount_classes = DEFAULT_TEST_AMOUNT_CLASSES,
                                   amount_pics = DEFAULT_TEST_AMOUNT_PIC)
        self.collector._create_directory(self.collector.data_dir)
    
    def test_check_dir_created(self):
        assert self.collector.data_dir == DEFAULT_TEST_DATA_DIR
        assert os.path.exists(self.collector.data_dir)

    def test_alphabet(self):
        pass

    def test_recollection_of_data(self):
        assert self.collector.amount_classes == DEFAULT_TEST_AMOUNT_CLASSES
        assert self.collector.amount_pics == DEFAULT_TEST_AMOUNT_PIC

        # Start the collection pics
        self.collector.start()



        
    def tearDown(self):
        self.collector.del_data()


