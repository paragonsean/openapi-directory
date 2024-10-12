from typing import List, Dict
from aiohttp import web

from openapi_server.models.routes_v2_sip_domain import RoutesV2SipDomain
from openapi_server import util


async def fetch_sip_domain(request: web.Request, sip_domain) -> web.Response:
    """fetch_sip_domain

    

    :param sip_domain: 
    :type sip_domain: str

    """
    return web.Response(status=200)


async def update_sip_domain(request: web.Request, sip_domain, friendly_name=None, voice_region=None) -> web.Response:
    """update_sip_domain

    

    :param sip_domain: 
    :type sip_domain: str
    :param friendly_name: 
    :type friendly_name: str
    :param voice_region: 
    :type voice_region: str

    """
    return web.Response(status=200)
