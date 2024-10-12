from typing import List, Dict
from aiohttp import web

from openapi_server.models.contact_types_contact_type_id_get200_response import ContactTypesContactTypeIdGet200Response
from openapi_server.models.contact_types_get200_response import ContactTypesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server import util


async def contact_types_contact_type_id_get(request: web.Request, contact_type_id) -> web.Response:
    """Get details about one contact type

    

    :param contact_type_id: 
    :type contact_type_id: str

    """
    return web.Response(status=200)


async def contact_types_get(request: web.Request, identifier=None) -> web.Response:
    """Get list of contact types supported in Apacta

    

    :param identifier: Search for specific identifier value
    :type identifier: str

    """
    return web.Response(status=200)
