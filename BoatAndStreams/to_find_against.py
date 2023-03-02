import colorama
from colorama import Fore
from fractions import Fraction

number_of_inputs = int(input("Enter number of inputs : "))
speeds_boats = []
speeds_stream = []
times = []
distances = []
for i in range(number_of_inputs):
    direction_of_stream_towards_boat = input("ender direction of stream as  'against' : ").lower()
    print("Direction of stream : "+direction_of_stream_towards_boat)
    if direction_of_stream_towards_boat == "against":
        print(Fore.GREEN+" you can find only one value by placing '?'")
        distance = input("enter distance: ")
        print("Distance : "+distance+" km")
        speed_of_boat = input("enter speed of boat: ")
        print("Speed of boat : "+speed_of_boat+" km/hr")
        speed_of_stream = input("enter speed of stream : ")
        print("Speed of stream : "+speed_of_stream+" km/hr")
        time = input("enter time : ")
        print("Time : "+time+" hr")
        if distance == "?":
            formula = "Time = Distance/(speed of boat-speed of stream)"
            print("if boat goes against the direction of stream : ")
            print(formula)
            speed_of_boat = Fraction(speed_of_boat)
            speed_of_stream = Fraction(speed_of_stream)
            time = Fraction(time)
            print("i.e Distance=(Speed of boat+speed of stream)*(Time)")
            total_distance = float(round((speed_of_boat-speed_of_stream)*(time), 2))
            if total_distance >= 0:
                distances = distances + [total_distance]
                print(" ")
                print(Fore.GREEN+"Distance : "+str(total_distance)+" km"+" ---------- "+str(i+1))
                print(" ")
            else:
                print(Fore.RED + "Invalid details")
        elif time == "?":
            formula = "Time = Distance/(speed of boat-speed of stream)"
            print("if boat goes against the direction of stream : ")
            print(formula)
            speed_of_boat = Fraction(speed_of_boat)
            speed_of_stream = Fraction(speed_of_stream)
            distance = Fraction(distance)
            total_time = float(round(distance/(speed_of_boat-speed_of_stream), 2))
            if total_time >= 0:
                times = times + [total_time]
                print(" ")
                print(Fore.GREEN+"Time : "+str(total_time)+" hr"+" ---------- "+str(i+1))
                print(" ")
            else:
                print(Fore.RED + "Invalid details")
        elif speed_of_boat == "?":
            formula = "Time = Distance/(speed of boat-speed of stream)"
            print("if boat goes against the direction of stream : ")
            print(formula)
            time = Fraction(time)
            speed_of_stream = Fraction(speed_of_stream)
            distance = Fraction(distance)
            print("i.e speed of boat=(Distance/Time)-speed of boat")
            total_speed_of_boat = float(round((distance/time)+speed_of_stream, 2))

            if total_speed_of_boat >= 0:
                speeds_boats = speeds_boats + [total_speed_of_boat]
                print(" ")
                print(Fore.GREEN+"Speed of boat : "+str(total_speed_of_boat)+" km/hr"+" ---------- "+str(i+1))
                print(" ")
            else:
                print(Fore.RED + "Invalid details")
        elif speed_of_stream == "?":
            formula = "Time = Distance/(speed of boat-speed of stream)"
            print("if boat goes against the direction of stream : ")
            print(formula)
            time = Fraction(time)
            speed_of_boat = Fraction(speed_of_boat)
            distance = Fraction(distance)
            print("i.e speed of stream=(Distance/Time)-speed_of_stream")
            total_speed_of_stream = float(round((distance/time)+speed_of_boat, 2))

            if total_speed_of_stream >= 0:
                speeds_stream = speeds_stream + [total_speed_of_stream]
                print(" ")
                print(Fore.GREEN+"Speed of stream : "+str(total_speed_of_stream)+" km/hr"+" ---------- "+str(i+1))
                print(" ")
            else:
                print(Fore.RED + "Invalid details")
if len(distances) > 0:
    total_distances = []
    for long in distances:
        total_distances = total_distances + [str(long)+" Km"]
    total_distances_in_strings = "the distances = "
    for cdistances in total_distances:
        total_distances_in_strings = total_distances_in_strings + "  " + cdistances
    print(total_distances_in_strings)
if len(times) > 0:
    total_times = []
    for hours in times:
        total_times = total_times + [str(hours)+" hr"]
    total_times_in_strings = "the time = "
    for ctimes in total_times:
        total_times_in_strings = total_times_in_strings + "  " + ctimes
    print(total_times_in_strings)
if len(speeds_boats) > 0:
    total_boats = []
    for kmhr in speeds_boats:
        total_boats = total_boats + [str(kmhr)+" Km/hr"]
    total_speeds_boats_in_strings = "the speeds of boats = "
    for cbboats in total_boats:
        total_speeds_boats_in_strings = total_speeds_boats_in_strings + "  " + cbboats
    print(total_speeds_boats_in_strings)
if len(speeds_stream) > 0:
    total_streams = []
    for hrkm in speeds_stream:
        total_streams = total_streams + [str(hrkm)+" Km/hr"]
    total_speeds_streams_in_strings = "the stream speed = "
    for cbstreams in total_streams:
        total_speeds_streams_in_strings = total_speeds_streams_in_strings + " " + cbstreams
    print(total_speeds_streams_in_strings)
