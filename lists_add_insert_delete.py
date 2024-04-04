fav_movies = ["Sandlot", "The Lego Movie", "Dune"]

print(len(fav_movies))

fav_movies.append("Iron Man")

print(len(fav_movies))

print(fav_movies)

fav_movies.insert(1, "Batman")

print(fav_movies)

del(fav_movies[2])

print(fav_movies)

# Remove enough items from fav_movies until there's only one movie left

del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[1])

print(fav_movies)