from typing import List, Dict
from aiohttp import web

from openapi_server.models.org import Org
from openapi_server.models.org_response import OrgResponse
from openapi_server import util


async def add_organization(request: web.Request, org_object) -> web.Response:
    """add_organization

    Create an org

    :param org_object: Org information
    :type org_object: dict | bytes

    """
    org_object = Org.from_dict(org_object)
    return web.Response(status=200)


async def get_my_organization(request: web.Request, ) -> web.Response:
    """get_my_organization

    Get org information


    """
    return web.Response(status=200)
