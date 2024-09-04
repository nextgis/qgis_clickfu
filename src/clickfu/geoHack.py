from .clickFuUtils import cfAction, convertLat, convertLon


class geoHack(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)

    def name(self):
        return "GeoHack Map Sources"

    def desc(self):
        return "Wikimedia ToolServer's GeoHack"

    def createURL(self, lat, long):
        url = "http://tools.wmflabs.org/geohack/geohack.php?params=%s_%s_%s_%s_%s_%s_%s_%s"
        latV = convertLat(lat)
        lonV = convertLon(long)
        url = url % (
            latV[0],
            latV[1],
            latV[2],
            latV[3],
            lonV[0],
            lonV[1],
            lonV[2],
            lonV[3],
        )
        return url
