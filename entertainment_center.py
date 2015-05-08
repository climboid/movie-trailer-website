import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
												"A story of a boy that comes to life",
												"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
												"https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
										 "A marine on an alien planet",
										 "http://fc02.deviantart.net/fs70/f/2010/014/b/c/Avatar_by_Eggar919.jpg",
										 "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

rambo = media.Movie("Rambo",
										"A soldier that suffers war",
										"http://i2.cdnds.net/13/36/618x400/rambo.jpg",
										"https://www.youtube.com/watch?v=OI0kenxkoNg")

movies = [toy_story, avatar, rambo]
fresh_tomatoes.open_movies_page(movies)