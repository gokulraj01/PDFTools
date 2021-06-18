import tkinter as tk
import PyPDF2 as pdf
from tkinter import filedialog, messagebox
from tkinter.constants import E, END, NSEW, SINGLE

files = []

def windowBuild():
    global file_list
    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    text = tk.Label(window, text="Select PDF files to merge")
    text.grid(row=0)
    file_list = tk.Listbox(window, width=50, selectmode=SINGLE)
    file_list.grid(row=1, sticky=NSEW)
    navbar = tk.Frame()
    tk.Button(navbar, text="↑", command=moveUp).grid(row=0, padx=5, pady=5)
    tk.Button(navbar, text="↓", command=moveDown).grid(row=1, padx=5, pady=5)
    tk.Button(navbar, text="Add Files", command=addFileDialog).grid(row=2, padx=5, pady=5)
    tk.Button(navbar, text="Merge", command=mergeOpDialog).grid(row=3, padx=5, pady=5)
    navbar.grid(row=1, column=1, padx=5, pady=5, sticky=E)
    
def addFileDialog():
    in_file = filedialog.askopenfilenames(filetypes=(("PDF Documents","*.pdf"),))
    for i in in_file:
        addFiles(i)

def mergeOpDialog():
    out_file = filedialog.asksaveasfilename(defaultextension="pdf", filetypes=(("PDF Documents","*.pdf"),))
    print("Saving to: ", out_file)
    generateMergedPDF(out_file)

def repopulateList():
    file_list.delete(0, END)
    for i in files:
        file_list.insert(END, i)

def moveUp():
    index = file_list.curselection()[0]
    if(index > 0):
        temp = files[index]
        files[index] = files[index-1]
        files[index-1] = temp
        repopulateList()
        file_list.selection_set(index-1)


def moveDown():
    index = file_list.curselection()[0]
    if(index < file_list.index(END)-1):
        temp = files[index]
        files[index] = files[index+1]
        files[index+1] = temp
        repopulateList()
        file_list.selection_set(index+1)

def addFiles(new_file):
    for i in files:
        if(i == new_file):
            return
    files.append(new_file)
    file_list.insert(END, new_file)

def generateMergedPDF(op_name):
    merger = pdf.PdfFileMerger()
    for i in files:
        f = open(i, 'rb')
        merger.append(f)
    op_file = open(op_name, 'wb')
    merger.write(op_file)
    messagebox.showinfo("Success", "PDF Merged\nSaved to %s"%op_name)


window = tk.Tk()
windowBuild()
window.title("PDF Merger")
window.geometry("500x300")
window.mainloop()