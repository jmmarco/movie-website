import media
import fresh_tomatoes

star_trek = media.Movie("Star Trek Into Darkness", "After the crew of the Enterprise find an unstoppable force of terror from within their own organization, Captain Kirk leads a manhunt to a war-zone world to capture a one-man weapon of mass destruction.",
                       "http://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",
                       "http://youtu.be/U_IWKaoN6hg")


ted = media.Movie("Ted", "John Bennett is a lonely child who dearly wished for his new Christmas gift, a large teddy bear named Ted",
                  "http://upload.wikimedia.org/wikipedia/en/6/62/Ted_poster.jpg",
                  "http://youtu.be/9fbo_pQvU7M")


the_intouchables = media.Movie("The Intouchables", "After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caretaker.",
                              "http://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg", "http://youtu.be/34WIbmXkewU")



planes = media.Movie("Planes", "A cropdusting plane with a fear of heights lives his dream of competing in a famous around-the-world aerial race.",
                     "http://upload.wikimedia.org/wikipedia/en/7/7b/Planes_FilmPoster.jpeg", "http://youtu.be/ibAxkCJfvC4")

kill_bill = media.Movie("Kill Bill", "The Bride wakens from a four-year coma. The child she carried in her womb is gone. Now she must wreak vengeance on the team of assassins who betrayed her - a team she was once part of.",
                        "http://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg", "http://youtu.be/7kSuas6mRpk")

premium_rush = media.Movie("Premium Rush", "In Manhattan, a bike messenger picks up an envelope that attracts the interest of a dirty cop, who pursues the cyclist throughout the city.",
                            "http://upload.wikimedia.org/wikipedia/en/4/46/Premium_rush_film.jpg", "http://youtu.be/Pn6ie1zCkZU")

movies = [star_trek, ted, the_intouchables, planes, kill_bill, premium_rush]
fresh_tomatoes.open_movies_page(movies)

#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
