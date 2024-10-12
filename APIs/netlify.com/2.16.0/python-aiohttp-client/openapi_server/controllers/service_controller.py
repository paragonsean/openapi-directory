from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.service import Service
from openapi_server import util


async def get_services(request: web.Request, search=None) -> web.Response:
    """get_services

    

    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def show_service(request: web.Request, addon_name) -> web.Response:
    """show_service

    

    :param addon_name: 
    :type addon_name: str

    """
    return web.Response(status=200)


async def show_service_manifest(request: web.Request, addon_name) -> web.Response:
    """show_service_manifest

    

    :param addon_name: 
    :type addon_name: str

    """
    return web.Response(status=200)
