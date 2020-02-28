#Import module pygame
import pygame

#Display map
def display_map():
    introScreenImage = pygame.image.load("Resource/NTU Map edited.jpg")
    screen = pygame.display.set_mode((766,524))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()

#Get distance between 2 points
def distance_a_b(location_of_a, location_of_b):
    return ((location_of_a[0]-location_of_b[0])**2 + (location_of_a[1]-location_of_b[1])**2)**0.5

#Get canteen with available food
def search_by_food(foodname, foodlist_canteens):
    availableList=[]
    for canteenName in foodlist_canteens.keys():
        for foods in foodlist_canteens[canteenName][3].keys():
            if (foods.lower() == foodname.lower()):
                availableList.append(canteenName)
                break
    return availableList

#Get the average price of all foods in a canteen
def average_price(foodlist_canteens,canteenName):
    totalPrice = 0
    for datas in foodlist_canteens[canteenName][3].values():
        price = datas[0]
        totalPrice += price
    return totalPrice / len(foodlist_canteens[canteenName][3])

#Scores canteen from 1 to 14 according to average price of food
def canteen_pricescore(foodlist_canteens):
    Foodscore_List = {}
    i = 1
    for key in foodlist_canteens.keys():
        Foodscore_List.update({key: average_price(foodlist_canteens,key)})
    for name in sorted(Foodscore_List.keys(), key = Foodscore_List.get):
        Foodscore_List[name] = i
        i+=1
    return Foodscore_List

#Scores canteen from 1 to 14 according to the distance
def canteen_distscore(foodlist_canteens,user_location):
    Distscore ={}
    i = 1
    for key in foodlist_canteens.keys():
        Distscore.update({key: distance_a_b(user_location,foodlist_canteens[key][0])})
    for name in sorted(Distscore.keys(), key = Distscore.get):
        Distscore[name] = i
        i+=1
    return Distscore

#Sort canteen based on calculated rank (20% Price, 80% Distance)
def sort_by_rank(foodlist_canteens,user_location):
    CanteenScore = {}
    Distscore = canteen_distscore(foodlist_canteens,user_location)
    Foodscore = canteen_pricescore(foodlist_canteens)
    for canteenName in foodlist_canteens.keys():
        CanteenScore.update({canteenName : (0.2 * Foodscore[canteenName] + 0.8 * Distscore[canteenName])})
    return sorted(CanteenScore.keys(), key = CanteenScore.get)

#Get canteens that have food suitable to the budget input
def search_by_price(priceMin, priceMax, foodlist_canteens):
    availableList = []
    for canteenName in foodlist_canteens.keys():
        for datas in foodlist_canteens[canteenName][3].values():
            price = float(datas[0])
            if (priceMin <= price <= priceMax):
                availableList.append(canteenName)
                break
    return availableList

#Gets coordinate when the map is clicked
def mouseclick(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickImage = pygame.image.load("Resource/Arrow.png")
                clickImage = pygame.transform.scale(clickImage,(15,15))
                load_arrow(screen, clickImage,pygame.mouse.get_pos())
                return pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()

#Sorts canteen by location to the user
def sort_distance(user_location, canteens_location):
    distList={}
    finalList =[]
    for name in canteens_location.keys():
        distList.update({distance_a_b(canteens_location[name][0], user_location):name})
    distSort = sorted(distList)
    for i in range(len(distSort)):
        finalList.append(distList[distSort[i]])
    return finalList

#Determine if the canteen is open
def is_open(opentime,closetime):
    import time
    current_time_list = time.localtime(time.time())
    current_time= '' + str(current_time_list[3]) + str(current_time_list[5])
    if opentime < current_time < closetime:
        return True
    else:
        return False

#Displays arrow on click
def load_arrow(screen,image,pos):
    display_map()
    coordinate = list(pos)
    coordinate[0] -= 8
    coordinate[1] -= 15
    screen.blit(image,coordinate)
    pygame.display.update()

#Display canteen availability
#Green = canteen is open
#Gray = canteen is closed
def display_canteen(screen, foodlist_canteens):
    for name in foodlist_canteens.keys():
        cant_pos = (foodlist_canteens[name][0])
        cant_open_time = foodlist_canteens[name][1]
        cant_close_time = foodlist_canteens[name][2]
        if is_open(cant_open_time,cant_close_time):
            cant_color = (0,255,0)
        else:
            cant_color = (60,60,60)
        draw_circle(screen, 10, cant_pos, cant_color,2,(0,0,0))
    pygame.display.update()

#Draw a circle with outline
def draw_circle(screen,radius,pos,color,outline_width,outline_color):
    pygame.draw.circle(screen, outline_color, pos, radius+outline_width)
    pygame.draw.circle(screen, color, pos, radius)

#Read Database
def read_data(filename):
    import json
    with open(filename,'r') as f:
        return json.load(f)

#Write Database
def write_data(database, filename):
    import json
    with open(filename,'w') as f:
        json.dump(database, f)

#Print canteens with numbers
def print_list(foodlist_canteen, the_list):
    if len(the_list)==0:
       print("Sorry! None are available")
    else:
        for i in range(len(the_list)):
            print((i+1),end ='')
            openTime = foodlist_canteen[the_list[i]][1]
            closeTime = foodlist_canteen[the_list[i]][2]
            if not is_open(openTime,closeTime):
                print(".", the_list[i],"(Closed)")
            else:
                print(".", the_list[i])

#Search canteens with halal food
def search_by_halal(foodlist_canteens):
    availableList = []
    for canteenName in foodlist_canteens.keys():
        for datas in foodlist_canteens[canteenName][3].values():
            halal = datas[1]
            if halal:
                availableList.append(canteenName)
                break
    return availableList

#Search canteens with vegetarian food
def search_by_veg(foodlist_canteens):
    availableList = []
    for canteenName in foodlist_canteens.keys():
        for datas in foodlist_canteens[canteenName][3].values():
            vegetarian = datas[2]
            if vegetarian:
                availableList.append(canteenName)
                break
    return availableList

#Print .txt file content
def print_txt(filename):
    with open(filename,'r') as f:
        for line in f:
            print(line, end='')

#Return the name of canteen in the database
def get_target_canteen(foodlist_canteens):
    canteen_target =''
    while not canteen_target in foodlist_canteens:
        canteen_target = input("Please enter the canteen that you want to update: ")
    return canteen_target

#Check and return the time in string (24 hour format)
def get_valid_time():
    new_time ='9999'
    while not ('00'<=new_time[0:2]<='24' and '00'<=new_time[2:] <= '59'):
        new_time= input("Please enter the new time: ")
    return new_time

#Get positive integer
def get_valid_num():
    num=''
    while not num.isdigit():
        num = input()
    return int(num)

#Get the character y or n
def get_yes_no():
    answer = ''
    while not (answer.lower() =='y' or 'n'):
        answer = input()
    return answer.lower()

#Convert y or n to True or False
def y_n_to_bool(y_or_n):
    if(y_or_n == 'y'):
        return True
    else:
        return False

#Color the canteens based on the sorted list (green for the "best" red for the "worst")
def display_sorted(screen, foodlist_canteens, sorted_list):
    r = 0
    g = 255
    i = 0
    for canteenName in sorted_list:
        if is_open(foodlist_canteens[canteenName][1], foodlist_canteens[canteenName][2]):
            r += 17*i
            g -= 17*i
            draw_circle(screen, 10,foodlist_canteens[canteenName][0],(r,g,0),2,(0,0,0))
            i+=1
        else:
            draw_circle(screen, 10, foodlist_canteens[canteenName][0], (60,60,60),2,(0,0,0))
    pygame.display.update()
