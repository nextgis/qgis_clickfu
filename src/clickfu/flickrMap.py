from .clickFuUtils import cfAction


class flickrPics(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)
        return

    def name(self):
        return "Flickr Maps"

    def desc(self):
        return "Show Flickr photos near point"

    def createURL(self, lat, long):
        url = "http://www.flickr.com/map/?fLat=%s&fLon=%s&zl=17" % (lat, long)
        return url
