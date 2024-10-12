from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.fields import Fields
from openapi_server.models.model_field import ModelField
from openapi_server import util


async def fetch_all_fields(request: web.Request, x_next_token=None, x_limit=None, field_name=None) -> web.Response:
    """Retrieve list of all Fields the user has access to.

    Retrieve all fields the authenticated user has access to, including fields shared with the authenticated user from other resource owners. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified. A 409 will be returned if the X-Next-Token has expired. When receiving a 409, the client should discard the X-Next-Token, discard all currently persisted fields for the user, and re-fetch fields from /fields/all.

    :param x_next_token: Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    :type x_next_token: str
    :param x_limit: Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    :type x_limit: int
    :param field_name: Optional prefix filter for field name. Must be at least 3 characters.
    :type field_name: str

    """
    return web.Response(status=200)


async def fetch_field_by_id(request: web.Request, field_id) -> web.Response:
    """Retrieve a specific Field by ID

    Retrieve a given **Field** by ID.

    :param field_id: Unique identifier of the Field.
    :type field_id: str
    :type field_id: str

    """
    return web.Response(status=200)


async def fetch_fields(request: web.Request, x_next_token=None, x_limit=None, field_name=None) -> web.Response:
    """Retrieve list of Fields

    Retrieve list of **Fields**. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified.

    :param x_next_token: Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    :type x_next_token: str
    :param x_limit: Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    :type x_limit: int
    :param field_name: Optional prefix filter for field name. Must be at least 3 characters.
    :type field_name: str

    """
    return web.Response(status=200)
