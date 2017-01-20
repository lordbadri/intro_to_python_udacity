import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys, which comes to life",
                        "https://i.ytimg.com/vi/3jC6McxjCnE/hqdefault.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print(avatar.storyline)
#avatar.show_trailer()

movies=[toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
