from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_webhook_get_collection200_response import ApiTransportWebhookGetCollection200Response
from openapi_server.models.transport_webhook_get import TransportWebhookGet
from openapi_server.models.transport_webhook_jsonld_get import TransportWebhookJsonldGet
from openapi_server.models.transport_webhook_jsonld_post import TransportWebhookJsonldPost
from openapi_server.models.transport_webhook_jsonld_put import TransportWebhookJsonldPut
from openapi_server.models.transport_webhook_patch import TransportWebhookPatch
from openapi_server.models.transport_webhook_post import TransportWebhookPost
from openapi_server.models.transport_webhook_put import TransportWebhookPut
from openapi_server import util


async def api_transport_webhook_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportWebhook resources.

    Retrieves the collection of TransportWebhook resources.

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


async def api_transport_webhook_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportWebhook resource.

    Removes the TransportWebhook resource.

    :param id: TransportWebhook identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_webhook_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportWebhook resource.

    Retrieves a TransportWebhook resource.

    :param id: TransportWebhook identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_webhook_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportWebhook resource.

    Updates the TransportWebhook resource.

    :param id: TransportWebhook identifier
    :type id: str
    :param body: The updated TransportWebhook resource
    :type body: dict | bytes

    """
    body = TransportWebhookPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_webhook_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportWebhook resource.

    Replaces the TransportWebhook resource.

    :param id: TransportWebhook identifier
    :type id: str
    :param body: The updated TransportWebhook resource
    :type body: dict | bytes

    """
    body = TransportWebhookPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_webhook_post(request: web.Request, body) -> web.Response:
    """Creates a TransportWebhook resource.

    Creates a TransportWebhook resource.

    :param body: The new TransportWebhook resource
    :type body: dict | bytes

    """
    body = TransportWebhookPost.from_dict(body)
    return web.Response(status=200)
