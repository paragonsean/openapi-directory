from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_new_id_get200_response import ApplicationNewIDGet200Response
from openapi_server.models.application_new_id_get403_response import ApplicationNewIDGet403Response
from openapi_server.models.application_status_get200_response import ApplicationStatusGet200Response
from openapi_server.models.application_status_get500_response import ApplicationStatusGet500Response
from openapi_server.models.error import Error
from openapi_server import util


async def application_new_idget(request: web.Request, doc_type) -> web.Response:
    """Create a new WeGA ID

    

    :param doc_type: The WeGA document type
    :type doc_type: List[str]

    """
    return web.Response(status=200)


async def application_status_get(request: web.Request, ) -> web.Response:
    """Get status information about the running WeGA-WebApp

    


    """
    return web.Response(status=200)
