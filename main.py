import fresh_tomatoes
import media

movies = [
    media.Movie("The Godfather",
                "The aging patriarch of an organized crime dynasty transfers control of his clandestine "
                "empire to his reluctant son.",
                "http://dramatica.com/resources/onesheets/the-godfather-one-sheet.jpg",
                "https://www.youtube.com/watch?v=sY1S34973zA"),
    media.Movie("Pulp Fiction",
                "An insomniac office worker, looking for a way to change his life, crosses paths with a "
                "devil-may-care soap maker, forming an underground fight club that evolves into something "
                "much, much more.",
                "http://cdn.miramax.com/media/assets/Pulp-Fiction1.png",
                "https://www.youtube.com/watch?v=s7EdQ4FqbhY"),
    media.Movie("The Lord of the Rings: The Two Towers ",
                "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided "
                "fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",
                "http://www.gstatic.com/tv/thumb/movieposters/30793/p30793_p_v8_am.jpg",
                "https://www.youtube.com/watch?v=2dlRvAjU_RI"),

    media.Movie("Blue Streak",
                "A former convict poses as a cop to retrieve a diamond he stole years ago.",
                "https://upload.wikimedia.org/wikipedia/en/a/ab/Blue_Streak_film_poster.jpg",
                "https://www.youtube.com/watch?v=kj5NHXDvKKM"),
    media.Movie("Happy Gilmore",
                "A rejected hockey player puts his skills to the golf course to save his grandmother's "
                "house.",
                "http://images3.static-bluray.com/movies/covers/16771_slip.jpg",
                "https://www.youtube.com/watch?v=y1emDAYCfVQ"),
    media.Movie("School of Rock",
                "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a "
                "strict elementary private school, only to try and turn it into a rock band.",
                "https://www.movieposter.com/posters/archive/main/16/MPW-8303",
                "https://www.youtube.com/watch?v=3PsUJFEBC74")
]

fresh_tomatoes.open_movies_page(movies)

print media.Movie.valid_ratings
