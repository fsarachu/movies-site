import webbrowser


class Movie():
    def __init__(self, title, storyline, poster_image, youtube_trailer_url):
        self.title = title
        self.storyline = storyline
        self.image_url = poster_image
        self.trailer_url = youtube_trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
