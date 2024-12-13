from tkinter import *

vowels = {'a','e','i','o','u'}

def Huzzify(word):
    global newWord
    if word:
        for i in word:
            if i in vowels:
                splitWord = word.split(i,len(word)-1)
                splitWord.pop()
                splitWord.append("uzz")
                newWord = "".join(splitWord)
    else:
        print("Failed")

root = Tk()
root.title("Huzzifier")
root.geometry("400x400")
root.config(bg="teal")

frame = Frame(root)
frame.grid(row=0, column=0)
Label(frame, text="Huzzifier").pack(pady=10)
userIn = Entry(frame)
userIn.pack()
Button(frame,text="Submit",command=lambda:Huzzify(userIn.get()))

root.mainloop()