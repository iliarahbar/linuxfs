from kernel import *

class Shell:
    def __init__(self):
        self.env = {"PWD": "/"}
        self.fs = FS()
        self.cwd = self.fs.root

    def prompt(self):
        t = int(time.time())
        h = t // 3600 % 24
        m = t // 60 % 60
        print(f"[{h}:{m}] [{self.env['PWD']}] $ ", end = "")
    
    def parse(self):
        self.prompt()

        buffer = input()

        args = buffer.split()
    
    def exec(self):
        while True:
            self.parse()

    def mkdir(self, path, folder_name):
        pass

    def touch(self, path, file_name):
        pass

    def ls(self):
        pass
    
    def rm(self, path):
        pass
    
    def cd(self, path):
        pass
    
    def nwfiletxt(self, path):
        pass
    
    def appendtxt(self, path):
        pass
    
    def editline(self, path, line, text):
        pass
    
    def deline(self, path, line):
        pass

    def cat(self, cat):
        pass

    def mv(self, source_path, destination_path):
        pass
    
    def cp(self, source_path, destination_path):
        pass
    
    def rename(self, path, new_name):
        pass

s = Shell()
s.exec()
