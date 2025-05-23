from kernel import Kernel
import inspect, time

kernel = Kernel()

class Shell:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Shell, cls).__new__(cls)

        return cls.instance
        
    def prompt(self):
        t = int(time.time())
        h = t // 3600 % 24
        m = t // 60 % 60
        print(f"[{h}:{m}] [{kernel.pwd()}] $ ", end = "")
    
    def parse(self):
        self.prompt()

        buffer = input()

        args = buffer.split()
        if len(args) == 0:
            return 0
        
        try:
            func = getattr(Shell.instance, args[0])
            
            func(*args[1:])

        except AttributeError:
            print(f"Command '{args[0]}' not found")

        except TypeError:
            req = inspect.getfullargspec(func)

            print(f"""Command '{args[0]}' takes {len(req[0]) - 1} arguments: '{"', '".join(req[0][1:])}'""")
    
    def exec(self):
        while True:
            self.parse()

    def split_path(self, path):
        l = path.split('/')
        
        return '/'.join(l[:-1]), l[:-1]

    def mkdir(self, path):
        dire, file = self.split_path(path)
        
        try:
            kernel.mkdir_at(dire, file)

        except Exception as ex:
            print(ex)
    
    def rm(self, path):
        dire, file = self.split_path(path)

    def touch(self, path, file_name):
        self.cd(path)
        touch_fs(folder_name)   # it is system call
        self.cd(x)

    def ls(self):
        pass
    
    def cd(self, path):
        if path[0] == '/':
            self.cwd = path
        else:
            self.cwd += path
            
    def nwfiletxt(self, path):
        i = 1
        new = ''
        while 1:
            self.cd(path)
            x = self.ls()
            new = 'New File' + str(i) + '.txt'
            if not new in x:
                break
            i += 1
        
        self.touch(path, new)
    
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

