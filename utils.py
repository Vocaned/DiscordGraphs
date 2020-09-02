import datetime

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + datetime.timedelta(n)

class Line(object):
    def __init__(self, x, y, color='red', label='', linestyle='-', alpha=1):
        self.x = x
        self.y = y
        self.color = color
        self.label = label
        self.linestyle = linestyle
        self.alpha = alpha