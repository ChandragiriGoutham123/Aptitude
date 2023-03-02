
from fractions import Fraction
from colorama import Fore
number_of_inputs = int(input("Enter number of inputs : "))
total_answers_rs = []
total_answers_percentage = []
for i in range(number_of_inputs):
    find_the_value = input("choose '2' to find  '2.selling price' : ").lower()

    if find_the_value == "2":

        find_profit = input("Select one input among 'Profit' and 'profit%' 'loss' 'loss%': ").lower()

        if find_profit == "profit":

            profit = Fraction(input("Enter the amount of profit : RS. "))
            cp = Fraction(input("Enter Cost price : RS. "))
            print("To find Selling price we use :")
            print("SP=CP+PROFIT")
            selling_price = float(round(cp+profit, 2))

            if selling_price >= 0:

                total_answers_rs = total_answers_rs + [selling_price]
                print(Fore.YELLOW+"Selling Price : RS."+str(selling_price)+" ---------- "+str(i+1))

            else:
                print(Fore.RED+"You Entered Invalid details please check once")

        elif find_profit == "profit%":

            profit_percentage = Fraction(input("Enter the percentage of profit (%):  "))
            cp = Fraction(input("Enter Cost price : RS. "))
            print("To find Selling price we use :")
            print("SP=CP*(100+PROFIT PERCENTAGE)/100")
            selling_price = float(round(cp*(profit_percentage+100)/100, 2))
            if selling_price >= 0:

                total_answers_rs = total_answers_rs + [selling_price]
                print(Fore.YELLOW + "selling Price : RS." + str(selling_price)+" ---------- "+str(i+1))

            else:

                print(Fore.RED + "You Entered Invalid details "
                                 "please check once(selling price always greater than cost price)")
        elif find_profit == "loss":

            loss = Fraction(input("Enter the amount of loss : RS. "))
            cp = Fraction(input("Enter Cost price : RS. "))
            print("To find Selling price we use :")
            print("SP=CP-LOSS")
            selling_price = float(round(cp-loss, 2))
            if selling_price >= 0:
                total_answers_rs = total_answers_rs + [selling_price]
                print(Fore.YELLOW+"selling Price : RS."+str(selling_price)+" ---------- "+str(i+1))
            else:
                print(Fore.RED+"You Entered Invalid details please "
                               "check once(cost price always greater than selling price)")
        elif find_profit == "loss%":

            loss_percentage = Fraction(input("Enter the percentage of loss (%): "))
            cp = Fraction(input("Enter Cost price : RS. "))
            print("To find Selling price we use :")
            print("SP=CP*(100-LOSS%)/100")
            selling_price = float(round(cp*(100-loss_percentage)/100, 2))

            if selling_price >= 0:
                total_answers_rs = total_answers_rs + [selling_price]
                print(Fore.YELLOW + "selling Price : RS." + str(selling_price)+" ---------- "+str(i+1))

            else:
                print(Fore.RED + "You Entered Invalid details please "
                                 "check once(cost price always greater than selling price)")

        else:
            print(Fore.RED+"Enter valid details")

if len(total_answers_rs) > 0:

    total_answers_in_rss = []

    for rupees in total_answers_rs:

        total_answers_in_rss = total_answers_in_rss + ["RS." + str(rupees)]

    print(" ")
    print(total_answers_in_rss)