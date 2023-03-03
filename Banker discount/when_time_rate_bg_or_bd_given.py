from fractions import Fraction


number_of_inputs = int(input("Enter number of inputs : "))

for i in range(number_of_inputs):
    time = Fraction(input("Enter Time (years) : "))
    rate = Fraction(input("Enter rate (%) : "))
    bg_or_bd = input("select between '1.Bankers Gain' or '2.Bankers Discount' as input: ")

    if bg_or_bd == "1":
        bankers_gain = Fraction(input("Enter Bankers gain (RS): "))
        print("True discount = (Bankers gain * 100)/rate * time ")
        true_discount = round(float((bankers_gain*100)/(rate*time)), 2)

        if true_discount >= 0:

            print("True Discount :RS. "+str(true_discount)+"  ---------- "+str(i+1))
            print(" ")
        else:
            print("Enter valid details")
        print("present worth = (100*true discount)/rate*time")
        present_worth = round(float((100*true_discount)/(rate*time)), 2)

        if present_worth >= 0:

            print("present worth : RS. "+str(present_worth)+"  ---------- "+str(i+1))
            print(" ")
        else:
            print("Enter valid details")
        print("Bankers discount = true discount + bankers gain")
        bankers_discount = round(float(true_discount+bankers_gain), 2)

        if bankers_discount >= 0:

            print("Bankers discount : RS. "+str(bankers_discount)+"  ---------- "+str(i+1))
            print(" ")
        else:
            print("Enter valid details")
    if bg_or_bd == "2":
        bankers_discount = Fraction(input("Enter Bankers discount (RS): "))
        print("True discount = (Bankers discount * 100)/100+(rate * time) ")
        true_discount = round(float((bankers_discount * 100) / (100+(rate * time))), 2)

        if true_discount >= 0:

            print("True Discount :RS. " + str(true_discount) + "  ---------- " + str(i + 1))
            print(" ")
        else:
            print("Enter valid details")
        print("present worth = (100*true discount)/rate*time")
        present_worth = round(float((100 * true_discount) / (rate * time)), 2)

        if present_worth >= 0:

            print("present worth : RS. " + str(present_worth) + "  ---------- " + str(i + 1))
            print(" ")
        else:
            print("Enter valid details")
        print("Bankers gain = bankers discount - true discount")
        bankers_gain = round(float(bankers_discount-true_discount), 2)

        if bankers_gain >= 0:

            print("Bankers gain: RS. " + str(bankers_discount) + "  ---------- " + str(i + 1))
            print(" ")
        else:
            print("Enter valid details")

