import unittest
import tkinter as tk
from scheme_ide import *

class TestSchemeIDE(unittest.TestCase):
    
    def setUp(self):
        root = tk.Tk()
        self.app = SchemeIDE(master=root)

    def test_run_code(self):
        #Currently fails because evaluator is not implemented.
        self.app.editor.insert('end', "(+ 2 2)")
        self.app.run_code()
        self.assertEqual('4', self.app.console.get('1.3', '1.4'))
		
class TestSchemeText(unittest.TestCase):
	
	def setUp(self):
        root = tk.Tk()
        self.editor = SchemeText(root)
		
	def test_highlight_pattern(self):
		self.editor.highlight_pattern("lambda", "blue")
		#TODO: Generate Popup asking if text appears to be blue.

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSchemeIDE)
    unittest.TextTestRunner(verbosity=2).run(suite)
