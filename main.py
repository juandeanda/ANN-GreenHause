from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from read import readFile

root = Tk(  )
fileDataset = ""
#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="",
                           filetypes =(("Text File", "*.csv"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    dataset = readFile(name)
    print(dataset)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            fileDataset  = UseFile.read()
    except:
        print("No file exists")
    

Title = root.title( "Red Neuronal Artificial de estado critico de jitomate")
label = ttk.Label(root, text ="Red Neuronal Artificial de estado critico de jitomate",foreground="red",font=("Helvetica", 16))
label.pack()

#Menu Bar

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())

menu.add_cascade(label = 'File', menu = file)





root.mainloop()
