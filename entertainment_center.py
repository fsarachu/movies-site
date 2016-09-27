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

lord_of_rings = media.Movie("The Lord of the Rings: The Two Towers ",
                            "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided "
                            "fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard. ",
                            "http://www.gstatic.com/tv/thumb/movieposters/30793/p30793_p_v8_am.jpg",
                            "https://www.youtube.com/watch?v=2dlRvAjU_RI")

print the_godfather.title + " - " + the_godfather.storyline
print pulp_fiction.title + " - " + pulp_fiction.storyline
print lord_of_rings.title + " - " + lord_of_rings.storyline
