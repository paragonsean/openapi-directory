from typing import List, Dict
from aiohttp import web

from openapi_server.models.build import Build
from openapi_server.models.build_setup import BuildSetup
from openapi_server.models.build_status import BuildStatus
from openapi_server.models.error import Error
from openapi_server import util


async def create_site_build(request: web.Request, site_id, build=None) -> web.Response:
    """create_site_build

    

    :param site_id: 
    :type site_id: str
    :param build: 
    :type build: dict | bytes

    """
    build = BuildSetup.from_dict(build)
    return web.Response(status=200)


async def get_account_build_status(request: web.Request, account_id) -> web.Response:
    """get_account_build_status

    

    :param account_id: 
    :type account_id: str

    """
    return web.Response(status=200)


async def get_site_build(request: web.Request, build_id) -> web.Response:
    """get_site_build

    

    :param build_id: 
    :type build_id: str

    """
    return web.Response(status=200)


async def list_site_builds(request: web.Request, site_id, page=None, per_page=None) -> web.Response:
    """list_site_builds

    

    :param site_id: 
    :type site_id: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def notify_build_start(request: web.Request, build_id) -> web.Response:
    """notify_build_start

    

    :param build_id: 
    :type build_id: str

    """
    return web.Response(status=200)
