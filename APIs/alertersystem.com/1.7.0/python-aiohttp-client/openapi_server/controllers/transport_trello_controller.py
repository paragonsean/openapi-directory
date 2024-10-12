from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_trello_get_collection200_response import ApiTransportTrelloGetCollection200Response
from openapi_server.models.transport_trello_get import TransportTrelloGet
from openapi_server.models.transport_trello_jsonld_get import TransportTrelloJsonldGet
from openapi_server.models.transport_trello_jsonld_post import TransportTrelloJsonldPost
from openapi_server.models.transport_trello_jsonld_put import TransportTrelloJsonldPut
from openapi_server.models.transport_trello_patch import TransportTrelloPatch
from openapi_server.models.transport_trello_post import TransportTrelloPost
from openapi_server.models.transport_trello_put import TransportTrelloPut
from openapi_server import util


async def api_transport_trello_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportTrello resources.

    Retrieves the collection of TransportTrello resources.

    :param page: The collection page number
    :type page: int
    :param data_segment_code: 
    :type data_segment_code: str
    :param data_segment_code2: 
    :type data_segment_code2: List[str]
    :param partition: 
    :type partition: str
    :param partition2: 
    :type partition2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_transport_trello_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportTrello resource.

    Removes the TransportTrello resource.

    :param id: TransportTrello identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_trello_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportTrello resource.

    Retrieves a TransportTrello resource.

    :param id: TransportTrello identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_trello_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportTrello resource.

    Updates the TransportTrello resource.

    :param id: TransportTrello identifier
    :type id: str
    :param body: The updated TransportTrello resource
    :type body: dict | bytes

    """
    body = TransportTrelloPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_trello_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportTrello resource.

    Replaces the TransportTrello resource.

    :param id: TransportTrello identifier
    :type id: str
    :param body: The updated TransportTrello resource
    :type body: dict | bytes

    """
    body = TransportTrelloPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_trello_post(request: web.Request, body) -> web.Response:
    """Creates a TransportTrello resource.

    Creates a TransportTrello resource.

    :param body: The new TransportTrello resource
    :type body: dict | bytes

    """
    body = TransportTrelloPost.from_dict(body)
    return web.Response(status=200)
