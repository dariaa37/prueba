# This is a little proof for REPOSITORES in bedu

# Mini registro de datos

fMovies = {
    "Nombre" : ["Perfect Blue", "Princess Kaguya", "Fantastic Mr. Fox", "Coraline", "Pride and Predujice", "Pearl"],
    "Duración": [1.22, 2.17, 1.27, 1.40, 2.07, 1.42],
    "Genero": ["Triller/Mystery", "Fantasy/Animation", "Comedy/Adventure", "Fantasy", "Romance/Drama", "Horror/Slasher"]
}

answer = input("Ingresa el nombre de una peliula:\t")

index = fMovies["Nombre"].index(answer)

for movies in fMovies:
    print(f"{movies}:\t  {fMovies[movies][index]}")

