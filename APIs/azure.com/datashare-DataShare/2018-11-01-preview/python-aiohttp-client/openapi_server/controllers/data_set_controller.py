from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_set import DataSet
from openapi_server.models.data_set_list import DataSetList
from openapi_server.models.data_share_error import DataShareError
from openapi_server import util


async def data_sets_create(request: web.Request, subscription_id, resource_group_name, account_name, share_name, data_set_name, api_version, data_set) -> web.Response:
    """Adds a new data set to an existing share or updates it if existing.

    Create a DataSet 

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share to add the data set to.
    :type share_name: str
    :param data_set_name: The name of the dataSet.
    :type data_set_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param data_set: The new data set information.
    :type data_set: dict | bytes

    """
    data_set = DataSet.from_dict(data_set)
    return web.Response(status=200)


async def data_sets_delete(request: web.Request, subscription_id, resource_group_name, account_name, share_name, data_set_name, api_version) -> web.Response:
    """Delete DataSet in a share.

    Delete a DataSet in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param data_set_name: The name of the dataSet.
    :type data_set_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_sets_get(request: web.Request, subscription_id, resource_group_name, account_name, share_name, data_set_name, api_version) -> web.Response:
    """Get DataSet in a share.

    Get a DataSet in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param data_set_name: The name of the dataSet.
    :type data_set_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_sets_list_by_share(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version, skip_token=None) -> web.Response:
    """List DataSets in a share.

    List DataSets in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: continuation token
    :type skip_token: str

    """
    return web.Response(status=200)
