from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_clutter_request import AddClutterRequest
from openapi_server import util


async def add_clutter(request: web.Request, body) -> web.Response:
    """Upload clutter data as GeoJSON

    Upload GeoJSON lineString and polygon features to your account. The height property is in metres and the material code / type / attenuation are.. 1 Trees – 0.25,2Trees + 0.5,3 Timber – 1.0,4 Timber + 1.5,5 Brick –  1.5,6 Brick + 2.0,7 Concrete – 3.0,8 Concrete + 4.0,9 Metal 6.0

    :param body: 
    :type body: dict | bytes

    """
    body = AddClutterRequest.from_dict(body)
    return web.Response(status=200)


async def delete(request: web.Request, cid) -> web.Response:
    """Delete a calculation from the database.

    Warning! you could lose data. This function will delete the entry from the database and the file from the disk. Accidental deletion can be reversed by contacting support with biscuits who maintain an offsite backup.

    :param cid: Unique calculation ID number
    :type cid: int

    """
    return web.Response(status=200)


async def delete_network(request: web.Request, nid) -> web.Response:
    """Delete an entire network

    Warning! you could lose data. This function will delete the entry from the database and the file from the disk. Accidental deletion can be reversed by contacting support with biscuits who maintain an offsite backup.

    :param nid: Network name
    :type nid: str

    """
    return web.Response(status=200)


async def export(request: web.Request, file, fmt) -> web.Response:
    """Export a calculation in a GIS file format

    Download your data in a format suitable for a third party viewer like Google Earth or ESRI Arcmap.

    :param file: Calculation file name
    :type file: str
    :param fmt: Raster/Vector file format: KML, KMZ, SHP, GeoTIFF
    :type fmt: str

    """
    return web.Response(status=200)


async def list(request: web.Request, n=None, e=None, s=None, w=None) -> web.Response:
    """List calculations from your archive

    List your area and path calculations, sorted by time and limited to the last few hundred. To fetch all for a given network append a &#39;net&#39; filter with the network name.

    :param n: North bounding box
    :type n: float
    :param e: East bounding box
    :type e: float
    :param s: South bounding box
    :type s: float
    :param w: West bounding box
    :type w: float

    """
    return web.Response(status=200)
