
from .clickFuUtils import cfAction

class osmViewMap(cfAction):
    def __init__(self,iface):
        cfAction.__init__(self,self.name(),iface)
        return None

    def name(self):
        return "View OSM map"
    def desc(self):
        return "Goto Location on OpenStreetMap"

    def createURL(self,lat,long):
        url = "http://www.openstreetmap.org/#map=17/%s/%s" % (lat,long)
        return url


class osmEditMap(cfAction):
    def __init__(self,iface):
        cfAction.__init__(self,self.name(),iface)
        return None

    def name(self):
        return "Edit OSM with iD"
    def desc(self):
        return "Goto Location on OpenStreetMap and start editing with iD"

    def createURL(self,lat,long):
        url = "http://www.openstreetmap.org/edit?editor=id#map=17/%s/%s" % (lat,long)
        return url

class osmEditMapJOSM(cfAction):
    def __init__(self,iface):
        cfAction.__init__(self,self.name(),iface)
        return None

    def name(self):
        return "Edit OSM with JOSM"
    def desc(self):
        return "Goto Location on OpenStreetMap and start editing with JOSM"

    def createURL(self,lat,long):
        
        url = "http://127.0.0.1:8111/load_and_zoom?left=%s&top=%s&right=%s&bottom=%s" % (long-0.005,lat+0.005,long+0.005,lat-0.005)
        return url
