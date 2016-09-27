import media

the_godfather = media.Movie("The Godfather",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine "
                            "empire to his reluctant son. ",
                            "http://dramatica.com/resources/onesheets/the-godfather-one-sheet.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

pulp_fiction = media.Movie("Pulp Fiction",
                           "An insomniac office worker, looking for a way to change his life, crosses paths with a "
                           "devil-may-care soap maker, forming an underground fight club that evolves into something "
                           "much, much more. ",
                           "http://cdn.miramax.com/media/assets/Pulp-Fiction1.png",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

print the_godfather.title + ": " + the_godfather.storyline
print pulp_fiction.title + ": " + pulp_fiction.storyline
