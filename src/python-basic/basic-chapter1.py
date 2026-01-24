movies = ["The Holy Grail",
          "The Life of Brian",
          "The Meaning of Life"]
print(movies[-1])
cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(cast[1])
cast.append("Gilliam")
cast.pop()
cast.extend(["Gilliam","Chapman"])
print(cast)
cast.remove("Idle")
print(cast)
cast.insert(2, "Idle")
print(cast)
movies = ["The Holy Grail",
          "The Life of Brian",
          "The Meaning of Life"]
movies.insert(1, 1975)
print(movies)
movies.insert(3, 1979)
print(movies)
movies.insert(5, 1983)
print(movies)
fav_movies = ["The Holy Grail","The Life of Brian","The Meaning of Life"]
for each_flick in fav_movies:
    print(each_flick)
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies[4][0])
for each_item in movies:
    print(each_item)
if movies[3]>90:
    print("Long movie")
else:
    print("Short movie")
    for each_item in movies:
        print(each_item)
    names = ['Michael', 'Terry']
    isinstance(names, list)
    print(names)

    names = ['Michael', 'Terry']
    isinstance(names, list)
    print(movies[-1])
    if movies[3]<90:
        print("Long movie")
    else:
        print("Short movie")
print(len(movies))
print(type(movies))
movies.append("TBBT")
print(movies)
movies.pop()
print(movies)
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)
def print_movies(movies):
    for each_item in movies:
        if isinstance(each_item, list):
            print_movies(each_item)
        else:
            print(each_item)












