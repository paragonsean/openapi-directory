from typing import List, Dict
from aiohttp import web

from openapi_server.models.model_schema import ModelSchema
from openapi_server import util


async def setup_schema_get(request: web.Request, ) -> web.Response:
    """Returns a list of schemas

    Returns a list of schemas you&#39;ve previously created. The schemas are returned in sorted order, with the most recent schema appearing first.


    """
    return web.Response(status=200)


async def setup_schema_id_delete(request: web.Request, id) -> web.Response:
    """Delete an schema.

    Deletes the specified schema.

    :param id: Schema ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_schema_id_get(request: web.Request, id) -> web.Response:
    """Retrieve an existing schema

    Retrieves the details of an existing schema. You need only supply the unique schema identifier that was returned upon schema creation.

    :param id: Schema ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_schema_post(request: web.Request, ) -> web.Response:
    """Create or update an schema

    Creates or updates the specified schema. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
