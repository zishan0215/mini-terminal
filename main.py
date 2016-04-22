import MyFileManager


if __name__ == '__main__':
    fm = MyFileManager.FileManager()
    # ack = fm.copyfile("main.py", "test/abc.txt")
    ack = fm.copydir("test", "temp")
