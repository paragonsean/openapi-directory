from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.external_subscription_definition import ExternalSubscriptionDefinition
from openapi_server.models.external_subscription_definition_list_result import ExternalSubscriptionDefinitionListResult
from openapi_server import util


async def external_subscription_get(request: web.Request, api_version, external_subscription_name, expand=None) -> web.Response:
    """external_subscription_get

    Get an ExternalSubscription definition

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param external_subscription_name: External Subscription Name. (eg &#39;aws-{UsageAccountId}&#39;)
    :type external_subscription_name: str
    :param expand: May be used to expand the collectionInfo property. By default, collectionInfo is not included.
    :type expand: str

    """
    return web.Response(status=200)


async def external_subscription_list(request: web.Request, api_version) -> web.Response:
    """external_subscription_list

    List all ExternalSubscription definitions

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str

    """
    return web.Response(status=200)


async def external_subscription_list_by_external_billing_account(request: web.Request, api_version, external_billing_account_name) -> web.Response:
    """external_subscription_list_by_external_billing_account

    List all ExternalSubscriptions by ExternalBillingAccount definitions

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param external_billing_account_name: External Billing Account Name. (eg &#39;aws-{PayerAccountId}&#39;)
    :type external_billing_account_name: str

    """
    return web.Response(status=200)


async def external_subscription_list_by_management_group(request: web.Request, api_version, management_group_id, recurse=None) -> web.Response:
    """external_subscription_list_by_management_group

    List all ExternalSubscription definitions for Management Group

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param management_group_id: ManagementGroup ID
    :type management_group_id: str
    :param recurse: The $recurse&#x3D;true query string parameter allows returning externalSubscriptions associated with the specified managementGroup, or any of its descendants.
    :type recurse: bool

    """
    return web.Response(status=200)


async def external_subscription_update_management_group(request: web.Request, api_version, management_group_id, external_subscription_name) -> web.Response:
    """external_subscription_update_management_group

    Updates the management group of an ExternalSubscription

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param management_group_id: ManagementGroup ID
    :type management_group_id: str
    :param external_subscription_name: External Subscription Name. (eg &#39;aws-{UsageAccountId}&#39;)
    :type external_subscription_name: str

    """
    return web.Response(status=200)
