from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_type import DataType
from openapi_server import util


async def setup_data_type_get(request: web.Request, ) -> web.Response:
    """Returns a list of data types

    Returns a list of data types you&#39;ve previously created. The data types are returned in sorted order, with the most recent DataType appearing first.


    """
    return web.Response(status=200)


async def setup_data_type_id_delete(request: web.Request, id) -> web.Response:
    """Delete a data type

    Deletes the specified data type.

    :param id: data type ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_data_type_id_get(request: web.Request, id) -> web.Response:
    """Retrieve a data type

    Retrieves the details of an existing data type. You need only supply the unique data  type identifier that was returned upon DataType creation.

    :param id: data type ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_data_type_post(request: web.Request, ) -> web.Response:
    """Create or update a data type

    Creates or updates the specified data type by setting the values of the parameters passed. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
