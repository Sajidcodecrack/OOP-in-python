class account:
    def __init__(self,acc_num,acc_pass):
        self.acc_num=acc_num
        self.__acc_pass=acc_pass
    def reset(self):
        print(self.__acc_pass)    
acc1=account("323446","20A3")
print(acc1.acc_num)
print(acc1.reset())