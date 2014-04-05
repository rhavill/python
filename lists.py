#!/usr/bin/python

# just like PHP in_array
print 3 in [1,2,3,4]
names = ["Adam","Alex","Mariah","Martine","Columbus"]
names.pop(2)
del(names[1])
for name in names:
    print name
for i in range(0, len(names)):
 	print names[i]
print range(10)
print range(6,10);
print range(2,10,2)
print '--'.join(names)
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    
}
print inventory.items()
print inventory.keys()
print inventory.values()
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print inventory

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total +  prices[item]
            stock[item] = stock[item] - 1
    return total
print compute_bill(shopping_list)    

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = float(0)
    for number in numbers:
        total = total + number
    return total / len(numbers)
def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return homework*0.10 + quizzes*0.30 + tests*0.6
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
        
print get_letter_grade(get_average(lloyd))  

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
    
students = [lloyd, alice, tyler]    
class_average = get_class_average(students)      
print class_average
print get_letter_grade(class_average)

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

#reverse
my_list = range(1, 11)

# Add your code below!
print my_list[::-1]

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)