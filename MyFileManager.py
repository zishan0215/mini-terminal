# Contains the File Manager class

import os
import sys

class FileManager:
    def __init__(self):
        self.history = []
        self.sname = ""
        self.tname = ""
        self.spath = ""
        self.tpath = ""
        self.sindex = -1

    def copyfile(self, source, target):
        '''
        Function to copy file from source to target
        Leave the target blank or put a dot (".") to create a file with the same name as the source
        :param source: any existing file path (eg. "foo.py", "/home/user/bar.txt")
        :param target: name of the target file (or path to target file) (eg. "bar.py", "/home/user/foo.txt")
        :return: 1 for success and -1 for error
        '''

        self.history.append("copyfile " + source + " " + target)
        if not os.path.exists(source):
            print("copyfile: cannot copy '" + source + "': no such file")
            return -1

        # Setting the target filename and path
        if target == "." or target == "":
            self.tpath = os.getcwd()
            index = source.rfind('/')
            if index == -1:
                self.tname = source
            else:
                self.tname = source[index+1:]

        elif os.path.isdir(target):
            # if target path is a directory, then the name of the file should be same as the source filename
            self.tpath = target
            index = source.rfind('/')
            if index == -1:
                self.tname = source
            else:
                self.tname = source[index+1:]

        elif not (os.path.exists(target) and os.path.isdir(target)):
            # target is a filename or a path ending with a filename
            index = target.rfind('/')
            if index == -1:
                self.tpath = os.getcwd()
                self.tname = target
            else:
                self.tpath = target[:index]
                self.tname = target[index+1:]

        tp = self.tpath

        if self.tpath[-1] == '/':
            self.tpath += self.tname
        else:
            self.tpath += '/' + self.tname

        if not os.path.exists(tp):
            print("copyfile: cannot create file '" + self.tpath + "': no such file or directory")
            return -1

        # Setting the source filename and path
        if os.path.isdir(source):
            print("Source is a directory. Use copydir instead")
            return -1

        self.spath = source

        sfptr = open(self.spath, 'r')
        sfcontent = sfptr.read()
        sfptr.close()
        tfptr = open(self.tpath, 'w')
        tfptr.write(sfcontent)
        tfptr.close()

        return 1

    def copydir(self, source, target):
        '''
        A routine to copy directories including sub directories
        Eg.:
            copydir("foo", "bar")
            copydir("foo/baz","foo/bar")
            copydir("baz", ".")
            copydir("foo", "bar/foo")
        :param source:
        :param target:
        :return: 1 for succuss, -1 for failure
        '''

        if source == '/' or source == '~':
            print("copydir: please enter a valid path")
            return -1

        if not os.path.exists(source):
            print("copydir: cannot copy '" + source + "': no such file or directory")
            return -1

        # check if base target directory exists
        index = target.find('/')
        if index == len(target) - 1:
            index = target.rfind('/', 0, index-1)
        if index != -1:
            base = target[:index]
            if not os.path.exists(base):
                print("copydir: cannot copy '" + target + "': no such file or directory")
                return -1

        if source == target:
            print("copydir: cannot copy directory '" + source + "' into itself")
            return -1

        # get source base dir
        index = source.rfind('/')
        if index == len(source)-1:
            index = source.rfind('/', 0, index-1)
        if index == -1:
            self.sname = source
            self.spath = ""
        else:
            self.sindex = index
            self.sname = source[index+1:]
            self.spath = source[:index+1]

        ts = source
        i = -1
        count = 0
        while True:
            i = ts.find('/', i+1)
            if i == len(ts) - 1 or i == -1:
                break
            else:
                count += 1

        # print('slashes:', count)

        # get target base dir
        if os.path.exists(target):
            self.tname = self.sname
            self.tpath = target
            if self.tpath[len(self.tpath)-1] != '/':
                self.tpath += '/'
            if not os.path.exists(self.tpath+self.tname):
                os.mkdir(self.tpath+self.tname)
        else:
            index = target.rfind('/')
            if index == len(target)-1:
                index = target.rfind('/', 0, index-1)
            if index == -1:
                self.tname = target
                self.tpath = ""
                if not os.path.exists(self.tname):
                    os.mkdir(self.tname)
            else:
                self.tname = target[index+1:]
                self.tpath = target[:index+1]
                if not os.path.exists(self.tpath+self.tname):
                    os.mkdir(self.tpath+self.tname)

        # print("source base: " + self.sname)
        # print("source path: " + self.spath)
        # print("target base: " + self.tname)
        # print("target path: " + self.tpath)

        for root, dirs, files in os.walk(source):
            i = -1
            index = -1
            while i < count:
                index = root.find('/', index+1)
                i += 1

            troot = root
            if index == -1:
                path = self.tpath + self.tname
            else:
                if self.tname[-1] != '/':
                    if len(troot[index+1:]) > 0 and troot[index+1:][0] != '/':
                        path = self.tpath + self.tname + '/' + troot[index+1:]
                    else:
                        path = self.tpath + self.tname + troot[index+1:]
                else:
                    path = self.tpath + self.tname + troot[index+1:]

            if root[-1] != '/':
                root += '/'
            if path[-1] != '/':
                path += '/'

            # print('path:', path)
            # print('root:', root)

            for file in files:
                fptr = open(root+file, 'r')
                tfile = fptr.read()
                fptr.close()

                # print(path+file)
                fptr = open(path+file, 'w')
                fptr.write(tfile)
                fptr.close()

            for dir in dirs:
                if not os.path.exists(path+'/'+dir):
                    os.mkdir(path+'/'+dir)

        return 1

    def movefile(self, source, target):

        if not os.path.exists(source):
            print("movefile: cannot move '" + source + "': no such file")
            return -1

        if os.path.isdir(source):
            print("Source is a directory. Use movedir instead")
            return -1

        # get base and path of source
        index = source.rfind('/')
        if index == len(source)-1:
            index = source.rfind('/')
        if index == -1:
            self.sname = source
            self.spath = ""
        else:
            self.sname = source[index+1:]
            self.spath = source[:index]

        # get base and path of target
        index = target.rfind('/')
        if index == len(target)-1:
            index = target.rfind('/')
        if index == -1:
            self.tname = target
            self.tpath = ""
        else:
            self.tname = target[index+1:]
            self.tpath = target[:index]

        if self.spath == self.tpath:
            # same path. just rename
            os.rename(source, target)
        else:
            self.copyfile(source, target)
            os.remove(source)

        return 1

    def movedir(self, source, target):
        if not os.path.exists(source):
            print("movedir: cannot move '" + source + "': no such directory")
            return -1

        if not os.path.isdir(source):
            print("Source is a file. Use movefile instead")
            return -1

        # get base and path of source
        index = source.rfind('/')
        if index == len(source)-1:
            index = source.rfind('/')
        if index == -1:
            self.sname = source
            self.spath = ""
        else:
            self.sname = source[index+1:]
            self.spath = source[:index]

        # get base and path of target
        index = target.rfind('/')
        if index == len(target)-1:
            index = target.rfind('/')
        if index == -1:
            self.tname = target
            self.tpath = ""
        else:
            self.tname = target[index+1:]
            self.tpath = target[:index]

        if self.spath == self.tpath:
            # same path. just rename
            os.rename(source, target)
            print('renaming')
        else:
            self.copydir(source, target)
            # os.rmdir(source)

        return 1

    def deletefile(self, source):
        if not os.path.exists(source):
            print("deletefile: cannot delete '" + source + "': no such file")
            return -1
        os.remove(source)
        return 1

    def deletedir(self, source):
        stack = []
        for root, dirs, files in os.walk(source):
            for file in files:
                os.remove(root+'/'+file)

            for sdir in dirs:
                # print('path:', root+'/'+sdir)
                stack.append(root+'/'+sdir)

        while len(stack) > 0:
            path = stack.pop()
            os.rmdir(path)

        os.rmdir(source)
        return 1
