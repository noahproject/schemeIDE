import unittest
import tkinter as tk
import tkinter.messagebox as MBox
from scheme_ide import *
import time
		
class TestSchemeIDE(unittest.TestCase):
	
    def setUp(self):
        self.root = tk.Tk()
        self.app = SchemeIDE(master=self.root)

    def _verify(self, name, question):
        '''
        Asks the user to verify editor GUI functionality. Sets switch if a failure occurs.
        At the end, destroys the editor stub which is in the mainloop by the time this 
        method is called.
        '''
        self.gui_test_result = True
        result = MBox.askquestion(name, question)
        if result == 'no': self.gui_test_result = False
        self.root.destroy()

    def _key(self, event, title, msg):   
        if event.char == '+':
            self.app.editor.insert('end', '+')
            self._verify(title, msg)
    
    def _kill(self):
        self.root.destroy()
    
    def test_run_code(self):
        #Currently fails because evaluator is not implemented.
        self.app.editor.insert('end', "(+ 2 2)")
        self.app.run_code()
        result = self.app.console.get("2.3", "end")
        self.app.after(1, self._kill)
        self.app.mainloop()
        self.assertEqual(result, '4', 'Console did not output 4.')
		
    def test_highlight_lambda(self):
        self.app.editor.insert('end', 'Look at this code: (+ (lambda other stuff)')
        self.app.editor.highlight_pattern('lambda', 'red')
        self.app.after(1000, self._verify, "Test Lambda Highlight", "Is lambda highlighted?")
        self.app.mainloop()
        self.assertTrue(self.gui_test_result, 'Lambda is not highlighted.')

    def test_delayed_highlight(self):
        self.app.editor.insert('end', "Type '+': ")
        self.app.editor.bind("<Key>", lambda event: self._key(event, "Test Delayed Highlight", "Is '+' highlighted?"))
        self.app.mainloop()
        self.assertTrue(self.gui_test_result, 'Highlight does not occur on completion.')

    def test_double_arrow(self):       
        self.app.editor.insert('end', "2+2")
        self.app.run_code()
        output = self.app.console.get("1.0", "end")
        self.app.after(1, self._kill)
        self.app.mainloop()
        self.assertEqual(output, "-> \n Error!\n-> ", 'Invalid code breaks console format.')

		
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSchemeIDE)
    unittest.TextTestRunner(verbosity=2).run(suite)

