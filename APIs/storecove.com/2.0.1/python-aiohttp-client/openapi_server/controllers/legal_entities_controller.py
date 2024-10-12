from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.legal_entity import LegalEntity
from openapi_server.models.legal_entity_create import LegalEntityCreate
from openapi_server.models.legal_entity_update import LegalEntityUpdate
from openapi_server import util


async def create_legal_entity(request: web.Request, body) -> web.Response:
    """Create a new LegalEntity

    Create a new LegalEntity.

    :param body: LegalEntity to create
    :type body: dict | bytes

    """
    body = LegalEntityCreate.from_dict(body)
    return web.Response(status=200)


async def delete_legal_entity(request: web.Request, id) -> web.Response:
    """Delete LegalEntity

    Delete a specific LegalEntity.

    :param id: legal_entity id
    :type id: int

    """
    return web.Response(status=200)


async def get_legal_entity(request: web.Request, id) -> web.Response:
    """Get LegalEntity

    Get a specific LegalEntity.

    :param id: legal_entity id
    :type id: int

    """
    return web.Response(status=200)


async def update_legal_entity(request: web.Request, id, body) -> web.Response:
    """Update LegalEntity

    Update a specific LegalEntity.

    :param id: legal_entity id
    :type id: int
    :param body: LegalEntity updates
    :type body: dict | bytes

    """
    body = LegalEntityUpdate.from_dict(body)
    return web.Response(status=200)
