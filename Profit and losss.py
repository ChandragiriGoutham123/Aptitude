

from fractions import Fraction
from colorama import Fore
number_of_inputs = int(input("Enter number of inputs : "))
total_answers_rs = []
total_answers_percentage = []
for i in range(number_of_inputs):
        find_the_value = input("choose one to find among\n '1.cp' '2.sp' '3.profit' '4.profit percentage' "
                               "'5.loss'\n '6.loss percentage''7.loss%(gain%=loss%)'"
                               "'8.gain%(using false weight)"
                               "'9.gain%(using % of false weight)'"
                               "'10.Gain% or loss%(using % of false weight): ").lower()
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
        elif find_the_value == "2":

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
        elif find_the_value == "3":
            sp = Fraction(input("Enter Selling price : RS."))
            cp = Fraction(input("Enter Cost price : RS. "))
            print("profit=selling price - cost price")
            profit = float(round(sp-cp, 2))
            if profit >= 0:
                total_answers_rs = total_answers_rs+[profit]
                print(Fore.YELLOW+"Profit : RS."+str(profit)+" ---------- "+str(i+1))
            else:
                print(Fore.RED + "You Entered Invalid details please "
                                 "check once(selling price always greater than cost price)")

        elif find_the_value == "5":
            sp = Fraction(input("Enter Selling price : RS."))
            cp = Fraction(input("Enter Cost price : RS. "))
            print("profit=cost price - selling price")
            loss = float(round(cp-sp, 2))
            if loss >= 0:
                total_answers_rs = total_answers_rs + [loss]
                print(Fore.YELLOW+"loss : RS."+str(loss)+" ---------- "+str(i+1))
            else:
                print(Fore.RED + "You Entered Invalid details"
                                 " please check once(cost price always greater than selling price)")
        elif find_the_value == "4":
            sp = Fraction(input("Enter Selling price : RS."))
            cp = Fraction(input("Enter Cost price : RS. "))
            print("Profit Percentage=((selling price-cost price)/cost price)*100")
            profit_percentage = float(round(((sp-cp)/cp)*100, 2))
            if profit_percentage >= 0:
                total_answers_percentage = total_answers_percentage + [profit_percentage]
                print(Fore.YELLOW+"Profit Percentage : "+str(profit_percentage)+" %"+" ---------- "+str(i+1))
            else:
                print(Fore.RED + "You Entered Invalid details please "
                                 "check once(selling price always greater than cost price)")
        elif find_the_value == "6":
            sp = Fraction(input("Enter Selling price : RS."))
            cp = Fraction(input("Enter Cost price : RS. "))
            print("loss Percentage=((cost price-selling price)/cost price)*100")
            loss_percentage = float(round(((cp-sp)/cp)*100, 2))
            if loss_percentage >= 0:
                total_answers_percentage = total_answers_percentage + [loss_percentage]
                print(Fore.YELLOW+"loss Percentage : "+str(loss_percentage)+" %"+" ---------- "+str(i+1))
            else:
                print(Fore.RED + "You Entered Invalid details please check once(cost price always "
                                 "greater than selling price)")
        elif find_the_value == "7":
            loss_percentage = Fraction(input("Enter  common loss and gain percentage (%): "))
            print("if loss and gain percentages are same the loss occurs")
            print("To find loss percentage while common percentage given we use")
            print("loss%=(common gain and loss percentage/10)**2")

            total_loss_percentage = float(round((loss_percentage/10)**2, 2))
            if total_loss_percentage >= 0:
                total_loss_percentage = total_answers_percentage + [total_loss_percentage]
                print(Fore.YELLOW+"LOSS% : "+str(total_loss_percentage)+" %"+" ---------- "+str(i+1))
            else:
                print(Fore.RED+"Enter valid details")
        elif find_the_value == "8":
            true_weight = Fraction(input("Enter True Weight (in grams): "))
            false_weight = Fraction(input("Enter False weight(in grams): "))
            print("if we use false weight there is always a gain")
            print("To find gain% we use :")
            print("Gain%=((true weight-false weight)/(true weight)-(true weight-false weight))*100")
            gain_percentage = float(round(((true_weight-false_weight)/((true_weight)-(true_weight-false_weight)))*100, 2))
            if gain_percentage >= 0:
                total_answers_percentage = total_answers_percentage + [gain_percentage]
                print(Fore.YELLOW+"Gain percentage : "+str(gain_percentage)+" %"+" ---------- "+str(i+1))
            else:
                print("enter valid details")

        elif find_the_value == "9":
            profit_percentage = Fraction(input("Enter profit percentage(x) (%): "))
            false_weight_percentage = Fraction(input("Enter percentage of false weight which "
                                                     "less than true weight(y) (%): "))
            print("To find total gain percentage we use :")
            print("gain%=((x+y)/(100-y))*100")
            total_gain_percentage = \
                float(round(((profit_percentage+false_weight_percentage)/(100-false_weight_percentage))*100, 2))
            if total_gain_percentage >= 0:
                total_answers_percentage = total_answers_percentage + [total_gain_percentage]
                print(Fore.YELLOW+"Gain% : "+str(total_gain_percentage)+" %"+" ---------- "+str(i+1))
            else:
                print("Enter valid details")
        elif find_the_value == "10":
            loss_percentage = Fraction(input("Enter loss percentage(x) (%): "))
            false_weight_percentage = Fraction(input("Enter percentage of false weight which "
                                                     "less than true weight(y) (%): "))
            print("To find total gain or loss percentage we use :")
            print("gain% or loss%=((y-x)/(100-y))*100")
            total_gain_or_loss_percentage = float(
                round(((false_weight_percentage-loss_percentage) / (100 - false_weight_percentage)) * 100, 2))
            if total_gain_or_loss_percentage > 0:
                total_answers_percentage = total_answers_percentage + [total_gain_or_loss_percentage]
                print(Fore.YELLOW + "Gain% : " + str(total_gain_or_loss_percentage) + " %"+" ---------- "+str(i+1))
            elif total_gain_or_loss_percentage == 0:
                print(Fore.YELLOW+"No Gain and No loss")
            else:
                total_gain_or_loss_percentage = total_gain_or_loss_percentage*(-1)
                total_answers_percentage = total_answers_percentage + [total_gain_or_loss_percentage]
                print(Fore.YELLOW + "loss% : " + str(total_gain_or_loss_percentage) + " %"+" ---------- "+str(i+1))
if len(total_answers_rs) > 0:
    total_answers_in_rss=[]
    for rupees in total_answers_rs:
          total_answers_in_rss = total_answers_in_rss + ["RS." + str(rupees)]
    print(" ")
    print(total_answers_in_rss)
if len(total_answers_percentage) > 0:
    total_answers_percentages = []
    for percentages in  total_answers_percentage:
        total_answers_percentages = total_answers_percentages + [str(percentages)+" %"]
    print(" ")
    print(total_answers_percentages)
