import MyFileManager


if __name__ == '__main__':
    fm = MyFileManager.FileManager()
    # fm.copyfile("main.py", "test/abc.txt")
    # fm.copydir("test", "temp")
    # fm.movefile("test/one/onemore/onemore.txt", "test/abc.txt")
    # fm.movedir("t1", "/home/zishan/t2")
    # fm.copydir("t3", "t1")
    fm.deletedir("t2")
