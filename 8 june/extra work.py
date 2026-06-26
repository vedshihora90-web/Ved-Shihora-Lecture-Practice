#like anyone program

try:
    atm_pin=int(input("enter your atm pin:"))
except ValueError:
    print("pin must contain numbers only")
else:
    print("pin accepted",atm_pin)
