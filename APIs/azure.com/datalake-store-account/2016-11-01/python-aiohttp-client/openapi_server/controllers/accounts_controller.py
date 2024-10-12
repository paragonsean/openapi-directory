from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.create_data_lake_store_account_parameters import CreateDataLakeStoreAccountParameters
from openapi_server.models.data_lake_store_account import DataLakeStoreAccount
from openapi_server.models.data_lake_store_account_list_result import DataLakeStoreAccountListResult
from openapi_server.models.name_availability_information import NameAvailabilityInformation
from openapi_server.models.update_data_lake_store_account_parameters import UpdateDataLakeStoreAccountParameters
from openapi_server import util


async def accounts_check_name_availability(request: web.Request, subscription_id, location, api_version, parameters) -> web.Response:
    """accounts_check_name_availability

    Checks whether the specified account name is available or taken.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The resource location without whitespace.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to check the Data Lake Store account name availability.
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailabilityParameters.from_dict(parameters)
    return web.Response(status=200)


async def accounts_create(request: web.Request, subscription_id, resource_group_name, account_name, api_version, parameters) -> web.Response:
    """accounts_create

    Creates the specified Data Lake Store account.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to create the Data Lake Store account.
    :type parameters: dict | bytes

    """
    parameters = CreateDataLakeStoreAccountParameters.from_dict(parameters)
    return web.Response(status=200)


async def accounts_delete(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """accounts_delete

    Deletes the specified Data Lake Store account.

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


async def accounts_enable_key_vault(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """accounts_enable_key_vault

    Attempts to enable a user managed Key Vault for encryption of the specified Data Lake Store account.

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


async def accounts_get(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """accounts_get

    Gets the specified Data Lake Store account.

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


async def accounts_list(request: web.Request, subscription_id, api_version, filter=None, top=None, skip=None, select=None, orderby=None, count=None) -> web.Response:
    """accounts_list

    Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def accounts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, filter=None, top=None, skip=None, select=None, orderby=None, count=None) -> web.Response:
    """accounts_list_by_resource_group

    Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: A Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)


async def accounts_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, parameters) -> web.Response:
    """accounts_update

    Updates the specified Data Lake Store account information.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to update the Data Lake Store account.
    :type parameters: dict | bytes

    """
    parameters = UpdateDataLakeStoreAccountParameters.from_dict(parameters)
    return web.Response(status=200)
