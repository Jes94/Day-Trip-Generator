import random

destination_list = ['New York', 'Los Angeles', 'Vegas', 'Orlando', 'Tampa', 'Charlotte', 'San Antonio', 'San Jose', 'Chicago', 'Dallas', 'Philadelphia']
restaurant_list = ['McDonalds', 'Burger King', 'Wendys', 'Taco Bell', 'Qdoba', 'Chipotle', 'Olive Garden', 'TGI Fridays', 'Applebees', 'Logans Roadhouse']
transportation_list = ['Rental car', 'Uber', 'Lyft', 'Taxi', 'Limo service', 'Bus']
entertainment_list = ['going to the movies', 'visiting a local theme park', 'going golfing', 'visiting an arcade', 'going on a local tour', 'going to a concert', 'visting a museum', 'visiting a zoo', 'going clubbing']

def user_pick_destination():
    satisfied = 1  
    while satisfied != 0:
        random_destination = random.choice(destination_list)
        destination_satisfaction = input(f'We have selected {random_destination} for your destination! Does this sound good? Enter y/n:  ')
        if destination_satisfaction.lower() == 'y':
            print("Awesome! Glad that it's decided. Let's move on! ")
            satisfied -= 1
            return random_destination
        elif destination_satisfaction.lower() == 'n':
            print("Sorry you didn't like that choice, let's give it another go!")
            satisfied == 1

def user_pick_transportation():
    satisfied = 1  
    while satisfied != 0:
        random_transportation = random.choice(transportation_list)
        transportation_satisfaction = input(f'We have selected {random_transportation} for your transportation option! Does this sound good? Enter y/n: ')
        if transportation_satisfaction.lower() == 'y':
            print("Awesome, that's a great choice! Let's keep going!")
            satisfied -= 1
            return random_transportation
        elif transportation_satisfaction.lower() == 'n':
            print("We're terribly sorry that you didn't like that choice, let's try that again.")
            satisfied == 1

def user_pick_entertainment():
    satisfied = 1  
    while satisfied != 0:
        random_entertainment = random.choice(entertainment_list)
        entertainment_satisfaction = input(f'How about {random_entertainment} as your entertainment option! Does this sound good? Enter y/n: ')
        if entertainment_satisfaction.lower() == 'y':
            print("Awesome, sounds like a blast! Let's move on.")
            satisfied -= 1
            return random_entertainment
        elif entertainment_satisfaction.lower() == 'n':
            print("Sorry you didn't like that choice, let's try that again!")
            satisfied == 1

def user_pick_restaurant():
    satisfied = 1  
    while satisfied != 0:
        random_restaurant = random.choice(restaurant_list)
        restaurant_satisfaction = input(f'We have selected {random_restaurant} for your restaurant! Does that sound appatizing? Enter y/n: ')
        if restaurant_satisfaction.lower() == 'y':
            print("Glad we have that settled, let's keep going!")
            satisfied -= 1
            return random_restaurant
        elif restaurant_satisfaction.lower() == 'n':
            print("Sorry that you dind't like that idea, let's try that again!")
            satisfied == 1

chosen_destination = user_pick_destination()
chosen_transportation = user_pick_transportation()
chosen_entertainment = user_pick_entertainment()
chosen_restaurant = user_pick_restaurant()
