def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
           numbers.append(int(line))
    print(numbers)




# def write():
#     names = ["ly", "amaia", "moises"]
#     with open("./archivos/names.txt", "w", encoding="utf-8") as f:
#         for name in names:
#             f.write(name)
#             f.write("\n")

def write():
    names = ["nathalie", "jessimar", "vilmar", "mariana"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")




def run():
    write()



if __name__ == '__main__':
    run()