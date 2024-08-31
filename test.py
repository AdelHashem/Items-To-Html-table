import unittest
from itemstohtml import FilterModule

class TestItemsToHtml(unittest.TestCase):
    def setUp(self):
        self.items = [
            {'hostname': 'machine1', 'dist': 'redhat', 'ip': '192.168.1.50'},
            {'hostname': 'machine2', 'dist': 'debian', 'ip': '192.168.1.51'},
            {'hostname': 'machine3', 'dist': 'ubuntu', 'ip': '192.168.1.52'}
        ]
        self.title = 'Machines report'
    def test_selecting_part_of_keys(self):
        html = FilterModule().items_to_html(self.items, self.title, hostname='Hostname', dist='Distribution')

        self.assertIn('<title>Machines report</title>', html)
        self.assertIn('<th>Hostname</th>', html)
        self.assertIn('<th>Distribution</th>', html)
        self.assertIn('<td>machine1</td>', html)
        self.assertIn('<td>machine2</td>', html)
        self.assertIn('<td>machine3</td>', html)
        self.assertIn('<td>redhat</td>', html)
        self.assertIn('<td>debian</td>', html)
        self.assertIn('<td>ubuntu</td>', html)
        self.assertNotIn('<td>192.168.1.50</td>', html)
        self.assertNotIn('<td>192.168.1.51</td>', html)
        self.assertNotIn('<td>192.168.1.52</td>', html)
    
    def test_selecting_all_keys(self):
        html = FilterModule().items_to_html(self.items, self.title)

        self.assertIn('<title>Machines report</title>', html)
        self.assertIn('<th>hostname</th>', html)
        self.assertIn('<th>dist</th>', html)
        self.assertIn('<td>machine1</td>', html)
        self.assertIn('<td>machine2</td>', html)
        self.assertIn('<td>machine3</td>', html)
        self.assertIn('<td>redhat</td>', html)
        self.assertIn('<td>debian</td>', html)
        self.assertIn('<td>ubuntu</td>', html)
        self.assertIn('<td>192.168.1.50</td>', html)
        self.assertIn('<td>192.168.1.51</td>', html)
        self.assertIn('<td>192.168.1.52</td>', html)

if __name__ == '__main__':
    unittest.main()