from typing import List, Dict
from aiohttp import web

from openapi_server.models.brand_vetting_enum_vetting_provider import BrandVettingEnumVettingProvider
from openapi_server.models.list_brand_vetting_response import ListBrandVettingResponse
from openapi_server.models.messaging_v1_brand_registrations_brand_vetting import MessagingV1BrandRegistrationsBrandVetting
from openapi_server import util


async def create_brand_vetting(request: web.Request, brand_sid, vetting_provider, vetting_id=None) -> web.Response:
    """create_brand_vetting

    

    :param brand_sid: The SID of the Brand Registration resource of the vettings to create .
    :type brand_sid: str
    :param vetting_provider: 
    :type vetting_provider: str
    :param vetting_id: The unique ID of the vetting
    :type vetting_id: str

    """
    return web.Response(status=200)


async def fetch_brand_vetting(request: web.Request, brand_sid, brand_vetting_sid) -> web.Response:
    """fetch_brand_vetting

    

    :param brand_sid: The SID of the Brand Registration resource of the vettings to read .
    :type brand_sid: str
    :param brand_vetting_sid: The Twilio SID of the third-party vetting record.
    :type brand_vetting_sid: str

    """
    return web.Response(status=200)


async def list_brand_vetting(request: web.Request, brand_sid, vetting_provider=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_brand_vetting

    

    :param brand_sid: The SID of the Brand Registration resource of the vettings to read .
    :type brand_sid: str
    :param vetting_provider: The third-party provider of the vettings to read
    :type vetting_provider: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
