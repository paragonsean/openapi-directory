from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_general_informations200_response import ApiGeneralInformations200Response
from openapi_server.models.api_informations200_response import ApiInformations200Response
from openapi_server.models.api_sub_informations200_response import ApiSubInformations200Response
from openapi_server import util


async def api_general_informations(request: web.Request, ) -> web.Response:
    """List all endoints

    List all endpoints and their version


    """
    return web.Response(status=200)


async def api_informations(request: web.Request, endpoint_name) -> web.Response:
    """Get information about one API endpoint

    Get the description and the list of supported version for one API endpoint

    :param endpoint_name: Name of the endpoint for which one wants information
    :type endpoint_name: str

    """
    return web.Response(status=200)


async def api_sub_informations(request: web.Request, section_id) -> web.Response:
    """Get information on endpoint in a section

    Get all endpoints in the given section with their supported version.

    :param section_id: Id of the API section
    :type section_id: str

    """
    return web.Response(status=200)
