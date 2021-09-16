#contrib by ANAT1

from .clickFuUtils import cfAction
from .compat import QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsPointXY


class Rosreestr(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)

    def name(self):
        return "Rosreestr PKK"

    def desc(self):
        return "Goto Location on Rosreestr PKK"

    def createURL(self, lat, long):
        point = QgsPointXY(long, lat)
        pt3857 = QgsCoordinateTransform(
            QgsCoordinateReferenceSystem.fromEpsgId(4326),
            QgsCoordinateReferenceSystem.fromEpsgId(3857)
        ).transform(point)
        
        url = "http://pkk5.rosreestr.ru/#x=%.9f&y=%.9f&z=19&text=%s %s&type=1&app=search&opened=1" % (
            pt3857.x(), pt3857.y(), str("{0:.6f}".format(lat)).replace('.', ','),
            str("{0:.6f}".format(long)).replace('.', ',')
        )
        return url