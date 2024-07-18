from .clickFuUtils import cfAction


class osmViewMap(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)

    def name(self):
        return "View OSM map"

    def desc(self):
        return "Goto Location on OpenStreetMap"

    def createURL(self, lat, long):
        url = f"http://www.openstreetmap.org/#map=17/{lat}/{long}"
        return url


class osmEditMap(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)

    def name(self):
        return "Edit OSM with iD"

    def desc(self):
        return "Goto Location on OpenStreetMap and start editing with iD"

    def createURL(self, lat, long):
        url = (
            f"http://www.openstreetmap.org/edit?editor=id#map=17/{lat}/{long}"
        )
        return url


class osmEditMapJOSM(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)

    def name(self):
        return "Edit OSM with JOSM"

    def desc(self):
        return "Goto Location on OpenStreetMap and start editing with JOSM"

    def createURL(self, lat, long):
        url = f"http://127.0.0.1:8111/load_and_zoom?left={long - 0.005}&top={lat + 0.005}&right={long + 0.005}&bottom={lat - 0.005}"
        return url
