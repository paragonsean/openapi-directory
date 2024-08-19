from typing import List, Dict
from aiohttp import web

from openapi_server.models.legal_entity import LegalEntity
from openapi_server.models.legal_entity_info import LegalEntityInfo
from openapi_server.models.legal_entity_info_required_type import LegalEntityInfoRequiredType
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def get_legal_entities_id(request: web.Request, id) -> web.Response:
    """Get a legal entity

    Returns a legal entity.

    :param id: The unique identifier of the legal entity.
    :type id: str

    """
    return web.Response(status=200)


async def patch_legal_entities_id(request: web.Request, id, body=None) -> web.Response:
    """Update a legal entity

    Updates a legal entity.   &gt;To change the legal entity type, include only the new &#x60;type&#x60; in your request. To update the &#x60;entityAssociations&#x60; array, you need to replace the entire array. For example, if the array has 3 entries and you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

    :param id: The unique identifier of the legal entity.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LegalEntityInfo.from_dict(body)
    return web.Response(status=200)


async def post_legal_entities(request: web.Request, body=None) -> web.Response:
    """Create a legal entity

    Creates a legal entity.   This resource contains information about the user that will be onboarded in your platform. Adyen uses this information to perform verification checks as required by payment industry regulations. Adyen informs you of the verification results through webhooks or API responses.   

    :param body: 
    :type body: dict | bytes

    """
    body = LegalEntityInfoRequiredType.from_dict(body)
    return web.Response(status=200)
