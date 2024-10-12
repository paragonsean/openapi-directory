from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_trusted_id_provider_parameters import CreateOrUpdateTrustedIdProviderParameters
from openapi_server.models.trusted_id_provider import TrustedIdProvider
from openapi_server.models.trusted_id_provider_list_result import TrustedIdProviderListResult
from openapi_server.models.update_trusted_id_provider_parameters import UpdateTrustedIdProviderParameters
from openapi_server import util


async def trusted_id_providers_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, trusted_id_provider_name, api_version, parameters) -> web.Response:
    """trusted_id_providers_create_or_update

    Creates or updates the specified trusted identity provider. During update, the trusted identity provider with the specified name will be replaced with this new provider

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param trusted_id_provider_name: The name of the trusted identity provider. This is used for differentiation of providers in the account.
    :type trusted_id_provider_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to create or replace the trusted identity provider.
    :type parameters: dict | bytes

    """
    parameters = CreateOrUpdateTrustedIdProviderParameters.from_dict(parameters)
    return web.Response(status=200)


async def trusted_id_providers_delete(request: web.Request, subscription_id, resource_group_name, account_name, trusted_id_provider_name, api_version) -> web.Response:
    """trusted_id_providers_delete

    Deletes the specified trusted identity provider from the specified Data Lake Store account

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param trusted_id_provider_name: The name of the trusted identity provider to delete.
    :type trusted_id_provider_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def trusted_id_providers_get(request: web.Request, subscription_id, resource_group_name, account_name, trusted_id_provider_name, api_version) -> web.Response:
    """trusted_id_providers_get

    Gets the specified Data Lake Store trusted identity provider.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param trusted_id_provider_name: The name of the trusted identity provider to retrieve.
    :type trusted_id_provider_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def trusted_id_providers_list_by_account(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """trusted_id_providers_list_by_account

    Lists the Data Lake Store trusted identity providers within the specified Data Lake Store account.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def trusted_id_providers_update(request: web.Request, subscription_id, resource_group_name, account_name, trusted_id_provider_name, api_version, parameters=None) -> web.Response:
    """trusted_id_providers_update

    Updates the specified trusted identity provider.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param trusted_id_provider_name: The name of the trusted identity provider. This is used for differentiation of providers in the account.
    :type trusted_id_provider_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to update the trusted identity provider.
    :type parameters: dict | bytes

    """
    parameters = UpdateTrustedIdProviderParameters.from_dict(parameters)
    return web.Response(status=200)
