import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # make a list with at least 5 movie titles
        movies = [
            ("The Big Lebowski"),
            ("Secret Life of Pets"),
            ("Moana"),
            ("Rogue One: A Star Wars Story"),
            ("Doctor Strange")
        ]

        # randomly choose one of the movies, and return it
        randIndex = random.randint(0, (len(movies)-1))

        return movies[randIndex]

    def get(self):
        # choose a movie by invoking our new function
        movieToday = self.getRandomMovie()
        movieTomorrow = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movieToday + "</p>"

        # pick a different random movie, and display it under
        content += "<h1>Tommorrow's Movie</h1>"
        content += "<p>" + movieTomorrow + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
