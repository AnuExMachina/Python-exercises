my_number = int("56", 12)
other_number = int("12", 34)
f = float(24.5)
g = float(435.2)
print("zadanie 1")
print(f"pierwszy int - 56, baza 12: {my_number}")
print(f"drugi int - 12, baza 34: {other_number}")
print(f"pierwszy float: {f}")
print(f"drugi float: {g}")
print("zadanie 2")
print(f"{my_number}.bitcount(): {my_number.bit_count()}")
print(f"{g}.is_integer(): {g.is_integer()}")
print(f"24.0.is_integer(): {(24.0).is_integer()}")
print("zadanie 3")
print(f"bin({my_number}): {bin(my_number)}")
print(f"int(bin({my_number}), 2): {int(bin(my_number), 2)}")
print("zadanie 4")
print(f"{my_number} | 2: {my_number | 2}")
print(f"{my_number} ^ 2: {my_number ^ 2}")
print(f"{my_number} & 2: {my_number & 2}")
print(f"{my_number} << 2: {my_number << 2}")
print("zadanie 5")
print(f"{f}.hex(): {f.hex()}")
print(f"float.fromhex({f}.hex()): {float.fromhex(f.hex())}")
