import re

class Well:

    def __init__(self):
        return

    def format_string(self, str_in):
        return re.sub('\W+', '_', str_in).lower()

    @classmethod
    def from_txt(cls, pth, sep=':'):

        with open(pth, 'r') as f:
            lines = f.readlines()

        cls.attrs = {}
        for line in lines:
            rtn = line.replace(' ', '').replace('#', '').strip().split(sep)

            if len(rtn) == 2:
                
                setattr(cls, rtn[0], rtn[1])
                cls.attrs[rtn[0]] = rtn[1]

        return cls

w1 = Well.from_txt('header.txt')

print(w1)

print(w1.attrs.keys())