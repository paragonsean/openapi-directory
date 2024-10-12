from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_profile_about_response import GetProfileAboutResponse
from openapi_server.models.get_profile_photo_response import GetProfilePhotoResponse
from openapi_server.models.profile_about import ProfileAbout
from openapi_server import util


async def get_profile_about(request: web.Request, ) -> web.Response:
    """Get-Profile-About

    


    """
    return web.Response(status=200)


async def get_profile_photo(request: web.Request, format=None) -> web.Response:
    """Get-Profile-Photo

    

    :param format: 
    :type format: str

    """
    return web.Response(status=200)


async def update_profile_about(request: web.Request, body) -> web.Response:
    """Update-Profile-About

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProfileAbout.from_dict(body)
    return web.Response(status=200)


async def update_profile_photo(request: web.Request, file) -> web.Response:
    """Update-Profile-Photo

    

    :param file: 
    :type file: str

    """
    return web.Response(status=200)
