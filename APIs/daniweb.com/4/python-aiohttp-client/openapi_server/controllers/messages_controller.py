from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_get_messages_id import EndpointGetMessagesID
from openapi_server.models.endpoint_get_messages_id_metadata import EndpointGetMessagesIDMetadata
from openapi_server.models.endpoint_get_messages_id_metadata_collections import EndpointGetMessagesIDMetadataCollections
from openapi_server.models.endpoint_post_messages_id_metadata import EndpointPostMessagesIDMetadata
from openapi_server.models.endpoint_post_messages_metadata_filters import EndpointPostMessagesMetadataFilters
from openapi_server import util


async def messages_id_metadata_collections_get(request: web.Request, id) -> web.Response:
    """messages_id_metadata_collections_get

    Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def messages_id_metadata_get(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """messages_id_metadata_get

    Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

    :param id: 
    :type id: int
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def messages_id_metadata_post(request: web.Request, id, metadata_0_key=None, metadata_0_privacy=None, metadata_0_values=None, metadata_1_key=None, metadata_1_privacy=None, metadata_1_values=None, metadata_2_key=None, metadata_2_privacy=None, metadata_2_values=None) -> web.Response:
    """messages_id_metadata_post

    Attach one-to-many key/value pairs of metadata to a message, so long as the user who authored the message exists within the current access token&#39;s bubble. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by you or the other user in the message&#39;s conversation, using an access token which grants you access to the user who authored the message, if it wasn&#39;t you; Bubbled metadata by you or the other user in the message&#39;s conversation, using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message, if it wasn&#39;t you; Private metadata by you, so long as you are using an access token existing within the current bubble.

    :param id: 
    :type id: int
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_privacy: 
    :type metadata_0_privacy: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_privacy: 
    :type metadata_1_privacy: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_privacy: 
    :type metadata_2_privacy: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]

    """
    return web.Response(status=200)


async def messages_idget(request: web.Request, id) -> web.Response:
    """messages_idget

    Fetch an array of messages. You can only retrieve messages authored by you or by users who exist within the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def messages_metadata_filters_post(request: web.Request, limit=None, metadata_0_key=None, metadata_0_values=None, metadata_1_key=None, metadata_1_values=None, metadata_2_key=None, metadata_2_values=None, offset=None) -> web.Response:
    """messages_metadata_filters_post

    Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

    :param limit: 
    :type limit: int
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)
