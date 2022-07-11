
class test():
    def __init__(self, hoge):
        super().__init__()
        self.Iph = hoge

    def print(self):
        print(self.Iph)


fp = test(1)
fp.print()
print(fp.Iph)


fp2 = test(2)
fp2.print()
print(fp2.Iph)

