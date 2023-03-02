from fractions import Fraction
from colorama import Fore

number_of_inputs = int(input("Enter number of inputs : "))
total_answers_rs = []
total_answers_percentage = []

for i in range(number_of_inputs):
    find_the_value = input("choose one to find among\n  '3.profit' '4.profit percentage' "
                           "'5.loss'\n '6.loss percentage': ").lower()
    if find_the_value == "3":
        sp = Fraction(input("Enter Selling price : RS."))
        cp = Fraction(input("Enter Cost price : RS. "))
        print("profit=selling price - cost price")
        profit = float(round(sp - cp, 2))

        if profit >= 0:
            total_answers_rs = total_answers_rs + [profit]
            print(Fore.YELLOW + "Profit : RS." + str(profit) + " ---------- " + str(i + 1))

        else:
            print(Fore.RED + "You Entered Invalid details please "
                             "check once(selling price always greater than cost price)")

    elif find_the_value == "5":
        sp = Fraction(input("Enter Selling price : RS."))
        cp = Fraction(input("Enter Cost price : RS. "))
        print("profit=cost price - selling price")
        loss = float(round(cp - sp, 2))

        if loss >= 0:
            total_answers_rs = total_answers_rs + [loss]
            print(Fore.YELLOW + "loss : RS." + str(loss) + " ---------- " + str(i + 1))

        else:
            print(Fore.RED + "You Entered Invalid details"
                             " please check once(cost price always greater than selling price)")
    elif find_the_value == "4":
        sp = Fraction(input("Enter Selling price : RS."))
        cp = Fraction(input("Enter Cost price : RS. "))
        print("Profit Percentage=((selling price-cost price)/cost price)*100")
        profit_percentage = float(round(((sp - cp) / cp) * 100, 2))

        if profit_percentage >= 0:
            total_answers_percentage = total_answers_percentage + [profit_percentage]
            print(Fore.YELLOW + "Profit Percentage : " + str(profit_percentage) + " %" + " ---------- " + str(i + 1))

        else:
            print(Fore.RED + "You Entered Invalid details please "
                             "check once(selling price always greater than cost price)")
    elif find_the_value == "6":
        sp = Fraction(input("Enter Selling price : RS."))
        cp = Fraction(input("Enter Cost price : RS. "))
        print("loss Percentage=((cost price-selling price)/cost price)*100")
        loss_percentage = float(round(((cp - sp) / cp) * 100, 2))

        if loss_percentage >= 0:
            total_answers_percentage = total_answers_percentage + [loss_percentage]
            print(Fore.YELLOW + "loss Percentage : " + str(loss_percentage) + " %" + " ---------- " + str(i + 1))

        else:
            print(Fore.RED + "You Entered Invalid details please check once(cost price always "
                             "greater than selling price)")

if len(total_answers_rs) > 0:
    total_answers_in_rss = []

    for rupees in total_answers_rs:
        total_answers_in_rss = total_answers_in_rss + ["RS." + str(rupees)]

    print(" ")
    print(total_answers_in_rss)
if len(total_answers_percentage) > 0:
    total_answers_percentages = []

    for percentages in total_answers_percentage:
        total_answers_percentages = total_answers_percentages + [str(percentages) + " %"]
    print(" ")
    print(total_answers_percentages)
