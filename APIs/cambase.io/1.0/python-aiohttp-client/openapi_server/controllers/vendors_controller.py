from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v1_vendors_create(request: web.Request, vendor_name, vendor_info=None, vendor_url=None, vendor_mac=None) -> web.Response:
    """Creates a new Vendor

    

    :param vendor_name: Name
    :type vendor_name: str
    :param vendor_info: Info.
    :type vendor_info: str
    :param vendor_url: Website
    :type vendor_url: str
    :param vendor_mac: MAC
    :type vendor_mac: str

    """
    return web.Response(status=200)


async def api_v1_vendors_id_json_patch(request: web.Request, id, vendor_name=None, vendor_info=None, vendor_url=None, vendor_mac=None) -> web.Response:
    """Updates an existing Vendor

    

    :param id: Vendor ID
    :type id: str
    :param vendor_name: Name
    :type vendor_name: str
    :param vendor_info: Info.
    :type vendor_info: str
    :param vendor_url: Website
    :type vendor_url: str
    :param vendor_mac: MAC
    :type vendor_mac: str

    """
    return web.Response(status=200)


async def api_v1_vendors_id_json_put(request: web.Request, id, vendor_name=None, vendor_info=None, vendor_url=None, vendor_mac=None) -> web.Response:
    """Updates an existing Vendor

    

    :param id: Vendor ID
    :type id: str
    :param vendor_name: Name
    :type vendor_name: str
    :param vendor_info: Info.
    :type vendor_info: str
    :param vendor_url: Website
    :type vendor_url: str
    :param vendor_mac: MAC
    :type vendor_mac: str

    """
    return web.Response(status=200)


async def api_v1_vendors_index(request: web.Request, page=None, order=None) -> web.Response:
    """Fetches all Vendors

    

    :param page: Page number
    :type page: int
    :param order: Sort order
    :type order: str

    """
    return web.Response(status=200)


async def api_v1_vendors_show(request: web.Request, id, order=None) -> web.Response:
    """Fetches a single Vendor

    

    :param id: Vendor ID
    :type id: str
    :param order: Sort order
    :type order: str

    """
    return web.Response(status=200)
