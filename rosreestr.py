from clickFuUtils import cfAction
from qgis.core import QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsPoint


class Rosreestr(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)

    def name(self):
        return "Rosreestr PKK"

    def desc(self):
        return "Goto Location on Rosreestr PKK"

    def createURL(self, lat, long):
        point = QgsPoint(long, lat)
        pt3857 = QgsCoordinateTransform(
            QgsCoordinateReferenceSystem(4326),
            QgsCoordinateReferenceSystem(3857)
        ).transform(point)
        url = "http://pkk5.rosreestr.ru/#x=%.9f&y=%.9f&z=19&text=%s %s&type=1&app=search&opened=1" % (
            pt3857.x(), pt3857.y(), str("{0:.6f}".format(lat)).replace('.', ','),
            str("{0:.6f}".format(long)).replace('.', ',')
        )
        return url
