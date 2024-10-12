from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_response import OperationResponse
from openapi_server.models.trigger import Trigger
from openapi_server.models.trigger_list import TriggerList
from openapi_server import util


async def triggers_create(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, trigger_name, api_version, trigger) -> web.Response:
    """This method creates a trigger for a share subscription

    Create a Trigger 

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the share subscription which will hold the data set sink.
    :type share_subscription_name: str
    :param trigger_name: The name of the trigger.
    :type trigger_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param trigger: Trigger details.
    :type trigger: dict | bytes

    """
    trigger = Trigger.from_dict(trigger)
    return web.Response(status=200)


async def triggers_delete(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, trigger_name, api_version) -> web.Response:
    """Delete Trigger in a shareSubscription.

    Delete a Trigger in a shareSubscription

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param trigger_name: The name of the trigger.
    :type trigger_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def triggers_get(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, trigger_name, api_version) -> web.Response:
    """Get Trigger in a shareSubscription.

    Get a Trigger in a shareSubscription

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param trigger_name: The name of the trigger.
    :type trigger_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def triggers_list_by_share_subscription(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, skip_token=None) -> web.Response:
    """List Triggers in a share subscription.

    List Triggers in a share subscription

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
