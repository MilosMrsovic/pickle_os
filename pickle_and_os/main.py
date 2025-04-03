import pickle
from movie import Movie
import os

lista_filmova = []

if os.path.exists("filmovi.txt"):
    with open("filmovi.txt", "rb") as file:
        lista_filmova = pickle.load(file)

running = True

while running:
    command = input("Add new movie(1) \nShow all movies(2) \nExit(3) \n")
    
    if command == "1":
        title = input("Movie title: ")
        release_year = input("Movie release year: ") 
        genre = input("Movie genre: ")
        imdb_url = input("Movie IMBD URL: ")
        
        film = Movie(title, release_year, genre, imdb_url)
        lista_filmova.append(film)
        
        with open("filmovi.txt", "wb") as file:
            pickle.dump(lista_filmova, file)
    elif command == "2":
        if (len(lista_filmova) > 0):
            for film in lista_filmova:
                print(f"{film}\n")
        else:
            print("No movies entered yet")
    elif command == "3":
        print("Have a nice day!")
        running = False
    else:
        print("\nYou inputed wrong command \n")
        