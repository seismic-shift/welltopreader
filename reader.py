import re

class Well:

    def __init__(self):
        return

    @classmethod
    def from_txt(cls, pth, sep=':'):

        with open(pth, 'r') as f:
            lines = f.readlines()

        cls.attrs = {}
        for line in lines:
            rtn = line.replace(' ', '').replace('#', '').strip().split(sep)

            if len(rtn) == 2:
                
                attr = re.sub('\W+', '', rtn[0].strip()).lower()

                setattr(cls, attr, rtn[1])
                cls.attrs[attr] = rtn[1]

        return cls

w1 = Well.from_txt('header.txt')

print(w1)

print(w1.attrs.keys())