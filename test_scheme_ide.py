import unittest
import tkinter as tk
from scheme_ide import *

class TestSchemeIDE(unittest.TestCase):
    
    def setUp(self):
        root = tk.Tk()
        self.app = SchemeIDE(master=root)

    def test_run_code(self):
        #Currenty fails because evaluator is not implemented.
        self.app.editor.insert('end', "(+ 2 2)")
        self.app.run_code()
        self.assertEqual('4', self.app.console.get('1.3', '1.4'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSchemeIDE)
    unittest.TextTestRunner(verbosity=2).run(suite)
