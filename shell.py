import fs

class Shell:
    def __init__(self):
        self.env = {"PWD": "/"}
        self.fs = FS()
        self.cwd = self.fs.root

    def prompt(self):
        print(f"[{self.env[PWD]}]$ ", end = "")
    
    def parse(self):
        prompt()

        buffer = input()

        args = buffer.split()
    
        print(args)

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

s =shell()
s.exec()
