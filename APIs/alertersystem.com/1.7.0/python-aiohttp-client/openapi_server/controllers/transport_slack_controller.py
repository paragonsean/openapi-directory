from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_slack_get_collection200_response import ApiTransportSlackGetCollection200Response
from openapi_server.models.transport_slack_get import TransportSlackGet
from openapi_server.models.transport_slack_jsonld_get import TransportSlackJsonldGet
from openapi_server.models.transport_slack_jsonld_post import TransportSlackJsonldPost
from openapi_server.models.transport_slack_jsonld_put import TransportSlackJsonldPut
from openapi_server.models.transport_slack_patch import TransportSlackPatch
from openapi_server.models.transport_slack_post import TransportSlackPost
from openapi_server.models.transport_slack_put import TransportSlackPut
from openapi_server import util


async def api_transport_slack_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSlack resources.

    Retrieves the collection of TransportSlack resources.

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


async def api_transport_slack_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSlack resource.

    Removes the TransportSlack resource.

    :param id: TransportSlack identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_slack_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSlack resource.

    Retrieves a TransportSlack resource.

    :param id: TransportSlack identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_slack_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSlack resource.

    Updates the TransportSlack resource.

    :param id: TransportSlack identifier
    :type id: str
    :param body: The updated TransportSlack resource
    :type body: dict | bytes

    """
    body = TransportSlackPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_slack_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSlack resource.

    Replaces the TransportSlack resource.

    :param id: TransportSlack identifier
    :type id: str
    :param body: The updated TransportSlack resource
    :type body: dict | bytes

    """
    body = TransportSlackPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_slack_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSlack resource.

    Creates a TransportSlack resource.

    :param body: The new TransportSlack resource
    :type body: dict | bytes

    """
    body = TransportSlackPost.from_dict(body)
    return web.Response(status=200)
