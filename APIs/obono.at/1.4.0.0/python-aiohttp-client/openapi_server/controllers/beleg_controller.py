from typing import List, Dict
from aiohttp import web

from openapi_server.models.abschlussbelegdaten import Abschlussbelegdaten
from openapi_server.models.beleg import Beleg
from openapi_server.models.belegdaten import Belegdaten
from openapi_server.models.belege import Belege
from openapi_server import util


async def add_beleg(request: web.Request, registrierkasse_uuid, beleg_uuid, body) -> web.Response:
    """add_beleg

    Signs a receipt and stores it in the \&quot;Datenerfassungsprotokoll\&quot;.

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to use for signing data.
    :type registrierkasse_uuid: str
    :param beleg_uuid: The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to store.
    :type beleg_uuid: str
    :param body: An object that contains all data for a particular &#x60;Beleg&#x60; and is formatted according to RKSV \&quot;Signaturformat\&quot;.
    :type body: dict | bytes

    """
    body = Belegdaten.from_dict(body)
    return web.Response(status=200)


async def belege_beleg_uuid_get(request: web.Request, beleg_uuid) -> web.Response:
    """belege_beleg_uuid_get

    Retrieves a particular &#x60;Beleg&#x60; from the \&quot;Datenerfassungsprotokoll\&quot;.

    :param beleg_uuid: The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to fetch.
    :type beleg_uuid: str

    """
    return web.Response(status=200)


async def create_abschluss(request: web.Request, registrierkasse_uuid, body) -> web.Response:
    """create_abschluss

    Generates an &#x60;Abschlussbeleg&#x60;.

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the &#x60;Beleg&#x60; collection.
    :type registrierkasse_uuid: str
    :param body: An object that contains all data for a particular &#x60;Abschlussbeleg&#x60;.
    :type body: dict | bytes

    """
    body = Abschlussbelegdaten.from_dict(body)
    return web.Response(status=200)


async def get_beleg(request: web.Request, registrierkasse_uuid, beleg_uuid) -> web.Response:
    """get_beleg

    Retrieves a particular &#x60;Beleg&#x60; from the \&quot;Datenerfassungsprotokoll\&quot;.

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; that contains the requested &#x60;Beleg&#x60;.
    :type registrierkasse_uuid: str
    :param beleg_uuid: The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to fetch.
    :type beleg_uuid: str

    """
    return web.Response(status=200)


async def get_belege(request: web.Request, registrierkasse_uuid, format, order=None, limit=None, offset=None, before=None, after=None, gte=None, lte=None) -> web.Response:
    """get_belege

    Retrieves the &#x60;Beleg&#x60; collection from the \&quot;Datenerfassungsprotokoll\&quot;.

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the &#x60;Beleg&#x60; collection.
    :type registrierkasse_uuid: str
    :param format: Determines the format of the &#x60;Beleg&#x60; collection.
    :type format: str
    :param order: Determines the sorting order.
    :type order: str
    :param limit: Limits the number of returned results.
    :type limit: int
    :param offset: Skips the specified number of results from the result set.
    :type offset: int
    :param before: Only return results that where saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type before: str
    :param after: Only return results that where saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type after: str
    :param gte: Only return results that have at least a particular &#x60;Belegnummer&#x60;.
    :type gte: int
    :param lte: Only return results that have at most a particular &#x60;Belegnummer&#x60;.
    :type lte: int

    """
    return web.Response(status=200)
