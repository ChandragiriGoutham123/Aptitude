from fractions import Fraction

number_of_inputs = int(input("Enter number of inputs : "))

for i in range(number_of_inputs):
   bankers_discount = Fraction(input("Enter bankers discount amount (RS) : "))
   true_discount = Fraction(input("Enter True discount amount (RS) : "))
   time_period_and_rate = input("select between '1.time and rate are same' or '2.time and rate are different' "
                                "as input: ")

   if time_period_and_rate == "1":
       rate = Fraction(input("Enter rate of interest (%): "))
       simple_interest = round(float(true_discount - bankers_discount), 2)
       time = round(float((simple_interest * 100)/(bankers_discount*rate)), 2)
       if time >= 0:

           print("Time : "+str(time)+" years"+"  ---------- "+str(i+1))
           print(" ")
       else:
           print("enter valid details")
   elif time_period_and_rate == "2":
       time_on_banker_discount = Fraction(input("Enter time on banker discount in Years : "))
       time_on_true_discount = Fraction(input("Enter time on true discount in years : "))
       real_banker_discount = round(float((bankers_discount*time_on_true_discount)/time_on_banker_discount), 2)
       print("Banker discount on time on true discount : "+str(real_banker_discount))
       total_sum = round(float((real_banker_discount*true_discount)/(real_banker_discount-true_discount)), 2)
       print("Total sum : RS. "+str(total_sum))
       rate = round(float((real_banker_discount*100)/(total_sum*time_on_true_discount)), 2)

       if rate >= 0:
           print("Rate : "+str(rate)+" %"+"  ---------- "+str(i+1))
           print("")
       else:
           print("Enter valid details")



