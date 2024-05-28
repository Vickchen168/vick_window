import tkinter as tk

def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as file: #file實體物件
        content:str = file.read()
    names:list[str]=content.split()
    return names

# print(__name__) #內建值為 "__main__"
# names:list[str] = get_names()

if __name__ == '__main__':
    names:list[str] = get_names()
    window:tk.Tk = tk.Tk()
    window.title('我的第一個GUI程式')    
    window.mainloop()

