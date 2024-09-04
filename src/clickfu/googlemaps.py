from .clickFuUtils import cfAction


class googleMap(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)

    def name(self):
        return "Google Maps"

    def desc(self):
        return "Goto Location on Google Maps"

    def createURL(self, lat, long):
        url = f"https://www.google.com/maps/@{lat},{long},17z"
        return url
