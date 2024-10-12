from typing import List, Dict
from aiohttp import web

from openapi_server.models.consumer_source_data_set_list import ConsumerSourceDataSetList
from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_response import OperationResponse
from openapi_server.models.share_subscription import ShareSubscription
from openapi_server.models.share_subscription_list import ShareSubscriptionList
from openapi_server.models.share_subscription_synchronization import ShareSubscriptionSynchronization
from openapi_server.models.share_subscription_synchronization_list import ShareSubscriptionSynchronizationList
from openapi_server.models.source_share_synchronization_setting_list import SourceShareSynchronizationSettingList
from openapi_server.models.synchronization_details_list import SynchronizationDetailsList
from openapi_server.models.synchronize import Synchronize
from openapi_server import util


async def consumer_source_data_sets_list_by_share_subscription(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, skip_token=None) -> web.Response:
    """Get source dataSets of a shareSubscription.

    Get source dataSets of a shareSubscription

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: Continuation token
    :type skip_token: str

    """
    return web.Response(status=200)


async def share_subscriptions_cancel_synchronization(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, share_subscription_synchronization) -> web.Response:
    """Request cancellation of a data share snapshot

    Request to cancel a synchronization.

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param share_subscription_synchronization: Share Subscription Synchronization payload.
    :type share_subscription_synchronization: dict | bytes

    """
    share_subscription_synchronization = ShareSubscriptionSynchronization.from_dict(share_subscription_synchronization)
    return web.Response(status=200)


async def share_subscriptions_create(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, share_subscription) -> web.Response:
    """Create shareSubscription in an account.

    Create a shareSubscription in an account

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param share_subscription: create parameters for shareSubscription
    :type share_subscription: dict | bytes

    """
    share_subscription = ShareSubscription.from_dict(share_subscription)
    return web.Response(status=200)


async def share_subscriptions_delete(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version) -> web.Response:
    """Delete shareSubscription in an account.

    Delete a shareSubscription in an account

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def share_subscriptions_get(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version) -> web.Response:
    """Get shareSubscription in an account.

    Get a shareSubscription in an account

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def share_subscriptions_list_by_account(request: web.Request, subscription_id, resource_group_name, account_name, api_version, skip_token=None) -> web.Response:
    """List of available share subscriptions under an account.

    List share subscriptions in an account

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: Continuation Token
    :type skip_token: str

    """
    return web.Response(status=200)


async def share_subscriptions_list_source_share_synchronization_settings(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, skip_token=None) -> web.Response:
    """Get source share synchronization settings for a shareSubscription.

    Get synchronization settings set on a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of the shareSubscription.
    :type share_subscription_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: Continuation token
    :type skip_token: str

    """
    return web.Response(status=200)


async def share_subscriptions_list_synchronization_details(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, share_subscription_synchronization, skip_token=None) -> web.Response:
    """List data set level details for a share subscription synchronization

    List synchronization details

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
    :param share_subscription_synchronization: Share Subscription Synchronization payload.
    :type share_subscription_synchronization: dict | bytes
    :param skip_token: Continuation token
    :type skip_token: str

    """
    share_subscription_synchronization = ShareSubscriptionSynchronization.from_dict(share_subscription_synchronization)
    return web.Response(status=200)


async def share_subscriptions_list_synchronizations(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, skip_token=None) -> web.Response:
    """List Synchronizations in a share subscription.

    List synchronizations of a share subscription

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


async def share_subscriptions_synchronize(request: web.Request, subscription_id, resource_group_name, account_name, share_subscription_name, api_version, synchronize) -> web.Response:
    """Initiate an asynchronous data share job

    Initiate a copy

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_subscription_name: The name of share subscription
    :type share_subscription_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param synchronize: Synchronize payload
    :type synchronize: dict | bytes

    """
    synchronize = Synchronize.from_dict(synchronize)
    return web.Response(status=200)
