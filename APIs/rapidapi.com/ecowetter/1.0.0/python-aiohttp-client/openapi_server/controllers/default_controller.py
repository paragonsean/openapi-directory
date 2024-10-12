from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def public_history_get(request: web.Request, q=None, _from=None, to=None) -> web.Response:
    """Wetter 2021 für Berlin, Reichstag

    Abfrage der Wettervorhersage für einen Ort, der entweder durch Angabe eines Suchbegriffs mit dem Parameter &#x60;q&#x60; oder durch Geo-Koordinaten in den Parametern &#x60;lat&#x60; und &#x60;lon&#x60; spezifiziert wird.

    :param q: Ortssuche mit Freitext
    :type q: str
    :param _from: Startdatum der Abfrage im Format (JJJJ-MM-DD)
    :type _from: str
    :param to: Enddatum der Abfrage im Format (JJJJ-MM-DD)
    :type to: str

    """
    return web.Response(status=200)
