import tkinter as tk
import time

root = tk.Tk()

# width= ширина строки, height= колическтво строк, bg= цвет фона
text = tk.Text(root, width=100, height=1, bg='blue')
text.pack()

# Шрифт, размер, жирный
text.config(font=('Times New Roman', 100, 'bold'))

s1 = input("Введите текст для бегущей строки: ")

# накладка спереди и сзади на 50 символов
s2 = ' ' * 50
s = s2 + s1 + s2

for k in range(len(s)):

    ticker_text = s[k:]
    text.insert("1.1", ticker_text)
    root.update()
    # задержка на 0,15 секунды
    time.sleep(3/len(s))

root.mainloop()