from nbimporter import NotebookLoader
loader = NotebookLoader()
tes = loader.load_module("func")

import unittest

class TestNotebook(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(tes.add(2, 3), 'eeeee')
        
unittest.main(argv=[''], verbosity=2, exit=False)



