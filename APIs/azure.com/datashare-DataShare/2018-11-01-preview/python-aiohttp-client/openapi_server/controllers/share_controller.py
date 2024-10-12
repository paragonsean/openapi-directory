from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_response import OperationResponse
from openapi_server.models.provider_share_subscription import ProviderShareSubscription
from openapi_server.models.provider_share_subscription_list import ProviderShareSubscriptionList
from openapi_server.models.share import Share
from openapi_server.models.share_list import ShareList
from openapi_server.models.share_synchronization import ShareSynchronization
from openapi_server.models.share_synchronization_list import ShareSynchronizationList
from openapi_server.models.synchronization_details_list import SynchronizationDetailsList
from openapi_server import util


async def provider_share_subscriptions_get_by_share(request: web.Request, subscription_id, resource_group_name, account_name, share_name, provider_share_subscription_id, api_version) -> web.Response:
    """Get share subscription in a provider share.

    Get share subscription in a provider share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param provider_share_subscription_id: To locate shareSubscription
    :type provider_share_subscription_id: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def provider_share_subscriptions_list_by_share(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version, skip_token=None) -> web.Response:
    """List of available share subscriptions to a provider share.

    List share subscriptions in a provider share

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
    :param skip_token: Continuation Token
    :type skip_token: str

    """
    return web.Response(status=200)


async def provider_share_subscriptions_reinstate(request: web.Request, subscription_id, resource_group_name, account_name, share_name, provider_share_subscription_id, api_version) -> web.Response:
    """Reinstate share subscription in a provider share.

    Reinstate share subscription in a provider share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param provider_share_subscription_id: To locate shareSubscription
    :type provider_share_subscription_id: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def provider_share_subscriptions_revoke(request: web.Request, subscription_id, resource_group_name, account_name, share_name, provider_share_subscription_id, api_version) -> web.Response:
    """Revoke share subscription in a provider share.

    Revoke share subscription in a provider share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param provider_share_subscription_id: To locate shareSubscription
    :type provider_share_subscription_id: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def shares_create(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version, share) -> web.Response:
    """Create a share in the given account.

    Create a share 

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
    :param share: The share payload
    :type share: dict | bytes

    """
    share = Share.from_dict(share)
    return web.Response(status=200)


async def shares_delete(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version) -> web.Response:
    """Deletes a share

    Delete a share 

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

    """
    return web.Response(status=200)


async def shares_get(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version) -> web.Response:
    """Get a specified share

    Get a share 

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share to retrieve.
    :type share_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def shares_list_by_account(request: web.Request, subscription_id, resource_group_name, account_name, api_version, skip_token=None) -> web.Response:
    """List of available shares under an account.

    List shares in an account

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


async def shares_list_synchronization_details(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version, share_synchronization, skip_token=None) -> web.Response:
    """List data set level details for a share synchronization

    List synchronization details

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
    :param share_synchronization: Share Synchronization payload.
    :type share_synchronization: dict | bytes
    :param skip_token: Continuation token
    :type skip_token: str

    """
    share_synchronization = ShareSynchronization.from_dict(share_synchronization)
    return web.Response(status=200)


async def shares_list_synchronizations(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version, skip_token=None) -> web.Response:
    """List Synchronizations in a share

    List synchronizations of a share

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
    :param skip_token: Continuation token
    :type skip_token: str

    """
    return web.Response(status=200)
