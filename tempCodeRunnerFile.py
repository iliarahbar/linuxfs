def prompt(self):
        t = int(time.time())
        h = t // 3600 % 24
        m = t // 60 % 60
        print(f"[{h}:{m}] [{self.env['PWD']}] $ ", end = "")