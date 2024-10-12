from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_profile import BusinessProfile
from openapi_server.models.get_business_profile_response import GetBusinessProfileResponse
from openapi_server import util


async def get_business_profile(request: web.Request, ) -> web.Response:
    """Get-Business-Profile

    


    """
    return web.Response(status=200)


async def update_business_profile(request: web.Request, body) -> web.Response:
    """Update-Business-Profile

    

    :param body: 
    :type body: dict | bytes

    """
    body = BusinessProfile.from_dict(body)
    return web.Response(status=200)
