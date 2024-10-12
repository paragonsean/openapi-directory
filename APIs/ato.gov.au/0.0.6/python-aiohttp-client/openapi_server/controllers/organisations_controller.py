from typing import List, Dict
from aiohttp import web

from openapi_server.models.failed_precondition import FailedPrecondition
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.organisation import Organisation
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def organisations_get(request: web.Request, api_key, registered_identifier=None, identifier=None) -> web.Response:
    """Retrieve a list of organisations

    Retrieve a list of organisations 

    :param api_key: The API key.
    :type api_key: str
    :param registered_identifier: The registered identifier, for example, &#x60;ACN&#x60; or &#x60;ABN&#x60;.
    :type registered_identifier: str
    :param identifier: The identifier, for example, &#x60;123456789&#x60;.
    :type identifier: str

    """
    return web.Response(status=200)


async def organisations_party_id_delete(request: web.Request, api_key, party_id) -> web.Response:
    """Delete an organisation

    Delete an organisation with the specified identifier 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str

    """
    return web.Response(status=200)


async def organisations_party_id_get(request: web.Request, api_key, party_id) -> web.Response:
    """Retrieve an organisation

    Retrieve an organisation with the specified identifier 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str

    """
    return web.Response(status=200)


async def organisations_party_id_put(request: web.Request, api_key, party_id, body) -> web.Response:
    """Update an organisation

    Update an organisation 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param body: Organisation resource
    :type body: dict | bytes

    """
    body = Organisation.from_dict(body)
    return web.Response(status=200)


async def organisations_post(request: web.Request, api_key, body) -> web.Response:
    """Create an organisation

    Create an organisation 

    :param api_key: The API key.
    :type api_key: str
    :param body: Organisation resource
    :type body: dict | bytes

    """
    body = Organisation.from_dict(body)
    return web.Response(status=200)
