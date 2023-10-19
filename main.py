from vendingmachine import VendingMachine
from beverage import Beverage


machine = VendingMachine()

cola1 = Beverage("coca cola", 11000)

print(machine.add_beverage(1, cola1, 20))
print(machine.add_beverage(2, cola1, 20))

print(machine.info(1))
print(machine.get_price("fanta"))
print(machine.recharge_card(1,100000))
print(machine.get_credit(1))
#machine.recharge_card(24, 12000)
#machine.recharge_card(24, 10000)

#credit = machine.getCredit(12)
#if credit != -1.0:
#    print(f"Card 12 has {credit} credits.")
#else:
#    print("Card 12 is not available.")

#machine.refill_column(1, "Coca Cola", 1)
#machine.refill_column(2, "Water", 10)
#machine.refill_column(3, "Pepsi", 15)
#machine.refill_column(4, "Water", 20)
#available_cans = machine.available_cans()
#print(f"Total available cans: {available_cans}")


result = machine.sell(1, "coca cola")
if result != -1.0:
   print(f"Sold coca cola from column {result}")
else:
   print("Sale failed. Please check the conditions.")
print(machine.get_credit(1))
print(machine.info(1))


