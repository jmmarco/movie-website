import media
import fresh_tomatoes

# Movie instances

star_trek = media.Movie("Star Trek Into Darkness",
                        "After the crew of the Enterprise find an unstoppable"
                        " force of terror from within their own organization,"
                        " Captain Kirk leads a manhunt to a war-zone world to"
                        " capture a one-man weapon of mass destruction.",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",  # noqa
                        "http://youtu.be/U_IWKaoN6hg")

ted = media.Movie("Ted",
                  "John Bennett is a lonely child who dearly wished for his "
                  " new Christmas gift, a large teddy bear named Ted",
                  "http://upload.wikimedia.org/wikipedia/en/6/62/Ted_poster.jpg",  # noqa
                  "http://youtu.be/9fbo_pQvU7M")

the_intouchables = media.Movie("The Intouchables",
                               "After he becomes a quadriplegic from a"
                               " paragliding accident, an aristocrat hires a"
                               " young man from the projects to be his"
                               " caretaker.",
                              "http://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",  # noqa
                               "http://youtu.be/34WIbmXkewU")

planes = media.Movie("Planes",
                     "A cropdusting plane with a fear of heights lives his"
                     " dream of competing in a famous around-the-world aerial"
                     " race.",
                     "http://upload.wikimedia.org/wikipedia/en/7/7b/Planes_FilmPoster.jpeg",  # noqa
                     "http://youtu.be/ibAxkCJfvC4")

kill_bill = media.Movie("Kill Bill",
                        "The Bride wakens from a four-year coma. The child"
                        " she carried in her womb is gone. Now she must wreak"
                        " vengeance on the team of assassins who betrayed her"
                        " - a team she was once part of.",
                        "http://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",  # noqa
                        "http://youtu.be/7kSuas6mRpk")

premium_rush = media.Movie("Premium Rush",
                           "In Manhattan, a bike messenger picks up an"
                           " envelope that attracts the interest of a dirty"
                           " cop, who pursues the cyclist throughout the"
                           " city.",
                           "http://upload.wikimedia.org/wikipedia/en/4/46/Premium_rush_film.jpg",  # noqa
                           "http://youtu.be/Pn6ie1zCkZU")

# Add each movie to the list
movies = [star_trek, ted, the_intouchables, planes, kill_bill, premium_rush]

i = 1
for movie in movies:
    movie.number = i
    i += 1
    print movie.number


# Open movies
fresh_tomatoes.open_movies_page(movies)
