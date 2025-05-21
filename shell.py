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

    def mkdir(self):
        pass

    def touch(self):
        pass

    def cd(self):
        pass

    def ls(self):
        pass

s = Shell()
s.exec()
