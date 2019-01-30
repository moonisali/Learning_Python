import media
import toms

toy_story = media.Movie("Toy Story",
                        "A story of a boy whose toys live forever",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "An indegenous war on colonisers",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=xy1ccIP_i24")
""" print(avatar.title)
print(avatar.storyline)
avatar.show_trailer() """

invictus = media.Movie("Invictus",
                       "An inspiring epic about the rise of a united South AFrica",
                       "https://upload.wikimedia.org/wikipedia/en/0/05/Invictus-poster.png",
                       "https://www.youtube.com/watch?v=o2isdUuHmFY")

""" print(invictus.title)
print(invictus.storyline)
invictus.show_trailer()
invictus.show_poster()"""

lotr = media.Movie("Lord of the Rings","A story through the middle earth",
                   "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                   "https://www.youtube.com/watch?v=V75dMMIW2B4")

#lotr.show_trailer()

cast_away = media.Movie("Cast Away", "A story of man who finds himself after being shipwrecked",
                   "https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",
                   "https://www.youtube.com/watch?v=PJvosb4UCLs")

#cast_away.show_trailer()

goal = media.Movie("Goal Series", "A tale of a boy who becomes a star by starting out from rags",
                   "https://upload.wikimedia.org/wikipedia/en/9/96/GoalPoster.jpg",
                   "https://www.youtube.com/watch?v=qGhCJXrqZwE")
movies = [toy_story, avatar, invictus, lotr, cast_away, goal]
toms.open_movies_page(movies)
