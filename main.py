import MyFileManager


if __name__ == '__main__':
    fm = MyFileManager.FileManager()
    # fm.copyfile("main.py", "test/abc.txt")
    # fm.copydir("test", "temp")
    # fm.movefile("test/one/onemore/onemore.txt", "test/abc.txt")
    # fm.movedir("t1", "test/t2")
    # fm.copydir("t3", "/home/zishan/")
    fm.deletedir("/home/zishan/t3")
