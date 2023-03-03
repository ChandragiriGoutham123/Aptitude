from fractions import Fraction
print("this is used to find sum using true discount and banker discount")
number_of_inputs = int(input("Enter number of inputs : "))

for i in range(number_of_inputs):
    bankers_discount = Fraction(input("Enter bankers discount (RS) : "))
    true_discount = Fraction(input("Enter True Discount (RS) : "))
    print("sum = (Bankers discount * true discount)/(bankers discount -true discount)")
    total_sum = round(float((bankers_discount*true_discount)/(bankers_discount-true_discount)), 2)

    if total_sum >= 0:
        print("total sum : RS "+str(total_sum)+"  ---------- "+str(i+1))
        print(" ")
    else:
        print("enter valid details")