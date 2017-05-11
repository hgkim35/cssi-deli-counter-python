katz_deli = []

#1. line() function that shows everyone their current place in line. If there's nobody in line, it should say "The line is currently empty.
def line(katz_deli):
    deli_list_string = "The line is currently:"
    for i in range(0, len(katz_deli)):
        deli_list_string += str(i+1) + ". "+ katz_deli[i]
    if len(katz_deli) == 0:
        return "The line is currently empty."
    return deli_list_string
# #2. take_a_number function should accept two arguments: the list for the current line of people (katz_deli) and a string containing the name of the person wishing to join the line. The function should return the person's name along with their position in line.
#
def take_a_number(katz_deli, name):
    katz_deli.append(name)
        return "Welcome, " + name + "." + " You are number " + str(len(katz_deli)) " in line."

#
# #3. now_serving() function should call out (print) the next person in line and then remove them from the front. If there's nobody in line, it should print "There is nobody waiting to be served!"
#

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        return "There is nobody waiting to be served!"
    katz_deli.pop(0)
        return "Currently serving " + katz_deli[0] + "."
