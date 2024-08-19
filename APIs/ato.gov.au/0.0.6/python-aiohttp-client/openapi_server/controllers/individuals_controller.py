from typing import List, Dict
from aiohttp import web

from openapi_server.models.failed_precondition import FailedPrecondition
from openapi_server.models.individual import Individual
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def individuals_get(request: web.Request, api_key, date_of_birth=None, place_of_birth=None) -> web.Response:
    """Retrieve a list of individuals

    Retrieve a list of individuals 

    :param api_key: The API key.
    :type api_key: str
    :param date_of_birth: The individual&#39;s date of birth, for example, &#x60;1979-01-13&#x60; (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format).
    :type date_of_birth: str
    :param place_of_birth: The individual&#39;s place of birth, for example, &#x60;Tamworth&#x60;.
    :type place_of_birth: str

    """
    return web.Response(status=200)


async def individuals_party_id_delete(request: web.Request, api_key, party_id) -> web.Response:
    """Delete an individual

    Delete an individual with the specified identifier 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_get(request: web.Request, api_key, party_id) -> web.Response:
    """Retrieve an individual

    Retrieve an individual with the specified identifier 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_put(request: web.Request, api_key, party_id, body) -> web.Response:
    """Update an individual

    Update an individual 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param body: Individual resource
    :type body: dict | bytes

    """
    body = Individual.from_dict(body)
    return web.Response(status=200)


async def individuals_post(request: web.Request, api_key, body) -> web.Response:
    """Create an individual

    Create an individual 

    :param api_key: The API key.
    :type api_key: str
    :param body: Individual resource
    :type body: dict | bytes

    """
    body = Individual.from_dict(body)
    return web.Response(status=200)
