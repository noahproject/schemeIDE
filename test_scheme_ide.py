import unittest
import tkinter as tk
import tkinter.messagebox as MBox
from scheme_ide import *
		
class TestSchemeIDE(unittest.TestCase):
	
    def setUp(self):
        self.root = tk.Tk()
        self.app = SchemeIDE(master=self.root)
        self.gui_test_result = True

    def _verify(self, name, question):
        '''
        Asks the user to verify editor GUI functionality. Sets switch if a failure occurs.
        At the end, destroys the editor stub which is in the mainloop by the time this 
        method is called.
        '''

        result = MBox.askquestion(name, question)
        if result == 'no': self.gui_test_result = False
        self.root.destroy()
		
    def test_run_code(self):
        #Currently fails because evaluator is not implemented.
        self.app.editor.insert('end', "(+ 2 2)")
        self.app.run_code()
        self.app.after(1000, self._verify, "Test Console Output", "Is there a 4 in the console?")
        self.app.mainloop()
        self.assertTrue(self.gui_test_result, 'Console did not output 4.')
		
    def test_highlight_pattern(self):
        self.app.editor.insert('end', 'Look at this code: (+ (lambda other stuff)')
        self.app.editor.highlight_pattern('lambda', 'red')
        self.app.after(1000, self._verify, "Test Highlight", "Is lambda highlighted?")
        self.app.mainloop()
        self.assertTrue(self.gui_test_result, 'Lambda is not highlighted.')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSchemeIDE)
    unittest.TextTestRunner(verbosity=2).run(suite)

