from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from read import readFile
from ANN import *
dataset = []
N = 0
root = Tk(  )
L1 = Label(root, text="N neurona")
L1.pack( side = RIGHT)
E1 = Entry(root)
E1.pack(side = RIGHT)
L2 = Label(root, text="rate")
L2.pack( side = RIGHT)
E2 = Entry(root)
E2.pack(side = RIGHT)
L3 = Label(root, text="Epoca")
L3.pack( side = RIGHT)
E3 = Entry(root)
E3.pack(side = RIGHT)


#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="",
                           filetypes =(("Text File", "*.csv"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    global dataset
    dataset = readFile(name)
    
    #ANN_run(dataset)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            fileDataset  = UseFile.read()
    except:
        print("No file exists")
    
def helloCallBack():
    N = E1.get()
    R = E2.get()
    E = E3.get()
    ANN_run(dataset,N,R,E)
   
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

B = Button(root, text ="Entrenar", command = helloCallBack)
B.pack()

root.mainloop()
