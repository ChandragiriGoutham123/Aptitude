

from fractions import Fraction
from colorama import Fore

find_the_value = input("choose one to find among 'cp' 'sp' 'profit' 'profit percentage' 'loss' 'loss percentage': ").lower()
if find_the_value == "cp":

    find_profit = input("Select one input among 'Profit' and 'profit%' 'loss' 'loss%': ").lower()
    if find_profit == "profit":

        profit = Fraction(input("Enter the amount of profit : RS. "))
        sp = Fraction(input("Enter Selling price : RS. "))
        print("To find Cost price we use :")
        print("CP=SP-PROFIT")
        cost_price = float(round(sp-profit, 2))
        if cost_price >= 0:
            print(Fore.YELLOW+"Cost Price : RS."+str(cost_price))
        else:
            print(Fore.RED+"You Entered Invalid details please check once")
    elif find_profit == "profit%":

        profit_percentage = Fraction(input("Enter the percentage of profit (%): "))
        sp = Fraction(input("Enter Selling price : RS. "))
        print("To find Cost price we use :")
        print("CP=100*sp/(profit%+100)")
        cost_price = float(round((100*sp)/(profit_percentage+100), 2))
        if cost_price >= 0:
            print(Fore.YELLOW + "Cost Price : RS." + str(cost_price))
        else:
            print(Fore.RED + "You Entered Invalid details please check once")
    elif find_profit == "loss":

        loss = Fraction(input("Enter the amount of loss : RS. "))
        sp = Fraction(input("Enter Selling price : RS. "))
        print("To find Cost price we use :")
        print("CP=SP+LOSS")
        cost_price = float(round(sp+loss, 2))
        if cost_price >= 0:
            print(Fore.YELLOW+"Cost Price : RS."+str(cost_price))
        else:
            print(Fore.RED+"You Entered Invalid details please check once")
    elif find_profit == "loss%":

        loss_percentage = Fraction(input("Enter the percentage of loss (%): "))
        sp = Fraction(input("Enter Selling price : RS. "))
        print("To find Cost price we use :")
        print("CP=100*sp/(100-loss%)")
        cost_price = float(round((100*sp)/(100-loss_percentage), 2))
        if cost_price >= 0:
            print(Fore.YELLOW + "Cost Price : RS." + str(cost_price))
        else:
            print(Fore.RED + "You Entered Invalid details please check once")
    else:
        print(Fore.RED+"Enter valid details")
if find_the_value == "sp":

    find_profit = input("Select one input among 'Profit' and 'profit%' 'loss' 'loss%': ").lower()
    if find_profit == "profit":

        profit = Fraction(input("Enter the amount of profit : RS. "))
        cp = Fraction(input("Enter Cost price : RS. "))
        print("To find Selling price we use :")
        print("SP=CP+PROFIT")
        selling_price = float(round(cp+profit, 2))
        if selling_price >= 0:
            print(Fore.YELLOW+"Selling Price : RS."+str(selling_price))
        else:
            print(Fore.RED+"You Entered Invalid details please check once")
    elif find_profit == "profit%":

        profit_percentage = Fraction(input("Enter the percentage of profit (%):  "))
        cp = Fraction(input("Enter Cost price : RS. "))
        print("To find Selling price we use :")
        print("SP=CP*(100+PROFIT PERCENTAGE)/100")
        selling_price = float(round(cp*(profit_percentage+100)/100, 2))
        if selling_price >= 0:
            print(Fore.YELLOW + "selling Price : RS." + str(selling_price))
        else:
            print(Fore.RED + "You Entered Invalid details please check once(selling price always greater than cost price)")
    elif find_profit == "loss":

        loss = Fraction(input("Enter the amount of loss : RS. "))
        cp = Fraction(input("Enter Cost price : RS. "))
        print("To find Selling price we use :")
        print("SP=CP-LOSS")
        selling_price = float(round(cp-loss, 2))
        if selling_price >= 0:
            print(Fore.YELLOW+"selling Price : RS."+str(selling_price))
        else:
            print(Fore.RED+"You Entered Invalid details please check once(cost price always greater than selling price)")
    elif find_profit == "loss%":

        loss_percentage = Fraction(input("Enter the percentage of loss (%): "))
        cp = Fraction(input("Enter Cost price : RS. "))
        print("To find Selling price we use :")
        print("SP=CP*(100-LOSS%)/100")
        selling_price = float(round(cp*(100-loss_percentage)/100, 2))
        if selling_price >= 0:
            print(Fore.YELLOW + "selling Price : RS." + str(selling_price))
        else:
            print(Fore.RED + "You Entered Invalid details please check once(cost price always greater than selling price)")
    else:
        print(Fore.RED+"Enter valid details")
elif find_the_value == "profit":
    sp = Fraction(input("Enter Selling price : RS."))
    cp = Fraction(input("Enter Cost price : RS. "))
    print("profit=selling price - cost price")
    profit = float(round(sp-cp, 2))
    if profit >= 0:
        print(Fore.YELLOW+"Profit : RS."+str(profit))
    else:
        print(Fore.RED + "You Entered Invalid details please check once(selling price always greater than cost price)")

elif find_the_value == "loss":
    sp = Fraction(input("Enter Selling price : RS."))
    cp = Fraction(input("Enter Cost price : RS. "))
    print("profit=cost price - selling price")
    loss = float(round(cp-sp, 2))
    if loss >= 0:
        print(Fore.YELLOW+"loss : RS."+str(loss))
    else:
        print(Fore.RED + "You Entered Invalid details please check once(cost price always greater than selling price)")
elif find_the_value == "profit percentage":
    sp = Fraction(input("Enter Selling price : RS."))
    cp = Fraction(input("Enter Cost price : RS. "))
    print("Profit Percentage=((selling price-cost price)/cost price)*100")
    profit_percentage = float(round(((sp-cp)/cp)*100, 2))
    if profit_percentage >= 0:
        print(Fore.YELLOW+"Profit Percentage : "+str(profit_percentage)+" %")
    else:
        print(Fore.RED + "You Entered Invalid details please check once(selling price always greater than cost price)")
elif find_the_value == "loss percentage":
    sp = Fraction(input("Enter Selling price : RS."))
    cp = Fraction(input("Enter Cost price : RS. "))
    print("loss Percentage=((cost price-selling price)/cost price)*100")
    loss_percentage = float(round(((cp-sp)/cp)*100, 2))
    if loss_percentage >= 0:
        print(Fore.YELLOW+"loss Percentage : "+str(loss_percentage)+" %")
    else:
        print(Fore.RED + "You Entered Invalid details please check once(cost price always greater than selling price)")

