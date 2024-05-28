with open('names.txt', encoding='utf-8') as file: #file實體物件
    content:str = file.read()
names:list[str]=content.split()
for name in names:
    print(name)