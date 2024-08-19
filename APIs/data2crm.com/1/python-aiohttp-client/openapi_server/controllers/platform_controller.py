from typing import List, Dict
from aiohttp import web

from openapi_server.models.platform_entity import PlatformEntity
from openapi_server import util


async def get_platform_collection(request: web.Request, x_api2_crm_user_key, page_size=None, page=None, fields=None, sort=None) -> web.Response:
    """GET for platform

    Returns all platforms from the system

    :param x_api2_crm_user_key: API2CRM user key
    :type x_api2_crm_user_key: str
    :param page_size: Amount of results (default: 25)
    :type page_size: int
    :param page: Page to show (default: 1)
    :type page: int
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str
    :param sort: Specifies ascending or descending sort on existing fields
    :type sort: str

    """
    return web.Response(status=200)


async def get_platform_entity(request: web.Request, x_api2_crm_user_key, type, fields=None) -> web.Response:
    """GET for platform

    Return platform information

    :param x_api2_crm_user_key: API2CRM user key
    :type x_api2_crm_user_key: str
    :param type: Platform type
    :type type: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str

    """
    return web.Response(status=200)
