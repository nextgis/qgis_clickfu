from .clickFuUtils import cfAction


class flickrPics(cfAction):
    def __init__(self, iface):
        super().__init__(self.name(), iface)

    def name(self):
        return "Flickr Maps"

    def desc(self):
        return "Show Flickr photos near point"

    def createURL(self, lat, long):
        url = f"http://www.flickr.com/map/?fLat={lat}&fLon={long}&zl=17"
        return url
