#Import all functions used from Utilities.py
from Utilities import *

import json

#Database {Canteen name : [ (location), opentime, closetime, {food : [price, halal, vegetarian]} ] }
#Load Database
try:
    canteenList = read_data('Resource/database.json')
#Use the default database if not found
except FileNotFoundError:
    canteenList = {"North Spine Plaza" : [(215,220), "0900", "2100", {"Steamboat": [7, False, False],
                                                                 "Sandwich Guys": [5, False, True],
                                                                 "The Soup Spoon": [6, False, True],
                                                                 "Bakery Cuisine": [3, True, True],
                                                                 "Each A Cup (Bubbletea)": [3, True, True],
                                                                 "Grande Cibo (Italian Food)": [10, False, False],
                                                                 "KFC": [6, True, False],
                                                                 "Long John Silver": [6, True, False],
                                                                 "MacDonald's": [6, True, True],
                                                                 "Mr Bean": [4, True, True],
                                                                 "North Spine Food Court": [5, True, True],
                                                                 "PAIK Bibim's (Korean)": [8, False, False],
                                                                 "Peach Garden's Restaurant": [10, False, False],
                                                                 "Pizza Hut": [6, True, True],
                                                                 "Subway": [6, True, True],
                                                                 "Starbucks Coffee": [6, True, True],
                                                                 "PEN & INC": [8, False, False]}],
               "Koufu@SS"          : [(174,412), "0700", "2100", {"Yong Tau Foo": [4, True, False],
                                                                  "Fish Soup": [4, True, False],
                                                                  "Ban Mian": [3, True, True],
                                                                  "Indian Cuisine": [4, True, True]}],
               "Pioneer Food Court": [(451,468), "0700", "2100", {"Korean": [5, False, False],
                                                                  "Cai Fun": [5, False, True],
                                                                  "Ayam Penyet": [5, True, True]}],
               "Quad Cafe"         : [(158,284), "0700", "2100", {"Korean": [5, True, False],
                                                                  "Yong Tau Foo": [6, True, True],
                                                                  "Cai Fun": [5, True, True]}],
               "Food Court 1": [(382,377), "0700", "2100", {"chicken rice" :[4, False, False],
                                             "bak kut teh" : [6, False, False],
                                             "Nasi Padang" : [6, True, False],
                                             "Prata": [1, True, True],
                                             "fishball noodle" : [3, True, False],
                                             "pasta" : [6, True, False]}],
           "Food Court 2": [(408,308), "0700", "2100", {"ayam penyet" :[4.5, True, False],
                                             "xiao long bao" : [6, False, False]}],
           "North Hill Food Court" : [(600, 190),"0700","2100",{"Roasted Duck Noodle/Rice" : [4,True,False],
                                                        "Roasted Pork Noodle/Rice": [3.5,False,False],
                                                        "Char Siew Rice/Noodle": [3.5,False,False],
                                                        "Duck (Whole)": [44,False,False],
                                                        "Duck (Half)": [22,False,False],
                                                        "Char Siew" :[8,False,False],
                                                        "Roasted Pork":[8,False,False],
                                                        "Fishball Noodle" : [3,True,False],
                                                        "Minced Meat Noodle":[3,False,False],
                                                        "Laksa": [3.5,False,False],
                                                        "Korean Mini Wok Noodle" : [5,False,False],
                                                        "Mini Wok Noodle/Rice" : [5,False,False],
                                                        "Meatball Soup" : [3,False,False],
                                                        "Fishball Soup" : [3,True,False]}],
           "Foodgle Food Court" : [(555,91),"0700","2100",{"U mian" : [3.5,False,False],
                                                         "Yi mian": [3.5,False,False],
                                                         "Tom Yam Mian" : [4,False,False],
                                                         "Curry Rice" : [3.5,False,False],
                                                         "Chasiu Don" : [5.2,False,False],
                                                         "Chicken Katsu" : [5.2,True,False]}],
           "Ananda Kitchen" : [(602, 190),"1200","2230",{"Fish ball noodle":[3.5,True,False],
                                                 "Fish ball soup" : [3,True,False],
                                                 "Chicken Katsu" : [4.5,True,False],
                                                 "Curry Rice" : [4,False,False],
                                                 "Teh" : [1,True,True],
                                                 "Kopi" : [1,True,True],
                                                 "Plain Waffle" : [1.3,True,True],
                                                 "Cheese Waffle" : [1.8,True,True],
                                                 "Chocolate Waffle" : [1.8,True,True]}],
           "Food Court 16" : [(333,168),"0700","2100",{"Prata" : [1.5, True,True],
                                                "Nasi briyani" : [0.5,True,True],
                                                "Bandung" : [1.5,True,True],
                                                "Teh" : [1,True,True],
                                                "Kopi" : [1,True,True],
                                                "Fishball noodle" : [3.5,True,False],
                                                "Fishball soup" : [3,True,False]}],
            'Food Court 9' : [(508,183), '0700', '2100', {'mala':[10, False, False],
                                                          'chicken chop':[6,True,False],
                                                          'pasta':[3,True,False],
                                                          'cheese fries':[2,True,False],
                                                          'prata':[1.5,True,True],
                                                          'briyani':[5,True,False],
                                                          'chapati':[3,True,True],
                                                          'fried rice':[4,False,False],
                                                          'ban mian':[3,False,False],
                                                          'carrot cake':[3,False,False]}],
            'Food Court 11' : [(597,129), '0700', '2100', {'ramen':[5,False, False],
                                                           'curry rice':[5,False,False],
                                                           'mixed rice':[3,False,False],
                                                           'prata':[1,True,True],
                                                           'briyani':[3,True,False],
                                                           'fruit juice':[2.5,True,True],
                                                           'waffles':[2,True,True],
                                                           'bread':[1.5,True,True],
                                                           'drinks':[1.5,True,True]}],
            'Food Court 13' : [(358,95), '0700', '2100', {'ramen':[6,False, False],
                                                          'curry rice':[5,False,False],
                                                          'chicken rice':[3,False,False],
                                                          'roast pork rice':[3,False,False],
                                                          'duck rice':[4,False,False],
                                                          'chicken chop':[4,False,False],
                                                          'fish and chips':[5,False,False],
                                                          'pork chop':[4,False,False],
                                                          'pasta':[3,False,False],
                                                          'american breakfast':[3,True,False],
                                                          'cake':[3,True,False],
                                                          'teh':[1.5,True,True],
                                                          'kopi':[1.5,True,True]}],
            'Food Court 14' : [(418,90), '0700', '2100', {'chicken chop':[5.5,True,False],
                                                          'pasta':[3,True,False],
                                                          'ban mian':[3,False,False],
                                                          'fish soup':[4,False,False],
                                                          'dumpling soup':[3,False,False],
                                                          'chicken cutlet rice':[5,False,False],
                                                          'braised pork rice':[3.8,False,False],
                                                          'teh':[1.5,True,True],
                                                          'kopi':[1.5,True,True]}]
    }

#Initialization (Display map)
pygame.init()
pygame.display.set_caption('Mini Project: F&B Recommendation')
introScreenImage = pygame.image.load("Resource/NTU Map edited.jpg")
screen = pygame.display.set_mode((766,524))
screen.blit(introScreenImage,(0,0))
display_canteen(screen,canteenList)
pygame.display.flip()

#Main program
choice = 0
print("Welcome to the program!")
while choice != '8':
    #Print intro
    print_txt("Database/Intro.txt")
    print()
    #Prompt user what to do
    choice = input("Please do number: ")
    print()
    if  choice == '1': #Sort by distance
        print("Please click on the map")
        position = mouseclick(screen)
        print("These are the nearest canteens closest to you : ")
        distance_sorted = sort_distance(position,canteenList)
        #Display canteen coloured based on rank (Green is closest red is furthest)
        display_sorted(screen,canteenList,distance_sorted)
        print_list(canteenList,distance_sorted)
        print()
    elif choice == '2': #Search by food
        food = input("What food are you craving for? ")
        print("Checkout these canteens with the food you wanted: ")
        print_list(canteenList,search_by_food(food,canteenList))
        print()
    elif choice == '3': #Search by price
        try:
            budgetMin = float(input("Enter min price: "))
            budgetMax = float(input("Enter max price: "))
            #Reinput if the max is smaller than the min
            while(budgetMin > budgetMax):
                print("Invalid budget range! Please re-enter")
                budgetMin = float(input("Enter min price: "))
                budgetMax = float(input("Enter max price: "))
        except:
            print("Invalid budget!")
        else:
            print("These are the canteens that have prices between $%.2f and $%.2f: " % (budgetMin,budgetMax))
            print_list(canteenList,search_by_price(budgetMin,budgetMax,canteenList))
            print()
    elif choice == '4': #Search halal food
        print("These are canteens that have halal food: ")
        print_list(canteenList,search_by_halal(canteenList))
        print()
    elif choice == '5': #Search vegetarian food
        print("These are canteens that have vegetarian food: ")
        print_list(canteenList,search_by_veg(canteenList))
        print()
    elif choice == '6': #Sort by rank
        print("Please click on the map")
        position = mouseclick(screen)
        print("These are canteens recommended by us: ")
        display_canteen(screen,canteenList)
        rank_sorted = sort_by_rank(canteenList,position)
        print_list(canteenList,rank_sorted)
        print()
    elif choice == '7': #Update database
        update_choice = '0'
        while update_choice != '5':
            #Display canteens that are open
            display_canteen(screen,canteenList)
            #Print from Update.txt
            print_txt("Resource/Update.txt")
            print()
            update_choice = input("I want to update: ")
            if update_choice == '1':
                #What canteen to update
                canteen_target = get_target_canteen(canteenList)
                #Get the new opening time
                new_open_time = get_valid_time()
                #Update database
                canteenList[canteen_target][1] = new_open_time
                print("Updated! Thank you for your information!")
                print()
                write_data(canteenList,"Resource/database.json")
                #Refresh database used on runtime
                canteenList = read_data('Resource/database.json')
            elif update_choice == '2':
                #What canteen to update
                canteen_target = get_target_canteen(canteenList)
                #Get the new closing time
                new_close_time = get_valid_time()
                #Update database
                canteenList[canteen_target][2] = new_close_time
                print("Updated! Thank you for your information!")
                print()
                write_data(canteenList,"Resource/database.json")
                #Refresh database used on runtime
                canteenList = read_data('Resource/database.json')
            elif update_choice == '3':
                #What canteen to update
                canteen_target = get_target_canteen(canteenList)
                #Color the chosen canteen blue
                draw_circle(screen,10,canteenList[canteen_target][0],(0,0,255),2,(0,0,0))
                #Get the new location
                print("Click on the map to enter the new location")
                new_position = mouseclick(screen)
                #Update database
                canteenList[canteen_target][0] = new_position
                print("Updated! Thank you for your information!")
                print()
                write_data(canteenList,"Resource/database.json")
                #Refresh database used on runtime
                canteenList = read_data('Resource/database.json')
            elif update_choice == '4':
                #What canteen to update
                canteen_target = get_target_canteen(canteenList)
                #Get the new food's name
                new_food_name = input("Please enter the new dish's name: ")
                #Get the new food's price
                print("Please enter the new dish's price")
                print("Dollar: ",end='')
                new_food_dollar = get_valid_num()
                print("Cent: ",end='')
                new_food_cent = get_valid_num()
                new_food_price = new_food_dollar + new_food_cent*0.01
                #Is the food halal?
                print("Is it halal? (Y/N) ",end='')
                new_food_halal = y_n_to_bool(get_yes_no())
                #Is the food vegetarian?
                new_food_vegetarian = y_n_to_bool(get_yes_no())
                #Update database
                canteenList[canteen_target][3].update({new_food_name:[new_food_price,new_food_halal,new_food_vegetarian]})
                print("Updated! Thank you for your information!")
                print()
                write_data(canteenList,"Resource/database.json")
                #Refresh database used on runtime
                canteenList = read_data('Resource/database.json')
            elif update_choice == '5':
                print()
            else:
                update_choice = input('Invalid input! Please re-enter: ')

    elif choice == '8':
        print("Goodbye! See you next time!")
    else:
        choice = input("Invalid input! Please re-enter: ")
