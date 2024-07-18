# contrib by ANAT01

from .clickFuUtils import cfAction
from .compat import (
    QgsPointXY,
)


class Rosreestr(cfAction):
    def __init__(self, iface):
        cfAction.__init__(self, self.name(), iface)

    def name(self):
        return "Rosreestr PKK"

    def desc(self):
        return "Goto Location on Rosreestr PKK"

    def createURL(self, lat, long):
        point = QgsPointXY(long, lat)
        pt4326 = point

        # https://pkk.rosreestr.ru/#/search/{Y},{X}/{ZOOM}/{PARAMETERS}"
        url = f"https://pkk.rosreestr.ru/#/search/{pt4326.y()},{pt4326.x()}/10"

        return url
