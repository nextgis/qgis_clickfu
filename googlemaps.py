
from .clickFuUtils import cfAction

class googleMap(cfAction):
    def __init__(self,iface):
        cfAction.__init__(self,self.name(),iface)
        return None
    def name(self):
        return "Google Maps"
    def desc(self):
        return "Goto Location on Google Maps"

    def createURL(self,lat,long):
        url = "https://www.google.com/maps/@%s,%s,17z" % (lat,long)
        return url
