class Media:
    def get_details(self):
        return "This is a media item"


class Movie(Media):
    def get_details(self):
        return "Movie duration: 2 hours"


class Series(Media):
    def get_details(self):
        return "Series seasons: 3"


watchlist = [Movie(), Series()]

for item in watchlist:
    print(item.get_details())
