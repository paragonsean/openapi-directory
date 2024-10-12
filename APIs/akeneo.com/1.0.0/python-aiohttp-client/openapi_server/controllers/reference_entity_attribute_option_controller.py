from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_reference_entity_attributes_attribute_code_options200_response_inner import GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_reference_entity_attributes_attribute_code_options(request: web.Request, reference_entity_code, attribute_code) -> web.Response:
    """Get a list of attribute options of a given attribute for a given reference entity

    This endpoint allows you to get a list of attribute options for a given reference entity.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param attribute_code: Code of the attribute
    :type attribute_code: str

    """
    return web.Response(status=200)


async def get_reference_entity_attributes_attribute_code_options_code(request: web.Request, reference_entity_code, attribute_code, code) -> web.Response:
    """Get an attribute option for a given attribute of a given reference entity

    This endpoint allows you to get the information about a given attribute option.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_reference_entity_attributes_attribute_code_options_code(request: web.Request, reference_entity_code, attribute_code, code, body) -> web.Response:
    """Update/create a reference entity attribute option

    This endpoint allows you to update a given option for a given attribute and a given reference entity. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the option does not already exist for the given attribute of the given reference entity, it creates it.

    :param reference_entity_code: Code of the reference entity
    :type reference_entity_code: str
    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner.from_dict(body)
    return web.Response(status=200)
