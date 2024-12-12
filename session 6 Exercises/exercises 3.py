##Read the file and print each movie on a new line.

with open("movies.txt", "r") as file:
    for line in file:
        print(line.strip())
