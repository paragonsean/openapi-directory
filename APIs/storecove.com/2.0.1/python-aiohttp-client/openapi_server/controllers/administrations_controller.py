from typing import List, Dict
from aiohttp import web

from openapi_server.models.administration import Administration
from openapi_server.models.administration_create import AdministrationCreate
from openapi_server.models.administration_update import AdministrationUpdate
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def create_administration(request: web.Request, legal_entity_id, body) -> web.Response:
    """Create a new Administration

    Deprecated. Create a new Administration. An Administration is an email destination for purchase invoices.

    :param legal_entity_id: The id of the LegalEntity for which to create the Administration
    :type legal_entity_id: int
    :param body: Administration to create
    :type body: dict | bytes

    """
    body = AdministrationCreate.from_dict(body)
    return web.Response(status=200)


async def delete_administration(request: web.Request, legal_entity_id, id) -> web.Response:
    """Delete Administration

    Deprecated. Delete an Administration

    :param legal_entity_id: The id of the LegalEntity the Administration belongs to
    :type legal_entity_id: int
    :param id: The id of the Administration
    :type id: int

    """
    return web.Response(status=200)


async def get_administration(request: web.Request, legal_entity_id, id) -> web.Response:
    """Get Administration

    Deprecated. Get an Administration

    :param legal_entity_id: The id of the LegalEntity the Administration belongs to
    :type legal_entity_id: int
    :param id: The id of the Administration
    :type id: int

    """
    return web.Response(status=200)


async def update_administration(request: web.Request, legal_entity_id, id, body) -> web.Response:
    """Update Administration

    Deprecated. Update an Administration

    :param legal_entity_id: The id of the LegalEntity the Administration belongs to
    :type legal_entity_id: int
    :param id: The id of the Administration to be updated
    :type id: int
    :param body: Administration to update
    :type body: dict | bytes

    """
    body = AdministrationUpdate.from_dict(body)
    return web.Response(status=200)
