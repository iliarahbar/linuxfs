import sys, time

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

    def __init__(self, par = None, mode = REG_FILE | DEF_REG_PERM):
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


