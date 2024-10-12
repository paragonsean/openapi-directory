from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_set_mapping import DataSetMapping
from openapi_server.models.data_set_mapping_list import DataSetMappingList
from openapi_server.models.data_share_error import DataShareError
from openapi_server import util


async def data_set_mappings_create(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, data_set_mapping_name, api_version, data_set_mapping) -> web.Response:
    """Maps a source data set in the source share to a sink data set in the share subscription.  Enables copying the data set from source to destination.

    Create a DataSetMapping 

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the share subscription which will hold the data set sink.
    :type share_subscription_name: str
    :param data_set_mapping_name: The name of the data set mapping to be created.
    :type data_set_mapping_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param data_set_mapping: Destination data set configuration details.
    :type data_set_mapping: dict | bytes

    """
    data_set_mapping = DataSetMapping.from_dict(data_set_mapping)
    return web.Response(status=200)


async def data_set_mappings_delete(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, data_set_mapping_name, api_version) -> web.Response:
    """Delete DataSetMapping in a shareSubscription.

    Delete a DataSetMapping in a shareSubscription

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param data_set_mapping_name: The name of the dataSetMapping.
    :type data_set_mapping_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_set_mappings_get(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, data_set_mapping_name, api_version) -> web.Response:
    """Get DataSetMapping in a shareSubscription.

    Get a DataSetMapping in a shareSubscription

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param data_set_mapping_name: The name of the dataSetMapping.
    :type data_set_mapping_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_set_mappings_list_by_share_subscription(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, skip_token=None) -> web.Response:
    """List DataSetMappings in a share subscription.

    List DataSetMappings in a share subscription

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the share subscription.
    :type share_subscription_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: Continuation token
    :type skip_token: str

    """
    return web.Response(status=200)
