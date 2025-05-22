from kernel import *

class Shell:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Shell, cls).__new__(cls)

        return cls.instance
        

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
        if len(args) == 0:
            continue
        
        getattr(self, args[0])(*args[1:])      
    
    def exec(self):
        while True:
            self.parse()

    def mkdir(self, path, folder_name):
        x = self.cwd
        self.cd(path)
        mkdir_fs(folder_name)   # it is system call
        self.cd(x)

    def touch(self, path, file_name):
        x = self.cwd
        self.cd(path)
        touch_fs(folder_name)   # it is system call
        self.cd(x)

    def ls(self):
        pass
    
    def rm(self, path):
        x = path.split('/')[-1]
        y = path[:-1]
        location = ''
        for i in range(len(y)):
            location += '/' + y[i]
        cur_loc = self.path
        self.cd(location)
        delete_fs(x[-1])   # it is system call
        self.cd(cur_loc)
    
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
print(s)
s = Shell()
print(s)
s.exec()

