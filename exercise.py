# Exercise 0
fav_colors = ['blue', 'red', 'green', 'yellow', 'burgundy']
age = [23, 26, 30, 28, 25]
coin_flip = ['heads', 'tails', 'tails', 'heads', 'heads']
fav_artists = ['Ellie Goulding', 'Katy Perry', 'Beyonce']

words = {'antithesis': 'exact opposite', 'cogent': 'powerfully persuasive','extol': 'praise,glorify, or honor'}
fav_movies = {'Lincoln': 2012, 'Arrival': 2016, 'The Imitation Game': 2016}
city_pop = {'New York': 8.623,'London': 8.136, 'Tokyo': 9.273}
name_age = {'Andrew': 27, 'Mike': 25, 'Nancy': 24, 'John': 30}


# Exercise 1
print(coin_flip)
print(fav_colors[0])
print(sorted(age))
age.append(0)
print(age)
print(fav_movies['Lincoln'])


# Exercise 2
print(fav_colors[-1])
city_pop['Barcelona'] = 1.615
# print(city_pop)
coin_flip.reverse()
# print(coin_flip)
print(city_pop['Tokyo'])
for artists in fav_artists:
    print(f'I think {artists} is great')


# Exercise 3
print(fav_artists[1:3])
for movies, year in fav_movies.items():
    print(f'{movies} came out in {year}.')
age.sort(reverse=True)
print(age)
fav_movies['Beauty and the Beast'] = "'original': 1991 and 'remake': 2017"
print(fav_movies)


# Exercise 4
for ages in age:
    if ages < 28: 
        print(ages)
print(f"Oldest person's age is {max(age)}.")
print(coin_flip.count('heads'))
fav_artists.remove('Beyonce')
# print(fav_artists)
city_pop['Tokyo'] = 10
# print(city_pop)


# Exercise 5
print(sum(city_pop.values()))
for name, ages in name_age.items():
    if ages <= 26:
        print(f'{name} is young.')
    else:
        print(f'{name} is old.')
print(fav_colors[-2:])
for index, ages in enumerate(age):
    age[index] = ages + 1
    print(age[index])
fav_colors.append('white')
fav_colors.append('orange')
# print(fav_colors)

# Exercise 6
new_movies = {
    1991: 'The Matrix, Star Wars: Episode 1, The Mummy',
    2009: 'Avatar, Star Trek, District 9',
    2019: 'How to Train Your Dragon 3, Toy Story 4, Star Wars: Episode 9'
}
# print(new_movies) 
phone_buttons = [[1,2,3], [4,5,6], [6,7,8], ['*',0,'#']]
# print(phone_buttons)
countries = [
    {'name': 'Fiji', 'continent': 'Asia', 'island': 'Yes'},
    {'name': 'Argentina', 'continent': 'South America', 'island': 'No'},
    {'name': 'Spain', 'continent': 'Europe', 'island': 'No'}
]


# Exercise 7

for i in range(20):
    print('I will not skateboard in the halls')
# message = ['I will not skateboard in the halls'] * 20
# print(message)
# or
message = []
for i in range(20):
    message.append('I will not skateboard in the halls')
# print(message)
numbers = list(range(1, 51))
# print(numbers)
total = 0
for i in numbers:
   total += i
# print(total)
again = []
for i in numbers:
        again.append(i)
        again.append(i)
        again.append(i)
print(again)
not_a_island = []    
for islands in countries:
    if islands['island'] == 'No':
        not_a_island.append(islands)
print(not_a_island)
print(countries)

def monthly_exp(expenses):
    return sum(expenses)
expense1 = [250, 7.95, 30.95, 16.50]
expense2 = [50.44, 70.92, 305.05, 160.08]
print(monthly_exp(expense1))
print(monthly_exp(expense2))

















