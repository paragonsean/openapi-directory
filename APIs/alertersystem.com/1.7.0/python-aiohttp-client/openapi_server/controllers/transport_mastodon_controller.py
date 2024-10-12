from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_mastodon_get_collection200_response import ApiTransportMastodonGetCollection200Response
from openapi_server.models.transport_mastodon_get import TransportMastodonGet
from openapi_server.models.transport_mastodon_jsonld_get import TransportMastodonJsonldGet
from openapi_server.models.transport_mastodon_jsonld_post import TransportMastodonJsonldPost
from openapi_server.models.transport_mastodon_jsonld_put import TransportMastodonJsonldPut
from openapi_server.models.transport_mastodon_patch import TransportMastodonPatch
from openapi_server.models.transport_mastodon_post import TransportMastodonPost
from openapi_server.models.transport_mastodon_put import TransportMastodonPut
from openapi_server import util


async def api_transport_mastodon_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportMastodon resources.

    Retrieves the collection of TransportMastodon resources.

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


async def api_transport_mastodon_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportMastodon resource.

    Removes the TransportMastodon resource.

    :param id: TransportMastodon identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mastodon_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportMastodon resource.

    Retrieves a TransportMastodon resource.

    :param id: TransportMastodon identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mastodon_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportMastodon resource.

    Updates the TransportMastodon resource.

    :param id: TransportMastodon identifier
    :type id: str
    :param body: The updated TransportMastodon resource
    :type body: dict | bytes

    """
    body = TransportMastodonPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_mastodon_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportMastodon resource.

    Replaces the TransportMastodon resource.

    :param id: TransportMastodon identifier
    :type id: str
    :param body: The updated TransportMastodon resource
    :type body: dict | bytes

    """
    body = TransportMastodonPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_mastodon_post(request: web.Request, body) -> web.Response:
    """Creates a TransportMastodon resource.

    Creates a TransportMastodon resource.

    :param body: The new TransportMastodon resource
    :type body: dict | bytes

    """
    body = TransportMastodonPost.from_dict(body)
    return web.Response(status=200)
