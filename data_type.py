# #String
# robot_name = "Robot Sau"

# #integer 
# age = "10" 
# height = 1.90

# # boolean 
# is_active = True  

# # NoneType
# warning = None

# # print("I Have a robot named", robot_name, ". It aged", age, ".")
# # print(f"I have a robot named {robot_name}. It aged {age}.")

# distance_a = 4.2
# distance_b = 20

# print("Distance A:", distance_a )
# print("Distance B:", distance_b)

# print("Total distance:", distance_a + distance_b)
# print("Multiplication distance:", distance_a * distance_b)
# print("division distance:", distance_a / distance_b)

# x = 9
# y = 7
# z = x and y

# print("x/y=", x/y)
# print("x//y=", x//y)
# print("x%y=", x%y)
# print("z:", z )

# a = 2
# b == 4
# c != 5

x_min, x_max = 9.8, 11.20

pos_x = 10.45
is_safe = (pos_x >= x_min and pos_x <= x_max)
print("Is that safe:", is_safe) 
# if pos_x < x_min:
#     print("Position is below the minimu limit.")
# elif pos_x > x_max:
#     print("Position is above the maximum limit.")
# else: 
#     print("Position is within the acceptable range.")

for pos_x in [8.5, 9.5, 10.5,11.5]:
    print(pos_x)

telemetry_line = "Status: OK ID: 4 Margin: LV3"

field = telemetry_line.split(" ")
status = field[1]

print(status)