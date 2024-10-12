from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def v2do_post_multi_part(request: web.Request, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, file, feed_type=None) -> web.Response:
    """Upload an item feed

    You can upload an item feed. If the feed successfully processed, it returns a feed ID. Use the returned feed ID to retrieve a feed status. You need your Consumer ID and the Private Key to upload an item.

    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param file: Feed File to upload
    :type file: str
    :param feed_type: Feed Type
    :type feed_type: str

    """
    return web.Response(status=200)


async def v2get_all_items_status(request: web.Request, feed_id, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, include_details=None, offset=None, limit=None) -> web.Response:
    """Get status of an item within a feed

    You can display the status of all items within a feed. Use the feed ID returned from the upload an item API.

    :param feed_id: The feed ID
    :type feed_id: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param include_details: Includes details of each entity in the feed. Do not set this parameter to true.
    :type include_details: str
    :param offset: The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true.
    :type offset: str
    :param limit: The number of entities to be returned. It cannot be more than 50 entities. Use it only when the includeDetails is set to true.
    :type limit: str

    """
    return web.Response(status=200)


async def v2get_feed_item_status(request: web.Request, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, feed_id=None, include_details=None, offset=None, limit=None) -> web.Response:
    """Get status of an item feed

    You can display the status of an item within a feed. Use the feed ID returned from the upload an item API.

    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param feed_id: The feed ID.
    :type feed_id: str
    :param include_details: Includes the status details for each item in the feed. Do not set this parameter to true as discrepancies may appear between the header and the item details (the item details may be incorrect). Instead, use the Get a feedItems status.
    :type include_details: str
    :param offset: The object response to start with, where 0 is the first entity that can be requested. It can only be used when includeDetails is set to true.
    :type offset: str
    :param limit: The number of items to be returned. Cannot be more than 50 items. Use it only when the includeDetails is set to true.
    :type limit: str

    """
    return web.Response(status=200)
