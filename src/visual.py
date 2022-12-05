
import tkinter as tk

# Создается новое окно с заголовком.
window = tk.Tk()
window.title("Форма расчета")

# Создается новая рамка `frm_form` для ярлыков с текстом и
# Однострочных полей для ввода информации об адресе.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

# Помещает рамку на окно приложения.
frm_form.pack()

# Список ярлыков полей.
labels = [
    "Масса первой звезды:",
    "Масса второй звезды:",
    "Радиус:",

]

# Цикл для списка ярлыков полей.
for idx, text in enumerate(labels):
    # Создает ярлык с текстом из списка ярлыков.
    label = tk.Label(master=frm_form, text=text)
    # Создает текстовое поле которая соответствует ярлыку.
    entry = tk.Entry(master=frm_form, width=50)
    label.grid(row=idx, column=0, sticky="e")
    entry.grid(row=idx, column=1)

# Создает новую рамку `frm_buttons` для размещения в ней
# кнопок "Отправить" и "Очистить".
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Создает кнопку "Отправить" и размещает ее
# справа от рамки `frm_buttons`.
btn_submit = tk.Button(master=frm_buttons, text="ввод")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Создает кнопку "Очистить" и размещает ее
# справа от рамки `frm_buttons`.
btn_clear = tk.Button(master=frm_buttons, text="отмена")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

# Запуск приложения.
window.mainloop()