import random as rn
import string as str
def acc_numgen():
    digi=str.digits
    acc_num=""
    for i in range(11):
        rann=rn.choice(digi)
        acc_num=rann+acc_num
    return acc_num
print(acc_numgen())