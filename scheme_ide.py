import tkinter as tk
from subprocess import Popen, PIPE

class SchemeIDE(tk.Frame):
    '''
    Scheme IDE

    This is the main application window.   
    IMPORTANT: Currently only runs Python code for demo purposes.
    '''

    def __init__(self, master=None):
        '''Creates the application and its widgets.'''
        tk.Frame.__init__(self, master)
        master.minsize(width=300, height=300)
        self.create_toolbar(master)
        self.create_editor(master)
        self.create_console(master)

    def create_toolbar(self, r):
        '''Creates a run button that will execute code in the editor.'''
        self.runButton = tk.Button(r, text='Run', command=self.run_code)
        self.runButton.pack()

    def create_editor(self, r):
        '''Creates a text box that a user can type code into.'''
        self.editor = tk.Text(r,height=20,width=60,bg='black',fg='white', \
                         insertbackground='blue')
        self.editor.pack()

    def create_console(self, r):
        '''Creates a console for program output.'''
        self.console = tk.Text(r,height=10,width=60,bg='black',fg='white')
        self.console.insert(tk.END, '-> ');
        self.console.config(state=tk.DISABLED)
        self.console.pack()

    def run_code(self):
        '''Runs (python) code from editor and displays stdout in console.'''
        f = open('output.py', 'w')
        f.write(self.editor.get("1.0", tk.END))
        f.close()
        #TODO: Change to Scheme evaluator.
        p = Popen(['python', 'output.py'], stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, output)
        self.console.insert(tk.END, '-> ')
        self.console.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Scheme IDE Beta Version')
    app = SchemeIDE(master=root)
    app.mainloop()

