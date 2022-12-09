import tkinter as tk
root = tk.Tk()
root.title("Форма расчета")
root.geometry("400x200")

def getTextInput():
    result=textExample.get("1.0","end")
    return 

entry = tk.Entry(width=100, bg="white", fg="black")
entry.pack()

entry.insert(0, "Введите: "
                "массу первой звезды, "
                "массу второй звезды, "
                "радиус")

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=2, width=10, text="Ввод",
                    command=getTextInput)

btnRead.pack()

root.mainloop()
result=textExample.get("1.0", "end")
