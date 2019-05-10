# Exercise 9
grocery_list = ['carrots', 'toilet paper', 'apples', 'salmon']

def grocery(items):
    for i in items:
        print(f'* {i}')
    print(len(items))
    if i == 'bananas':
        print("You don't need to pick up bananas today.")
    else: 
        print('You need to pick up bananas.')
    print(items[1])

grocery_list.append('rice')
grocery_list.remove('salmon')
grocery_list.sort()
grocery(grocery_list)


# Exercise 10

students = {
    'cohort1': 34,
    'cohort2': 42,
    'cohort3': 22
}
def cohort(numbers):
    for stu_name, stu_no in numbers.items():
        print(f'{stu_name}: {stu_no} students')

students['cohort4'] = 43
print(students.keys())
cohort(students)

new_stu_increament = {}
for key, value in students.items():
    new_stu_increament[key] = float(value + value*0.05) 
cohort(new_stu_increament)

students.pop('cohort2')
cohort(students)

total = 0
for no_of_stu in new_stu_increament.values():
    total += no_of_stu 

print(total)




