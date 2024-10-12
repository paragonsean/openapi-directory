from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def delete_swagger(request: web.Request, id) -> web.Response:
    """delete_swagger

    DEPRECATED. Instead, use https://docs.readme.com/developers/reference/api-specification#deleteapispecification to delete a Swagger file in ReadMe

    :param id: ID of swagger the file
    :type id: str

    """
    return web.Response(status=200)


async def update_swagger(request: web.Request, id, swagger=None) -> web.Response:
    """update_swagger

    DEPRECATED. Instead, use https://docs.readme.com/developers/reference/api-specification#updateapispecification to update a Swagger file.

    :param id: ID of the Swagger file
    :type id: str
    :param swagger: Swagger file
    :type swagger: str

    """
    return web.Response(status=200)


async def upload_swagger(request: web.Request, swagger=None) -> web.Response:
    """upload_swagger

    DEPRECATED. Instead use https://docs.readme.com/developers/reference/api-specification#uploadapispecification to upload a Swagger file to ReadMe

    :param swagger: Swagger file
    :type swagger: str

    """
    return web.Response(status=200)
