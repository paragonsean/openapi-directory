from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def export_csv_registrierkassen_registrierkasse_uuid_belege_get(request: web.Request, registrierkasse_uuid, before=None, after=None, posten=None) -> web.Response:
    """export_csv_registrierkassen_registrierkasse_uuid_belege_get

    

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export.
    :type registrierkasse_uuid: str
    :param before: Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type before: str
    :param after: Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type after: str
    :param posten: Export &#x60;Posten&#x60; instead of &#x60;Belegdaten&#x60;.
    :type posten: bool

    """
    return web.Response(status=200)


async def export_dep131_registrierkassen_registrierkasse_uuid_belege_get(request: web.Request, registrierkasse_uuid, before=None, after=None) -> web.Response:
    """export_dep131_registrierkassen_registrierkasse_uuid_belege_get

    

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export.
    :type registrierkasse_uuid: str
    :param before: Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type before: str
    :param after: Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type after: str

    """
    return web.Response(status=200)


async def export_dep7_registrierkassen_registrierkasse_uuid_belege_get(request: web.Request, registrierkasse_uuid, before=None, after=None) -> web.Response:
    """export_dep7_registrierkassen_registrierkasse_uuid_belege_get

    

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export.
    :type registrierkasse_uuid: str
    :param before: Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type before: str
    :param after: Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type after: str

    """
    return web.Response(status=200)


async def export_gobd_registrierkassen_registrierkasse_uuid_get(request: web.Request, registrierkasse_uuid, before=None, after=None) -> web.Response:
    """export_gobd_registrierkassen_registrierkasse_uuid_get

    

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export.
    :type registrierkasse_uuid: str
    :param before: Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type before: str
    :param after: Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type after: str

    """
    return web.Response(status=200)


async def export_html_belege_beleg_uuid_get(request: web.Request, beleg_uuid) -> web.Response:
    """export_html_belege_beleg_uuid_get

    

    :param beleg_uuid: The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export.
    :type beleg_uuid: str

    """
    return web.Response(status=200)


async def export_pdf_belege_beleg_uuid_get(request: web.Request, beleg_uuid) -> web.Response:
    """export_pdf_belege_beleg_uuid_get

    

    :param beleg_uuid: The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export.
    :type beleg_uuid: str

    """
    return web.Response(status=200)


async def export_qr_belege_beleg_uuid_get(request: web.Request, beleg_uuid) -> web.Response:
    """export_qr_belege_beleg_uuid_get

    

    :param beleg_uuid: The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export.
    :type beleg_uuid: str

    """
    return web.Response(status=200)


async def export_thermal_print_belege_beleg_uuid_get(request: web.Request, beleg_uuid, qr=None, width=None, dialect=None, encoding=None) -> web.Response:
    """export_thermal_print_belege_beleg_uuid_get

    

    :param beleg_uuid: The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export.
    :type beleg_uuid: str
    :param qr: Should the RKSV QR code should be rendered?
    :type qr: bool
    :param width: Number of characters per line.
    :type width: int
    :param dialect: The thermal printer dialect.
    :type dialect: str
    :param encoding: The encoding of the binary data.
    :type encoding: str

    """
    return web.Response(status=200)


async def export_xls_registrierkassen_registrierkasse_uuid_belege_get(request: web.Request, registrierkasse_uuid, before=None, after=None) -> web.Response:
    """export_xls_registrierkassen_registrierkasse_uuid_belege_get

    

    :param registrierkasse_uuid: The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export.
    :type registrierkasse_uuid: str
    :param before: Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type before: str
    :param after: Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse).
    :type after: str

    """
    return web.Response(status=200)
