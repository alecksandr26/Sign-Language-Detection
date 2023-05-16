import unittest
import os
import sys

from src.dataset import Collector

DEFAULT_TEST_DATA_DIR = "test_data"
DEFAULT_TEST_AMOUNT_CLASSES = 3
DEFAULT_TEST_AMOUNT_PIC = 100
DEFAULT_TEST_DEVICE = 0

class TestCollector(unittest.TestCase):
    def setUp(self):
        self.collector = Collector(data_dir = DEFAULT_TEST_DATA_DIR,
                                   amount_classes = DEFAULT_TEST_AMOUNT_CLASSES,
                                   amount_pics = DEFAULT_TEST_AMOUNT_PIC,
                                   device = DEFAULT_TEST_DEVICE)
        self.collector._create_directory(self.collector.data_dir)

        # Shutdown the stdout
        self.old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
    
    def test_check_dir_created(self):
        assert self.collector.data_dir == DEFAULT_TEST_DATA_DIR
        assert os.path.exists(self.collector.data_dir)

    def test_cam_connection(self):
        # Start the cammera
        self.collector._initialize_device()
        assert self.collector.cam.isOpened()
        self.collector._shutdown_device()
        

    def test_recollection_of_data(self):
        assert self.collector.amount_classes == DEFAULT_TEST_AMOUNT_CLASSES
        assert self.collector.amount_pics == DEFAULT_TEST_AMOUNT_PIC

        # Start the collection pics
        self.collector.start()

        # Check the genereated directories
        count = 0
        for root_dir, cur_dir, files in os.walk(os.path.join(self.collector.data_dir)):
            count += len(files)
        assert count == DEFAULT_TEST_AMOUNT_PIC * DEFAULT_TEST_AMOUNT_CLASSES
        
        
    def tearDown(self):
        self.collector.del_data()
        sys.stdout.close()
        sys.stdout = self.old_stdout


