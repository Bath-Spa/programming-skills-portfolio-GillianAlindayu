# Chapter 3 Data structures 

#Exercise 1 : Names ballot_box_wth_check 
#Store the names of few of your friends in a list. Print each names by accessing each element in the list, one at the time.

names = ['Lai', 'Sam', 'Jam']

print(names[0])
print(names[1])
print(names[2])


# Exercise 2: Greetings ballot_box_with_check: 

#start with the list you used in exercise 1, but instead you just printing each person's name text of each message should be personalized with the name 

names = ['lai', 'sam', 'Jam']

for name in names:
    msg = "hello there, {}!".format(name.title())
    print(msg)

# Exercise 3: your own list ballot_box_with_check 


#think of your favorite mode of transportation such as motorcycle or car and make a list that stores a several examples. Use your list
#to print a series of your statements about these items, such as "I would like to own a honda motorcycle."

#favorite motorcycle 

motorcycles = ['Honda', 'Yamaha', 'Suzuki']

for motorcycle in motorcycles: 
    print(f"I would like to own a {motorcycle.lower()} motorcycle.")