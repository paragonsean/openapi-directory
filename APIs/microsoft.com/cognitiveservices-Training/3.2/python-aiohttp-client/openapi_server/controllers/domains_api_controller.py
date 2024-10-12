from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.domain import Domain
from openapi_server import util


async def get_domain(request: web.Request, domain_id) -> web.Response:
    """Get information about a specific domain.

    

    :param domain_id: The id of the domain to get information about.
    :type domain_id: str
    :type domain_id: str

    """
    return web.Response(status=200)


async def get_domains(request: web.Request, ) -> web.Response:
    """Get a list of the available domains.

    


    """
    return web.Response(status=200)
