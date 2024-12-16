from tkinter import *

vowels = {'','e','i','o','u','a'}
newWord = ""

def Huzzify(word):
    global newWord
    if word:
        for i in word:
            if i in vowels:
                splitWord = word.split(i,len(word)-1)
                splitWord.pop()
                splitWord.append("uzz")
                newWord = "".join(splitWord)
                print(newWord)
    else:
        newWord = "Process failed."

root = Tk()
root.title("Huzzifier")
root.geometry("400x400")
root.config(bg="teal")

def ShowWord():
    global newWord
    frame = Frame(root)
    frame.grid(row=0, column=0)
    Label(frame, text="Huzzifier").pack(pady=10)
    userIn = Entry(frame)
    userIn.pack()
    out = Label(frame, text=newWord)
    Button(frame,text="Submit",command=lambda:[Huzzify(userIn.get()), out.config(text=newWord)]).pack()
    out.pack()

ShowWord()

root.mainloop()