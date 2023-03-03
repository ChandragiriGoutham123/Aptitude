from fractions import Fraction

number_of_inputs = int(input("Enter number of inputs : "))

for i in range(number_of_inputs):
   input_selection = input("select one between '1.True discount and banker discount' or '2.banker discount "
                                                  "and banker gain : ")
   if input_selection == "1":
       print("let take true discount as 1 Rs")
       time = Fraction(input("Enter time in years : "))
       true_discount = 1
       banker_discount = Fraction(input("Enter fraction of banker discount : "))
       banker_discount = Fraction(banker_discount)
       total_sum = round(float((banker_discount*true_discount)/(banker_discount-true_discount)))
       rate = round(float((100*banker_discount)/(total_sum*time)), 2)
       if rate >= 0:
           print("rate : "+str(rate)+"%  ---------- "+str(i+1))
           print(" ")
       else:
           print("Enter valid details")
   elif input_selection == "2":
       print("let take bankers discount as 1 Rs")
       time = Fraction(input("Enter time in years : "))
       banker_discount = 1
       banker_gain = Fraction(input("Enter fraction of banker gain : "))
       true_discount = round(float(banker_discount-banker_gain), 2)
       total_sum = round(float((banker_discount*true_discount)/(banker_discount-true_discount)), 2)
       rate = round(float((100*banker_discount)/(total_sum*time)), 2)
       if rate >= 0:
           print("rate : "+str(rate)+" %"+ " ---------- "+str(i+1))
           print(" ")
       else:
           print("Enter valid details")


