import random, time, math, statistics
import matplotlib.pyplot as plt

char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#0 = nametag, 1 = generation, 2 = speed, 3 = sight, 4 = stamina, 5 = dominance, 6 = fertility
prey = []

#0 = nametag, 1 = generation, 2 = speed, 3 = sight, 4 = stamina, 5 = dominance, 6 = fertility
predators = []

#0 = nametag, 1 = generation, 2 = fertility, 3 = availability
food = []

prey_count = []
predator_count = []
food_count = []

print("+- GENERATION SETTINGS -+")
sim_mode = input("SIM MODE <N/D/S>: ")
world_seed = int(input("WORLD SEED: "))
total_terms = int(input("TOTAL TERMS: "))
term_time = int(input("TERM TIME: "))

print("\n","+- POPULATION -+")
prey_num = int(input("PREY COUNT: "))
predator_num = int(input("PREDATOR COUNT: "))
food_num = int(input("FOOD COUNT: "))

print("\n","+- WORLD SETTINGS -+")
max_food = int(input("MAX FOOD: "))
max_stamina = int(input("MAX STAMINA: "))
prey_lifespan = int(input("PREY LIFESPAN: "))
predator_lifespan = int(input("PREDATOR LIFESPAN: "))
food_lifespan = int(input("FOOD LIFESPAN: "))
change_limit = float(input("MUTATION LIMIT: "))

if world_seed != 0:
    random.seed(world_seed)
else:
    pass

for i in range(prey_num):
    name = ""
    for char in range(12):
        name += random.choice(char_list)
    prey.append([name, 1, random.random(),random.random(), random.randint(1,max_stamina), random.random(), random.random()])

for j in range(predator_num):
    name = ""
    for char in range(12):
        name += random.choice(char_list)
    predators.append([name, 1, random.random(),random.random(), random.randint(1,max_stamina), random.random(), random.random()])

for k in range(food_num):
    name = ""
    for char in range(12):
        name += random.choice(char_list)
    food.append([name, 1, random.random(),random.random()])

#print(prey, predators)

def eating_phase_prey():
    global prey, predators, food
    fed = []
    #prey.sort(key = lambda x: x[5], reverse=True)
    random.shuffle(prey)
    for i in prey:
        random.shuffle(food)
        if len(food) < i[4]:
            for j in range(len(food)):
                if food[j][3] - 0.2 > i[3]:
                    pass
                else:
                    food.pop(j)
                    fed.append(i)
                    break

        else:
            for j in range(i[4]):
                if food[j][3] - 0.2 < i[3]:
                    pass
                else:
                    food.pop(j)
                    fed.append(i)
                    break

    prey = [p for p in prey if p in fed]

def eating_phase_predators():
    global prey, predators, food
    fed = []
    #predators.sort(key = lambda x: x[5], reverse=True)
    random.shuffle(predators)
    for i in predators:
        random.shuffle(prey)
        if len(prey) < i[4]:
            for j in range(len(prey)):
                if prey[j][2] > i[2] + 0.3:
                    pass
                else:
                    prey.pop(j)
                    fed.append(i)
                    break

        else:
            for j in range(i[4]):
                if prey[j][2] < i[2] + 0.3:
                    pass
                else:
                    prey.pop(j)
                    fed.append(i)
                    break

    predators = [p for p in predators if p in fed]

def reproduction_food():
    global prey, predators, food
    for i in range(len(food) - 1):
        if food[i][2] > random.random() and random.random() > 0.4:
            if food[i][2] > 0.6:
                for loop in range(2):
                    name = ""
                    for char in range(12):
                        name += random.choice(char_list)
                    food.append([name, food[i][1] + 1, food[i][2] + random.uniform(-change_limit,change_limit),food[i][3] + random.uniform(-change_limit,change_limit)])
            else:
                name = ""
                for char in range(12):
                    name += random.choice(char_list)
                food.append([name, food[i][1] + 1, food[i][2] + random.uniform(-change_limit,change_limit),food[i][3] + random.uniform(-change_limit,change_limit)])
        else:
            pass

def reproduction_prey():
    global prey, predators, food
    for i in range(len(prey)):
        'prey[i][6] > random.random() and '
        if random.random() > (1 / (abs(len(prey) - len(food)) + 1)):
            if prey[i][6] > 0.5:
                for loop in range(2):
                    name = ""
                    for char in range(12):
                        name += random.choice(char_list)
                    prey.append([name, prey[i][1] + 1, prey[i][2] + random.uniform(-change_limit,change_limit) ,prey[i][3] + random.uniform(-change_limit,change_limit) ,prey[i][4] + random.randint(-2,2) ,prey[i][5] + random.uniform(-change_limit,change_limit) ,prey[i][6] + random.uniform(-change_limit,change_limit)])
            else:
                name = ""
                for char in range(12):
                    name += random.choice(char_list)
                prey.append([name, prey[i][1] + 1, prey[i][2] + random.uniform(-change_limit,change_limit) ,prey[i][3] + random.uniform(-change_limit,change_limit) ,prey[i][4] + random.randint(-2,2) ,prey[i][5] + random.uniform(-change_limit,change_limit) ,prey[i][6] + random.uniform(-change_limit,change_limit)])

        else:
            pass

def reproduction_predators():
    global prey, predators, food
    for i in range(len(predators)):
        'predators[i][6] > random.random() and '
        if random.random() > (1 / (abs(len(predators) - len(prey)) + 1)) + 0.2:
            if predators[i][6] > 0.5:
                for loop in range(2):
                    name = ""
                    for char in range(12):
                        name += random.choice(char_list)
                    predators.append([name, predators[i][1] + 1, predators[i][2] + random.uniform(-change_limit,change_limit) ,predators[i][3] + random.uniform(-change_limit,change_limit) ,predators[i][4] + random.randint(-2,2) ,predators[i][5] + random.uniform(-change_limit,change_limit) ,predators[i][6] + random.uniform(-change_limit,change_limit)])
            else:
                name = ""
                for char in range(12):
                    name += random.choice(char_list)
                predators.append([name, predators[i][1] + 1, predators[i][2] + random.uniform(-change_limit,change_limit) ,predators[i][3] + random.uniform(-change_limit,change_limit) ,predators[i][4] + random.randint(-2,2) ,predators[i][5] + random.uniform(-change_limit,change_limit) ,predators[i][6] + random.uniform(-change_limit,change_limit)])
        else:
            pass

def decay_food(current_term):
    global food, lifespan
    food = [f for f in food if f[1] > current_term - food_lifespan]

def decay_prey(current_term):
    global prey, lifespan
    prey = [p for p in prey if p[1] > current_term - prey_lifespan]

def decay_predators(current_term):
    global predators, lifespan
    predators = [pr for pr in predators if pr[1] > current_term - predator_lifespan]
    

def regulation():
    global food, prey, predators
    for i in food:
        if i[2] < 0:
            i[2] = 0
        elif i[2] > 1:
            i[2] = 0.999

        if i[3] < 0:
            i[3] = 0
        elif i[3] > 1:
            i[3] = 0.999

    for i in prey:
        if i[2] < 0:
            i[2] = 0
        elif i[2] > 1:
            i[2] = 0.999

        if i[3] < 0:
            i[3] = 0
        elif i[3] > 1:
            i[3] = 0.999

        if i[4] < 0:
            i[4] = 0
        elif i[4] > max_stamina:
            i[4] = max_stamina

        if i[5] < 0:
            i[5] = 0
        elif i[5] > 1:
            i[5] = 0.999

        if i[6] < 0:
            i[6] = 0
        elif i[6] > 1:
            i[6] = 0.999

    for i in predators:
        if i[2] < 0:
            i[2] = 0
        elif i[2] > 1:
            i[2] = 0.999

        if i[3] < 0:
            i[3] = 0
        elif i[3] > 1:
            i[3] = 0.999

        if i[4] < 0:
            i[4] = 0
        elif i[4] > max_stamina:
            i[4] = max_stamina

        if i[5] < 0:
            i[5] = 0
        elif i[5] > 1:
            i[5] = 0.999

        if i[6] < 0:
            i[6] = 0
        elif i[6] > 1:
            i[6] = 0.999

for i in range(total_terms):
    _term = i+1
    reproduction_food()

    while len(food) > max_food:
        random.shuffle(food)
        food.pop(0)
            
    
    eating_phase_prey()

    reproduction_prey()
    
    eating_phase_predators()

    reproduction_predators()

    decay_food(_term)
    decay_prey(_term)
    decay_predators(_term)
    
    print(f"TERM {_term}:")
    print(f"PREY: {len(prey)}")
    print(f"PREDATORS: {len(predators)}")
    print(f"FOOD: {len(food)}")
    print("")

    if sim_mode.lower() == "d":
        print("PREY:",prey,"\n")
        print("PREDATORS:",predators,"\n")
        print("FOOD:",food,"\n")

        print("")

        if len(prey) != 0:
            print(f"MEAN PREY SPEED: {statistics.mean([p[2] for p in prey])}")
            print(f"MEAN PREY SIGHT: {statistics.mean([p[3] for p in prey])}")
            print(f"MEAN PREY STAMINA: {statistics.mean([p[4] for p in prey])}")
            print(f"MEAN PREY DOMINANCE: {statistics.mean([p[5] for p in prey])}")
            print(f"MEAN PREY FERTILITY: {statistics.mean([p[6] for p in prey])}")

        if len(predators) != 0:
            print(f"MEAN PREDATOR SPEED: {statistics.mean([p[2] for p in predators])}")
            print(f"MEAN PREDATOR SIGHT: {statistics.mean([p[3] for p in predators])}")
            print(f"MEAN PREDATOR STAMINA: {statistics.mean([p[4] for p in predators])}")
            print(f"MEAN PREDATOR DOMINANCE: {statistics.mean([p[5] for p in predators])}")
            print(f"MEAN PREDATOR FERTILITY: {statistics.mean([p[6] for p in predators])}")

        if len(food) != 0:
            print(f"MEAN FOOD AVAILABILITY: {statistics.mean([p[3] for p in predators])}")
            print(f"MEAN FOOD FERTILITY: {statistics.mean([p[2] for p in predators])}")

        print("")

    if sim_mode.lower() == "s":
        if len(prey) != 0:
            print(f"MEAN PREY SPEED: {statistics.mean([p[2] for p in prey])}")
            print(f"MEAN PREY SIGHT: {statistics.mean([p[3] for p in prey])}")
            print(f"MEAN PREY STAMINA: {statistics.mean([p[4] for p in prey])}")
            print(f"MEAN PREY DOMINANCE: {statistics.mean([p[5] for p in prey])}")
            print(f"MEAN PREY FERTILITY: {statistics.mean([p[6] for p in prey])}")

        if len(predators) != 0:
            print(f"MEAN PREDATOR SPEED: {statistics.mean([p[2] for p in predators])}")
            print(f"MEAN PREDATOR SIGHT: {statistics.mean([p[3] for p in predators])}")
            print(f"MEAN PREDATOR STAMINA: {statistics.mean([p[4] for p in predators])}")
            print(f"MEAN PREDATOR DOMINANCE: {statistics.mean([p[5] for p in predators])}")
            print(f"MEAN PREDATOR FERTILITY: {statistics.mean([p[6] for p in predators])}")

        if len(food) != 0:
            print(f"MEAN FOOD AVAILABILITY: {statistics.mean([p[3] for p in predators])}")
            print(f"MEAN FOOD FERTILITY: {statistics.mean([p[2] for p in predators])}")

        print("")

    prey_count.append(len(prey))
    predator_count.append(len(predators))
    food_count.append(len(food))

    time.sleep(term_time)

plt.plot(prey_count)
plt.plot(predator_count)
plt.plot(food_count)

plt.show()
