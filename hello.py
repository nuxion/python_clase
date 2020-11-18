with open("mails.txt", "r") as archivo:
    for line in archivo.readlines():
        print(line.split("|")[1])


