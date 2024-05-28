def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as file: #file實體物件
        content:str = file.read()
    names:list[str]=content.split()
    return names

# print(__name__) #內建值為 "__main__"
# names:list[str] = get_names()

if __name__ == '__main__':
    names:list[str] = get_names()
    print(names)
