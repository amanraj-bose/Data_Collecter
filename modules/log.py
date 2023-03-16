"""
    @Author => Aman Raj
    @Encoding => UTF-8
    @File Created => 14/02/2023
"""

class Log(object):
    def __init__(self, file) -> None:
        self.file = file
        self.f = open(self.file, "w")

    def log(self, value) -> None:
        self.f.writelines(value)

    def close(self):
        self.f.close()
