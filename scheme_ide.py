import tkinter as tk

class SchemeIDE(tk.Frame):
    '''
    Scheme IDE

    This is the main application window.   
    '''

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.minsize(width=300, height=300)
        self.create_editor(master)

    def create_editor(self, r):
        editor = tk.Text(r,height=30,width=60,bg='black',fg='white', \
                         insertbackground='blue')
        editor.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Scheme IDE Beta Version')
    app = SchemeIDE(master=root)
    app.mainloop()
    root.destroy()
