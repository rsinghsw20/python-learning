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
for each_item in fav_movies:
    print(each_item)
