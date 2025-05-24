#!/bin/python3
from kernel import Kernel
import inspect, time, os

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

    def editor(self):
        os.system("vim buff")

        with open('buff') as b:
            data = b.read()

        os.system("rm buff")

        return data
    
    def exec(self):
        while True:
            self.parse()

    def split_path(self, path):
        l = path.strip('/').split('/')

        return ('/' if path[0] == '/' else '') + '/'.join(l[:-1]), ('.' if l[-1] == '' else l[-1])

    def mkdir(self, path):
        dire, file = self.split_path(path)
        
        try:
            kernel.mkdir_at(dire, file)

        except Exception as ex:
            print(ex)
    
    def rm(self, path):
        dire, file = self.split_path(path)
        
        try:
            kernel.unlink(dire, file)

        except Exception as ex:
            print(ex)

    def touch(self, path):
        dire, file = self.split_path(path)

        try:
            kernel.write(dire, file, "")

        except Exception as ex:
            print(ex)

    def ls(self, path = '.'):
        dire, file = self.split_path(path)

        try:
            dc = kernel.read(dire, file)

            print(*dc.keys())

        except Exception as ex:
            print(ex)      
    
    def cd(self, path):
        try:
            kernel.chdir(path)

        except Exception as ex:
            print(ex)     
            
    def nwfiletxt(self, path):
        dire, file = self.split_path(path)
        
        data = self.editor()

        try:
            kernel.write(dire, file, data)

        except Exception as ex:
            print(ex)     

    def appendtxt(self, path):
        dire, file = self.split_path(path)
        
        data = self.editor()

        try:
            kernel.write(dire, file, data, append=1)

        except Exception as ex:
            print(ex)    
    
    def editline(self, path, line, *text):
        dire, file = self.split_path(path)

        try:
            data = kernel.read(dire, file)

            l = data.split('\n')

            if (len(l) < line):
                print("line {line} not found, file {file} has {len(l}) lines")

            else:
                l[line-1] = ' '.join(text)

                newdata = '\n'.join(l)

                try:
                    kernel.write(dire, file, newdata)

                except Exception as ex:
                    print(ex) 

        except Exception as ex:
            print(ex)
    
    def deline(self, path, line):
        dire, file = self.split_path(path)

        try:
            data = kernel.read(dire, file)

            l = data.split('\n')

            if (len(l) < line):
                print("line {line} not found, file {file} has {len(l}) lines")

            else:
                l = l[:line] + l[line+1:]

                newdata = '\n'.join(l)

                try:
                    kernel.write(dire, file, newdata)

                except Exception as ex:
                    print(ex) 

        except Exception as ex:
            print(ex)

    def cat(self, path):
        dire, file = self.split_path(path)

        try:
            data = kernel.read(dire, file)

            print(data, end = "")

        except Exception as ex:
            print(ex)


    def mv(self, source_path, destination_path):
        sdir, sfile = self.split_path(source_path)
        ddir, dfile = self.split_path(destination_path)
        
        try:
            kernel.renameat(sdir, sfile, ddir, dfile)

        except Exception as ex:
            print(ex)
    
    def cp(self, source_path, destination_path):
        sdir, sfile = self.split_path(source_path)
        ddir, dfile = self.split_path(destination_path)
        
        try:
            kernel.dup(sdir, sfile, ddir, dfile)

        except Exception as ex:
            print(ex)

    def rename(self, path, new_name):
        sdir, sfile = self.split_path(path)
        
        try:
            kernel.renameat(sdir, sfile, sdir, new_name)

        except Exception as ex:
            print(ex)
   
    
s = Shell()
s.exec()

