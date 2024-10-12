from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.channel_list import ChannelList
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def channels_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, channel_name, api_version, channel) -> web.Response:
    """Create or Update the EngagementFabric channel

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param channel_name: Channel Name
    :type channel_name: str
    :param api_version: API version
    :type api_version: str
    :param channel: The EngagementFabric channel description
    :type channel: dict | bytes

    """
    channel = Channel.from_dict(channel)
    return web.Response(status=200)


async def channels_delete(request: web.Request, subscription_id, resource_group_name, account_name, channel_name, api_version) -> web.Response:
    """Delete the EngagementFabric channel

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param channel_name: The EngagementFabric channel name
    :type channel_name: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)


async def channels_get(request: web.Request, subscription_id, resource_group_name, account_name, channel_name, api_version) -> web.Response:
    """Get the EngagementFabric channel

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param channel_name: Channel Name
    :type channel_name: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)


async def channels_list_by_account(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """List the EngagementFabric channels

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)
