#entertainment_center.py
import media
import fresh_tomatoes

#define movies using Movie class in media.py and place in list
fight_club = media.Movie("Fight Club",
                         "A tale of a guy with split personality disorder",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=J8FRBYOFu2w")

avatar = media.Movie("Avatar",
                     "A story of a marine who falls in love on another world",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

passengers = media.Movie("Passengers",
                         "A story of two people in hibernation on a spaceship who wake up 90 years too early",
                         "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")

planes = media.Movie("Planes Trains and Automobiles",
                     "Some travellers get delayed, some get frustrated and then there are some travellers that get Dell Griffith-ed",
                     "http://static.rogerebert.com/uploads/movie/movie_poster/planes-trains-and-automobiles-1987/large_3r93acWXFDcxOwo4XfeBi5RhuPR.jpg",
                     "https://www.youtube.com/watch?v=VWGqGHMO294")
                     
money = media.Movie("Money Pit",
                    "A husband and wife get buy into a lovely mansion that they soon find out is a money pit",
                    "https://images-na.ssl-images-amazon.com/images/I/51YNNPFH37L.jpg",
                    "https://www.youtube.com/watch?v=TLLQquBdU8M")
                    
scoundrels = media.Movie("Dirty Rotten Scoundrels",
                         "A comedy about two men that try to swindle a swindler out of $50'000",
                         "https://images-na.ssl-images-amazon.com/images/I/51QKEXSV7WL.jpg",
                         "https://www.youtube.com/watch?v=0ke-v0e3Cd4")
                         
movies = [fight_club, avatar, passengers, planes, money, scoundrels]

#Now we will use the fresh_tomatoes.py to create our webpage
fresh_tomatoes.open_movies_page(movies)
