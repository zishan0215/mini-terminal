import MyFileManager

def help():
    print()
    print("List of commands")
    print("1. copyfile​ <source_file_path> <destination_file_path>")
    print("2. copydir <source_directory_path> <destination_directory_path>")
    print("3. ​movefile​ <source_file_path> <destination_file_path>")
    print("4. ​movedir​ <source_directory_path> <destination_directory_path>")
    print("5. ​rmfile​ <source_file_path> <destination_file_path>")
    print("6. ​rmdir​ <source_directory_path> <destination_directory_path>")
    print("7. help: for help")
    print("8. exit: To exit the terminal")
    print()

if __name__ == '__main__':
    fm = MyFileManager.FileManager()
    print("Welcome to Zishan's Terminal")
    print("Type `help` to see a list of commands")
    com = ""
    while True:
        com = input('$ ')
        if com == "exit":
            break
        if com == "help":
            help()
        else:
            lcom = com.split()
            if lcom[0] == "copyfile":
                fm.copyfile(lcom[1], lcom[2])
            elif lcom[0] == "copydir":
                fm.copydir(lcom[1], lcom[2])
            elif lcom[0] == "movefile":
                fm.movefile(lcom[1], lcom[2])
            elif lcom[0] == "movedir":
                fm.movedir(lcom[1], lcom[2])
            elif lcom[0] == "rmfile":
                fm.rmfile(lcom[1])
            elif lcom[0] == "rmdir":
                fm.rmdir(lcom[1])
            else:
                print("This command is not supported. Type 'help' to see a list of commands")

    print("Thank you for using Zishan's Terminal")
    # fm.copyfile("main.py", "test/abc.txt")
    # fm.copydir("test", "temp")
    # fm.movefile("test/one/onemore/onemore.txt", "test/abc.txt")
    # fm.movedir("t1", "/home/zishan/t2")
    # fm.copydir("t3", "t1")
    # fm.deletedir("t2")
