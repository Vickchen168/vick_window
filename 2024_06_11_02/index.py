import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import data

class Window(ThemedTk):
    def __init__(self, theme: str | None, **kwargs):
        super().__init__(**kwargs)
        self.title("YouBike 即時資料")
        
        self.tree = ttk.Treeview(self, columns=("站名", "區域", "更新時間", "可租車數", "可還車數"))
        self.tree.heading("#0", text="站點編號")
        self.tree.heading("站名", text="站名")
        self.tree.heading("區域", text="區域")
        self.tree.heading("更新時間", text="更新時間")
        self.tree.heading("可租車數", text="可租車數")
        self.tree.heading("可還車數", text="可還車數")
        self.tree.pack(fill="both", expand=True)
        
        try:
            ubike = data.load_data()
            self.fill_tree(ubike)
        except Exception as error:
            print(error)
        
    def fill_tree(self, ubike):
        for idx, station in enumerate(ubike, start=1):
            self.tree.insert("", "end", text=str(idx), values=(
                station["sna"],
                station["sarea"],
                station["mday"],
                station["available_rent_bikes"],
                station["available_return_bikes"]
            ))

def main():   
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()
