#raised keyword

'''for handeking manuualy trigger exception in python'''

age=5
if age<0:
    raise ValueError("age cannot be negative")

#assert keyword in python

'''for using debugging and testing condition'''
'''if the condition is true->program run
   if the condition is false->assertion error is raised'''

num=10
assert num>0,"number must be positive."
print("valid number")

#custom exception exception with try-except

class InsufficientBalanceError(Exception):
    pass
balance=10000
withdraw=1500

try:
    if withdraw>balance:
        raise InsufficientBalanceError("not enough balance")
    print("withdrawal successful.")
except InsufficientBalanceError as e:
            print("Error:",e)


