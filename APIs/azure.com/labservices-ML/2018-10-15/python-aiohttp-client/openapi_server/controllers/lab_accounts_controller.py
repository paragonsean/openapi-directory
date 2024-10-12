from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.create_lab_properties import CreateLabProperties
from openapi_server.models.get_regional_availability_response import GetRegionalAvailabilityResponse
from openapi_server.models.lab_account import LabAccount
from openapi_server.models.lab_account_fragment import LabAccountFragment
from openapi_server.models.response_with_continuation_lab_account import ResponseWithContinuationLabAccount
from openapi_server import util


async def lab_accounts_create_lab(request: web.Request, subscription_id, resource_group_name, lab_account_name, api_version, create_lab_properties) -> web.Response:
    """lab_accounts_create_lab

    Create a lab in a lab account.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param create_lab_properties: Properties for creating a managed lab and a default environment setting
    :type create_lab_properties: dict | bytes

    """
    create_lab_properties = CreateLabProperties.from_dict(create_lab_properties)
    return web.Response(status=200)


async def lab_accounts_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, api_version, lab_account) -> web.Response:
    """lab_accounts_create_or_update

    Create or replace an existing Lab Account.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_account: Represents a lab account.
    :type lab_account: dict | bytes

    """
    lab_account = LabAccount.from_dict(lab_account)
    return web.Response(status=200)


async def lab_accounts_delete(request: web.Request, subscription_id, resource_group_name, lab_account_name, api_version) -> web.Response:
    """lab_accounts_delete

    Delete lab account. This operation can take a while to complete

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def lab_accounts_get(request: web.Request, subscription_id, resource_group_name, lab_account_name, api_version, expand=None) -> web.Response:
    """lab_accounts_get

    Get lab account

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def lab_accounts_get_regional_availability(request: web.Request, subscription_id, resource_group_name, lab_account_name, api_version) -> web.Response:
    """lab_accounts_get_regional_availability

    Get regional availability information for each size category configured under a lab account

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def lab_accounts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """lab_accounts_list_by_resource_group

    List lab accounts in a resource group.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def lab_accounts_list_by_subscription(request: web.Request, subscription_id, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """lab_accounts_list_by_subscription

    List lab accounts in a subscription.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def lab_accounts_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, api_version, lab_account) -> web.Response:
    """lab_accounts_update

    Modify properties of lab accounts.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_account: Represents a lab account.
    :type lab_account: dict | bytes

    """
    lab_account = LabAccountFragment.from_dict(lab_account)
    return web.Response(status=200)
