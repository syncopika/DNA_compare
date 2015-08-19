from tkinter import *
from tkinter import ttk

#set up window
root = Tk() 

#name of window
root.title("DNA Compare") 

#favicon optional. make sure favicon is stored in same directory as the .py file!
root.wm_iconbitmap('favicon.ico')

def DNAcompare():
    try:
        value1=str(seq1.get())
        value2=str(seq2.get())
        value1=value1.replace(' ','') #this removes any spaces between nucleotides, which may occur if copying over a sequence from another file into MS Word of Notepad.
        value2=value2.replace(' ','')
        if len(value1)>len(value2):
            value1=value1[0:len(value2)]
            for i in range(0,len(value2)):
                if value1[i]!=value2[i]:
                    result.set((str(i+1)+', '+value1[i]+', '+value2[i]))  #the i+1 makes it so that the nucleotide count starts at 1.
                    length1.set(str(len(value1))) #this print the length of the sequence.
                    length2.set(str(len(value2)))
        if len(value2)>len(value1):
            value2=value2[0:len(value1)]
            for i in range(0,len(value1)):
                if value1[i]!=value2[i]:
                    result.set((str(i+1)+', '+value1[i]+', '+value2[i]))
                    length1.set(str(len(value1)))
                    length2.set(str(len(value2)))
        if len(value1)==len(value2):
            for i in range(0,len(value1)):
                if value1[i]!=value2[i]:
                    result.set((str(i+1)+', '+value1[i]+', '+value2[i]))
                    length1.set(str(len(value1)))
                    length2.set(str(len(value2)))
    except ValueError:
        pass

#by putting the DNAcompare() function under the domain of onclick, connecting the Enter/Return key and DNAcompare should be successful. 
def onclick(event="None"):
    DNAcompare()
    
mainframe = ttk.Frame(root, padding="12 12 12 12") #specify dimensions of window (padding is left top right bottom-clockwise)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #place grid onto window
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight=1)

seq1=StringVar() 
seq2=StringVar()
length1=StringVar()
length2=StringVar()
result=StringVar()

seq1_entry = ttk.Entry(mainframe, width=10, textvariable=seq1) #this is the space for you to enter seq1 nucleotides
seq2_entry = ttk.Entry(mainframe, width=10, textvariable=seq2)
seq1_entry.grid(column=2, row=1, sticky=(W,E))
seq2_entry.grid(column=2, row=2, sticky=(W,E))
ttk.Label(mainframe, textvariable=length1).grid(column=3, row=1, sticky=(W,E))
ttk.Label(mainframe, textvariable=length2).grid(column=3, row=2, sticky=(W,E))
ttk.Label(mainframe, textvariable=result).grid(column=2, row=3, sticky=(W,E))
ttk.Button(mainframe, text="Compare!", command=DNAcompare).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="seq1:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="seq2:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="result:").grid(column=1,row=3, sticky=W)

#touch-up to make the GUI pretty :D
for child in mainframe.winfo_children(): child.grid_configure(padx=6, pady=6)
seq1_entry.focus()
root.bind('<Return>', onclick)

root.mainloop();
