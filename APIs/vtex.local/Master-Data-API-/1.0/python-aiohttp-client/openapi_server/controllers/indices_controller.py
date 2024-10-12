from typing import List, Dict
from aiohttp import web

from openapi_server.models.putindices_request import PutindicesRequest
from openapi_server import util


async def deleteindexbyname(request: web.Request, data_entity_name, content_type, index_name) -> web.Response:
    """Delete index by name

    Delete an index.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param index_name: Name of the index.
    :type index_name: str

    """
    return web.Response(status=200)


async def getindexbyname(request: web.Request, data_entity_name, content_type, index_name) -> web.Response:
    """Get index by name

    Returns an index.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param index_name: Name of the index.
    :type index_name: str

    """
    return web.Response(status=200)


async def getindices(request: web.Request, data_entity_name, content_type) -> web.Response:
    """Get indices

    Returns the list of indices by data entity.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def putindices(request: web.Request, data_entity_name, body) -> web.Response:
    """Put indices

    Create an index.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param body: Request body for creating an index
    :type body: dict | bytes

    """
    body = PutindicesRequest.from_dict(body)
    return web.Response(status=200)
