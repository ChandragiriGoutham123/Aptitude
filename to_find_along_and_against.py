import colorama
from colorama import Fore
from fractions import Fraction


number_of_inputs = int(input("Enter number of inputs : "))
speeds_boats = []
speeds_stream = []
times = []
distances = []
for i in range(number_of_inputs):
    direction_of_stream_towards_boat = input("enter direction of stream towards 'along and against': ").lower()
    print("Direction of stream : "+direction_of_stream_towards_boat)
    if direction_of_stream_towards_boat == "along and against" or direction_of_stream_towards_boat == \
            "against and along":
        downstream_distance = input("Enter downstream distance : ")
        print("Downstream distance : " + downstream_distance + " km")
        downstream_time = input("Enter downstream time : ")
        print("Downstream time : " + downstream_time + " hr")
        upstream_distance = input("Enter upstream distance :")
        print("Upstream Distance : " + upstream_distance + " km")
        upstream_time = input("enter upstream time: ")
        print("Upstream time : " + upstream_time + " hr")
        print("downstream speed=downstream distance/downstream time")
        downstream_speed = float(round((Fraction(downstream_distance) / Fraction(downstream_time)), 2))
        print("Downstream speed : " + str(downstream_speed) + " km/hr")
        print("upstream speed=upstream distance/upstream time")
        upstream_speed = float(round((Fraction(upstream_distance) / Fraction(upstream_time)), 2))
        print("Upstream speed : " + str(upstream_speed) + " km/hr")
        speed = input("Enter 'speed of boat' or 'speed of stream' or 'both':").lower()
        if speed == "speed of boat":
            print("Speed of boat=(downstream speed+upstream speed)/2")
            speed_of_boat = float(round((Fraction(downstream_speed) + Fraction(upstream_speed)) / 2, 2))
            if speed_of_boat >= 0:
                speeds_boats = speeds_boats + [speed_of_boat]
                print(Fore.GREEN + "Speed of boat : " + str(speed_of_boat) + " km/hr" + " ---------- " + str(i + 1))
                print(" ")
            else:
                print(Fore.RED + "Invalid details")
        elif speed == "speed of stream":
            print("Speed of stream=(downstream speed-upstream speed)/2")
            speed_of_stream = float(round((Fraction(downstream_speed) - Fraction(upstream_speed)) / 2, 2))
            if speed_of_stream >= 0:
                speeds_stream = speeds_stream + [speed_of_stream]
                print(Fore.GREEN + "Speed of stream : " + str(speed_of_stream) + " km/hr" + " ---------- " + str(i + 1))
                print(" ")
            else:
                print(Fore.RED + "Invalid details")
        elif speed == "both":
            print("Speed of boat=(downstream speed+upstream speed)/2")
            print("Speed of stream=(downstream speed-upstream speed)/2")
            speed_of_boat = float(round((Fraction(downstream_speed) + Fraction(upstream_speed)) / 2, 2))

            if speed_of_boat >= 0:
                speeds_boats = speeds_boats + [speed_of_boat]
                print(Fore.GREEN + "Speed of boat : " + str(speed_of_boat) + " km/hr" + " ---------- " + str(i + 1))
                print(" ")
            else:
                print(Fore.RED + "Invalid details")
            speed_of_stream = float(round((Fraction(downstream_speed) - Fraction(upstream_speed)) / 2, 2))
            if speed_of_stream >= 0:
                speeds_stream = speeds_stream + [speed_of_stream]
                print(Fore.GREEN + "Speed of stream : " + str(speed_of_stream) + " km/hr" + " ---------- " + str(i + 1))
                print(" ")
            else:
                print(Fore.RED + "Invalid details")

if len(distances) > 0:
    total_distances = []
    for long in distances:
        total_distances = total_distances + [str(long) + " Km"]
    total_distances_in_strings = "the distances = "
    for cdistances in total_distances:
        total_distances_in_strings = total_distances_in_strings + "  " + cdistances
    print(total_distances_in_strings)
if len(times) > 0:
    total_times = []
    for hours in times:
        total_times = total_times + [str(hours) + " hr"]
    total_times_in_strings = "the time = "
    for ctimes in total_times:
        total_times_in_strings = total_times_in_strings + "  " + ctimes
    print(total_times_in_strings)
if len(speeds_boats) > 0:
    total_boats = []
    for kmhr in speeds_boats:
        total_boats = total_boats + [str(kmhr) + " Km/hr"]
    total_speeds_boats_in_strings = "the speeds of boats = "
    for cbboats in total_boats:
        total_speeds_boats_in_strings = total_speeds_boats_in_strings + "  " + cbboats
    print(total_speeds_boats_in_strings)
if len(speeds_stream) > 0:
    total_streams = []
    for hrkm in speeds_stream:
        total_streams = total_streams + [str(hrkm) + " Km/hr"]
    total_speeds_streams_in_strings = "the stream speed = "
    for cbstreams in total_streams:
        total_speeds_streams_in_strings = total_speeds_streams_in_strings + " " + cbstreams
    print(total_speeds_streams_in_strings)




