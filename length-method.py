material = ['SAND', 'DUST', 'LEAVES', 'PAPER', 'TIN', 'ROOTS', 'BRICK', 'STONE', 'DISCARDED CLOTHING', 'GLASS', 'STEEL', 'PLASTIC', 'MUD', 'BROKEN DISHES', 'WOOD', 'STRAW', 'WEEDS']

location = ['IN A GREEN, MOSSY TERRAIN', 'IN AN OVERPOPULATED AREA', 'BY THE SEA', 'BY AN ABANDONED LAKE', 'IN A DESERTED FACTORY', 'IN DENSE WOODS', 'IN JAPAN', 'AMONG SMALL HILLS', 'IN SOUTHERN FRANCE', 'AMONG HIGH MOUNTAINS', 'ON AN ISLAND', 'IN A COLD, WINDY CLIMATE', 'IN A PLACE WITH BOTH HEAVY RAIN AND BRIGHT SUN', 'IN A DESERTED AIRPORT', 'IN A HOT CLIMATE', 'INSIDE A MOUNTAIN', 'ON THE SEA', 'IN MICHIGAN', 'IN HEAVY JUNGLE UNDERGROWTH', 'BY A RIVER', 'AMONG OTHER HOUSES', 'IN A DESERTED CHURCH', 'IN A METROPOLIS', 'UNDERWATER']

light_source = ['CANDLES', 'ALL AVAILABLE LIGHTING', 'ELECTRICITY', 'NATURAL LIGHT']


my_string = 'This is just a lonely string'

print(my_string)
# print(myString[0:10])
print('andy this the type mystring ', type(my_string))
print(type(light_source))

another_string = location[3]
print('another type is ', type(another_string))
new_v = my_string.upper()
print(new_v)

#to split a string into a list use the .split() method
am_I_string = my_string.split()
print(am_I_string)
print('am i a string is ', type(am_I_string))
# print(am_I_string[-1:])

#this is a Boolean data type, we didn't talk about this, but it resolves to either True or False
# my_variable = True
# print(my_variable)
# print(type(my_variable))

#the join method uses a seperator to connect items in a list. it turns a list into a string
new_variable = ' '.join(am_I_string)
vatIsEs = ' '.join(location)
print(new_variable)
print(vatIsEs)

print()
print()

my_list = []
this_element = ''

#This was the original way I made the snowball before I wrapped it in a funciton
# for i in am_I_string:
#     this_element = this_element +" " + i
#     print(this_element)

# my_calc = 4 + 5000
# print(my_calc)

new_string = "I don't like Mondays"
new_list = new_string.split()

#This is a slightly simpler way of making this program than the one below that I did during the video tutorial
def simple_snow(list_of_text):
    this_new_string = ''
    for i in list_of_text:
        this_new_string = this_new_string + " " + i
        print(this_new_string)

print(simple_snow(new_list))

#global scope is when you want to refer to a variable outside of the funciton. it can be called inside and outside the function
def make_a_snowball(text):
    make_a_snowball.this_string = ''
    for i in text:
        make_a_snowball.this_string = make_a_snowball.this_string + " " + i
        print(make_a_snowball.this_string)
make_a_snowball.this_string = ''

# print(make_a_snowball(new_list))