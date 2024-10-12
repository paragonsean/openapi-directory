from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource import Resource
from openapi_server import util


async def get_resource(request: web.Request, name) -> web.Response:
    """Get Resource

    

    :param name: Unique name/business identifier of the Service or API resource
    :type name: str

    """
    return web.Response(status=200)


async def get_resources_by_service(request: web.Request, service_id) -> web.Response:
    """Get Resources by Service

    

    :param service_id: Unique identifier of the Service or API the resources are attached to
    :type service_id: str

    """
    return web.Response(status=200)
