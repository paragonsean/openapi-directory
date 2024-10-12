from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_information import ServiceInformation
from openapi_server import util


async def service_information_statistics(request: web.Request, ) -> web.Response:
    """This resource can be used to check the status of the service.

    


    """
    return web.Response(status=200)
