from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_reference_entities_code200_response import GetReferenceEntitiesCode200Response
from openapi_server.models.patch_reference_entity_code_request import PatchReferenceEntityCodeRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.reference_entities import ReferenceEntities
from openapi_server import util


async def get_reference_entities(request: web.Request, search_after=None) -> web.Response:
    """Get list of reference entities

    This endpoint allows you to get a list of reference entities. Reference entities are paginated.

    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str

    """
    return web.Response(status=200)


async def get_reference_entities_code(request: web.Request, code) -> web.Response:
    """Get a reference entity

    This endpoint allows you to get the information about a given reference entity.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_reference_entity_code(request: web.Request, code, body) -> web.Response:
    """Update/create a reference entity

    This endpoint allows you to update a given reference entity. Note that if the reference entity does not already exist, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchReferenceEntityCodeRequest.from_dict(body)
    return web.Response(status=200)
