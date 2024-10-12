from typing import List, Dict
from aiohttp import web

from openapi_server.models.health_check200_response import HealthCheck200Response
from openapi_server import util


async def health_check(request: web.Request, accept_language) -> web.Response:
    """/health/check

    Health check Use this service to determine whether the Viator API is presently online and that your API key is valid. You should receive a response identical to the example shown. If you have not yet received an API key, please request one from your business development partner. If you have not yet signed up as a Viator merchant partner and would like to, please visit our [distribution partner website](https://www.viator.com/distribution-partners?mcid&#x3D;58463#api-solutions).\&quot; 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str

    """
    return web.Response(status=200)
