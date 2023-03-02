
from fractions import Fraction
from colorama import Fore
number_of_inputs = int(input("Enter number of inputs : "))
total_answers_rs = []
total_answers_percentage = []
for i in range(number_of_inputs):
        find_the_value = input("choose '1 'to find  '1.cost price' : ").lower()
        if find_the_value == "1":

            find_profit = input("Select one input among 'Profit' and 'profit%' 'loss' 'loss%' as"
                                " input: ").lower()
            if find_profit == "profit":

                profit = Fraction(input("Enter the amount of profit : RS. "))
                sp = Fraction(input("Enter Selling price : RS. "))
                print("To find Cost price we use :")
                print("CP=SP-PROFIT")
                cost_price = float(round(sp-profit, 2))
                if cost_price >= 0:
                    total_answers_rs = total_answers_rs + [cost_price]
                    print("Cost Price : RS."+str(cost_price)+" ---------- "+str(i+1))
                else:
                    print(Fore.RED+"You Entered Invalid details please check once(sp always greater than profit)")
            elif find_profit == "profit%":

                profit_percentage = Fraction(input("Enter the percentage of profit (%): "))
                sp = Fraction(input("Enter Selling price : RS. "))
                print("To find Cost price we use :")
                print("CP=100*sp/(profit%+100)")
                cost_price = float(round((100*sp)/(profit_percentage+100), 2))
                if cost_price >= 0:
                    total_answers_rs = total_answers_rs + [cost_price]
                    print(Fore.YELLOW + "Cost Price : RS." + str(cost_price)+" ---------- "+str(i+1))
                else:
                    print(Fore.RED + "You Entered Invalid details please check once")
            elif find_profit == "loss":

                loss = Fraction(input("Enter the amount of loss : RS. "))
                sp = Fraction(input("Enter Selling price : RS. "))
                print("To find Cost price we use :")
                print("CP=SP+LOSS")
                cost_price = float(round(sp+loss, 2))
                if cost_price >= 0:
                    total_answers_rs = total_answers_rs + [cost_price]
                    print(Fore.YELLOW+"Cost Price : RS."+str(cost_price)+" ---------- "+str(i+1))
                else:
                    print(Fore.RED+"You Entered Invalid details please check once")
            elif find_profit == "loss%":

                loss_percentage = Fraction(input("Enter the percentage of loss (%): "))
                sp = Fraction(input("Enter Selling price : RS. "))
                print("To find Cost price we use :")
                print("CP=100*sp/(100-loss%)")
                cost_price = float(round((100*sp)/(100-loss_percentage), 2))
                if cost_price >= 0:
                    total_answers_rs = total_answers_rs + [cost_price]
                    print(Fore.YELLOW + "Cost Price : RS." + str(cost_price)+" ---------- "+str(i+1))
                else:
                    print(Fore.RED + "You Entered Invalid details please check once")
            else:
                print(Fore.RED+"Enter valid details")
if len(total_answers_rs) > 0:
    total_answers_in_rss = []
    for rupees in total_answers_rs:
        total_answers_in_rss = total_answers_in_rss + ["RS." + str(rupees)]
    print(" ")
    print(total_answers_in_rss)