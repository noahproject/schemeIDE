import unittest
import tkinter as tk
import tkinter.messagebox as MBox
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
        self.root = tk.Tk()
        self.editor = SchemeText(self.root)
        self.gui_test_result = True

    def _spawn(self):
        '''
        Asks the user to verify editor GUI functionality. Sets switch if a failure occurs.
        At the end, destroys the editor stub which is in the mainloop by the time this 
        method is called.
        '''

        result = MBox.askquestion('Test Highlight Pattern', 'Is lambda highlighted?')
        if result == 'no': self.gui_test_result = False
        self.root.destroy()
		
    def test_highlight_pattern(self):
        self.editor.insert('end', 'Look at this code: (+ (lambda other stuff)')
        self.editor.highlight_pattern('lambda', 'red')
        self.editor.after(1000, self._spawn)
        self.editor.mainloop()
        self.assertTrue(self.gui_test_result, 'Lambda is not highlighted.')

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSchemeIDE)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSchemeText)
    full_suite = unittest.TestSuite([suite1, suite2])
    #TODO: When tk.Tk() is started in suite1, it breaks suite2.
    #unittest.TextTestRunner(verbosity=2).run(suite1)
    unittest.TextTestRunner(verbosity=2).run(suite2)

