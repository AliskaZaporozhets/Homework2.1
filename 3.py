# a = input ("Enter number of minutes, please: ")
#
# b = (int (a)) // 60
# c = (int (a)) % 60
# print ( "Your period is: ", b, "hours and", c, "minutes.")


a = int (input ("Enter a number of minutes, please: "))
div, mod = divmod (a, 60)

print ("Your period is: ", div, "hours and", mod, 'minutes.')

