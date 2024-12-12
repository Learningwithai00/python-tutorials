##Write a program to save a list of your favorite movies to a file.

movies = ["Inception", "The Matrix", "Interstellar"]
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(movie + "\n")
