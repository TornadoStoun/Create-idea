import tkinter as tk
from tkinter import font
import random

# прога для сочетания трех слов из списка


file_name = 'ideas.txt'

# Берет из списка рандомные слова и выводит их в определенные строки
def create_idea():
    with open('ideas.txt','r', encoding='UTF-8') as f:
        idea = f.readlines()
        random_idea1 = random.choice(idea).strip()
        random_idea2 = random.choice(idea).strip()
        random_idea3 = random.choice(idea).strip()
        while random_idea2 == random_idea1:
            random_idea2 = random.choice(idea).strip()
        while random_idea3 == random_idea1:
            random_idea3 = random.choice(idea).strip()
            while random_idea3 == random_idea2:
                random_idea3 = random.choice(idea).strip()
        lab1.config(text=random_idea1)
        lab2.config(text=random_idea2)
        lab3.config(text=random_idea3)
        
def add_word():
    word = tex.get("1.0", "end-1c")
    with open('ideas.txt','a',encoding='UTF-8') as fu:
        fu.write('\n' + word)
        tex.delete("1.0", "end-1c")



concept =tk.Tk()
concept.geometry('300x250')
concept.title('Генератор идей для персонажа')
concept.configure(bg ='gray')
plus_font = font.Font(size=20)
    
btn1 = tk.Button(text='Сгенерировать идею для персонажа', command=create_idea)
btn2 = tk.Button(text='Записать слово в список',command=add_word)
lab1 = tk.Label(width=10, height=2)
lab2 = tk.Label(width=10, height=2)
lab3 = tk.Label(width=10, height=2)
tex = tk.Text(width=20,height=4)
pl1 = tk.Label(text='+',width=1,height=1,font=plus_font)
pl1.configure(bg = 'gray')
pl2 = tk.Label(text='+',width=1,height=1,font=plus_font)
pl2.configure(bg = 'gray')
    
lab1.place(x=1, y=5)
lab2.place(x=110, y=5)
lab3.place(x=220, y=5)
pl1.place(x=82,y=4)
pl2.place(x=190,y=4)
btn1.place(x=10,y=180)
btn2.place(x=10,y=220)
tex.place(x=60,y=80)
    
concept.mainloop()