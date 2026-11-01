# # from utils import is_within_margin
# from utils import *

# value =95
# target = 100
# margin = 10

# print(is_within_margin(value, target, margin))

# kibo = [10,20,5]

import math

flight_path = []
# s1
flight_path.append([10.71, -1.90, 4.85])

# s2
flight_path.append([11.50, -1.50, 5.00])

# s3
flight_path.append([12.10, -0.80, 4.95])

print(flight_path)

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 +
                     (p2[1] - p1[1])**2 +
                     (p2[2] - p1[2])**2)

s1 = flight_path[0]
s2 = flight_path[1]
s3 = flight_path[2]

dist_s2_s1 = euclidean_distance(s2, s1)
dist_s3_s1 = euclidean_distance(s3, s1)

print(f"Distance s2 -> s1: {dist_s2_s1:.3f} m")
print(f"Distance s3 -> s1: {dist_s3_s1:.3f} m")