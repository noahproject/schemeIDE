import tkinter as tk

WELCOME_TEXT = "******************************************\n" \
               "Welcome to Scheme IDE Beta Version!       \n" \
               "Copyright 2014. All rights reserved.      \n" \
               "                                          \n" \
               "In this beta version, you can type on     \n" \
               "the screen and nothing else. No refunds.  \n" \
               "******************************************" 

class Application(tk.Frame):
    def create_widgets(self, r):
        editor = tk.Text(r,height=40,width=80,bg='black',fg='white', \
                         insertbackground='blue')
        editor.insert(tk.END, WELCOME_TEXT);
        editor.mark_set(tk.INSERT, "1.0")
        editor.pack()
        editor.mark_set(tk.INSERT, "1.0")

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.minsize(width=333, height=333)
        self.create_widgets(master)

root = tk.Tk()
root.title('Scheme IDE Beta Version')
app = Application(master=root)
app.editor.mark_set(tk.INSERT, "1.0")
app.mainloop()
root.destroy()
