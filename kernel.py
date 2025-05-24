import sys, time, copy

REG_FILE = 0b1000000000000000
DIR_FILE = 0b0100000000000000
R_PERM = 0b100
W_PERM = 0b010
X_PERM = 0b001
O_PERM = 0b1
G_PERM = 0b1000
U_PERM = 0b1000000
DEF_REG_PERM = (R_PERM | W_PERM) * U_PERM | (R_PERM | W_PERM) * G_PERM | (R_PERM) * O_PERM
DEF_DIR_PERM = (R_PERM | W_PERM | X_PERM) * U_PERM | (R_PERM | X_PERM) * G_PERM | (R_PERM | X_PERM) * U_PERM

class Inode:
    count = 0

    def __init__(self, name = "", par = None, mode = REG_FILE | DEF_REG_PERM):
        self.name = name
        self.par = par
        self.mode = mode
        self.uid = 1
        self.gid = 1
        self.atime = int(time.time()) 
        self.ctime = int(time.time())
        self.mtime = int(time.time())
        self.dtime = -1
        self.links_count = 1
    
        if (self.mode & REG_FILE):
            self.content = ""

        elif (self.mode & DIR_FILE):
            self.content = {"." : self, ".." : self.par}

        self.size = sys.getsizeof(self.content)

        self.id = Inode.count
        Inode.count += 1


class FS:
    def __init__(self):
        self.root = Inode(mode = DIR_FILE | DEF_DIR_PERM)
        self.root.par = self.root

class Kernel:
    def __init__(self):
        self.fs = FS()
        self.cwd = self.fs.root

    def pwd(self):
        p = [self.cwd.name]

        d = self.cwd

        while (d.par != d):
            d = d.par
            p.append(d.name)

        p.reverse()

        if (len(p) == 1):
            p.append('')

        return '/'.join(p)

    def get_inode(self, path):
        l = path.strip('/').split('/')

        if (len(path) == 0):
            cur = self.cwd
            l = []

        elif (path[0] == '/'):
            cur = self.fs.root

            if (l[0] == ''):
                l = l[1:]

        else:
            cur = self.cwd

        for dire in l:
            if not dire in cur.content:
                raise Exception(f"Direcotry '{dire}' not found")

            if cur.content[dire].mode & DIR_FILE == 0:
                raise Exception(f"'{dire}' is not a direcotry")

            cur = cur.content[dire]

        return cur

    def mkdir_at(self, dire, file):
        ind = self.get_inode(dire)

        if file in ind.content:
            raise Exception(f"'{file}' exists")

        ind.content[file] = Inode(file, ind, mode = DIR_FILE | DEF_DIR_PERM)

    def unlink(self, dire, file):
        ind = self.get_inode(dire)

        if not file in ind.content:
            raise Exception(f"File '{dire}' not found")

        ind.content.pop(file)

    def write(self, dire, file, data, append = 0):
        ind = self.get_inode(dire)

        if not file in ind.content:
            ind.content[file] = Inode(file, ind)

        if ind.content[file].mode & DIR_FILE != 0:
                raise Exception(f"'{file}' is a direcotry")

        f = ind.content[file]

        if (append):
            f.content += data

        else:
            f.content = data

    def read(self, dire, file):
        ind = self.get_inode(dire)

        if not file in ind.content:
            raise Exception(f"File '{dire}' not found")

        f = ind.content[file]

        return f.content

    def chdir(self, path):
        ind = self.get_inode(path)

        self.cwd = ind

    def renameat(self, sdir, sfile, ddir, dfile):
        sind = self.get_inode(sdir)
        dind = self.get_inode(ddir)

        if not sfile in sind.content:
            raise Exception(f"File '{dire}' not found")

        dind.content[dfile] = sind.content[sfile]

        sind.content.pop(sfile)

        dind.content[dfile].name = dfile

    def dup(self, sdir, sfile, ddir, dfile):
        sind = self.get_inode(sdir)
        dind = self.get_inode(ddir)

        if not sfile in sind.content:
            raise Exception(f"File '{dire}' not found")

        dind.content[dfile] = copy.deepcopy(sind.content[sfile])

        dind.content[dfile].name = dfile
