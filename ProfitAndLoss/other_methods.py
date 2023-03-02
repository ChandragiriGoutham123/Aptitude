from fractions import Fraction
from colorama import Fore

number_of_inputs = int(input("Enter number of inputs : "))
total_answers_rs = []
total_answers_percentage = []

for i in range(number_of_inputs):
    find_the_value = input("choose one to find among\n  '7.loss%(gain%=loss%)'"
                               "'8.gain%(using false weight)"
                               "'9.gain%(using % of false weight)'"
                               "'10.Gain% or loss%(using % of false weight): ").lower()

    if find_the_value == "7":
        loss_percentage = Fraction(input("Enter  common loss and gain percentage (%): "))
        print("if loss and gain percentages are same the loss occurs")
        print("To find loss percentage while common percentage given we use")
        print("loss%=(common gain and loss percentage/10)**2")

        total_loss_percentage = float(round((loss_percentage / 10) ** 2, 2))

        if total_loss_percentage >= 0:
            total_loss_percentage = total_answers_percentage + [total_loss_percentage]
            print(Fore.YELLOW + "LOSS% : " + str(total_loss_percentage) + " %" + " ---------- " + str(i + 1))

        else:
            print(Fore.RED + "Enter valid details")

    elif find_the_value == "8":
        true_weight = Fraction(input("Enter True Weight (in grams): "))
        false_weight = Fraction(input("Enter False weight(in grams): "))
        print("if we use false weight there is always a gain")
        print("To find gain% we use :")
        print("Gain%=((true weight-false weight)/(true weight)-(true weight-false weight))*100")
        gain_percentage = float\
            (round(((true_weight - false_weight) /((true_weight)-(true_weight - false_weight)))*100, 2))

        if gain_percentage >= 0:
            total_answers_percentage = total_answers_percentage + [gain_percentage]
            print(Fore.YELLOW + "Gain percentage : " + str(gain_percentage) + " %" + " ---------- " + str(i + 1))

        else:
            print("enter valid details")

    elif find_the_value == "9":
        profit_percentage = Fraction(input("Enter profit percentage(x) (%): "))
        false_weight_percentage = Fraction(input("Enter percentage of false weight which "
                                                 "less than true weight(y) (%): "))
        print("To find total gain percentage we use :")
        print("gain%=((x+y)/(100-y))*100")
        total_gain_percentage = \
            float(round(((profit_percentage + false_weight_percentage) / (100 - false_weight_percentage)) * 100, 2))

        if total_gain_percentage >= 0:
            total_answers_percentage = total_answers_percentage + [total_gain_percentage]
            print(Fore.YELLOW + "Gain% : " + str(total_gain_percentage) + " %" + " ---------- " + str(i + 1))

        else:
            print("Enter valid details")

    elif find_the_value == "10":
        loss_percentage = Fraction(input("Enter loss percentage(x) (%): "))
        false_weight_percentage = Fraction(input("Enter percentage of false weight which "
                                                 "less than true weight(y) (%): "))
        print("To find total gain or loss percentage we use :")
        print("gain% or loss%=((y-x)/(100-y))*100")
        total_gain_or_loss_percentage = float(
            round(((false_weight_percentage - loss_percentage) / (100 - false_weight_percentage)) * 100, 2))

        if total_gain_or_loss_percentage > 0:
            total_answers_percentage = total_answers_percentage + [total_gain_or_loss_percentage]
            print(Fore.YELLOW + "Gain% : " + str(total_gain_or_loss_percentage) + " %" + " ---------- " + str(i + 1))

        elif total_gain_or_loss_percentage == 0:
            print(Fore.YELLOW + "No Gain and No loss")

        elif total_gain_or_loss_percentage < 0:
            total_gain_or_loss_percentage = total_gain_or_loss_percentage * (-1)
            total_answers_percentage = total_answers_percentage + [total_gain_or_loss_percentage]
            print(Fore.YELLOW + "loss% : " + str(total_gain_or_loss_percentage) + " %" + " ---------- " + str(i + 1))

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
