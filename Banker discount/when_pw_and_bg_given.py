from fractions import Fraction
print("this is used to find true discount using present worth and bankers gain")
number_of_inputs = int(input("Enter number of inputs : "))

for i in range(number_of_inputs):
    present_worth = Fraction(input("Enter present worth (RS) : "))
    bankers_gain = Fraction(input("Enter bankers gain (RS) : "))
    print("True Discount = (present worth*bankers gain)**0.5")
    true_discount = round(float((present_worth*bankers_gain)**0.5), 2)

    if true_discount >= 0:
        print("True discount : RS "+str(true_discount)+"  ---------- "+str(i+1))
        print(" ")
    else:
        print("enter valid details")