from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_reference_entities_code_attributes200_response_inner import GetReferenceEntitiesCodeAttributes200ResponseInner
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_reference_entities_code_attributes(request: web.Request, reference_entity_code) -> web.Response:
    """Get the list of attributes of a given reference entity

    This endpoint allows you to get the list of attributes of a given reference entity.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str

    """
    return web.Response(status=200)


async def get_reference_entity_attributes_code(request: web.Request, reference_entity_code, code) -> web.Response:
    """Get an attribute of a given reference entity

    This endpoint allows you to get the information about a given attribute for a given reference entity.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_reference_entity_attributes_code(request: web.Request, reference_entity_code, code, body) -> web.Response:
    """Update/create an attribute of a given reference entity

    This endpoint allows you to update a given attribute for a given renference entity. Note that if the attribute does not already exist for the given reference entity, it creates it.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetReferenceEntitiesCodeAttributes200ResponseInner.from_dict(body)
    return web.Response(status=200)
