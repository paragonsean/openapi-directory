from typing import List, Dict
from aiohttp import web

from openapi_server.models.blob_service_items import BlobServiceItems
from openapi_server.models.blob_service_properties import BlobServiceProperties
from openapi_server import util


async def blob_services_get_service_properties(request: web.Request, resource_group_name, account_name, api_version, subscription_id, blob_services_name) -> web.Response:
    """blob_services_get_service_properties

    Gets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param blob_services_name: The name of the blob Service within the specified storage account. Blob Service Name must be &#39;default&#39;
    :type blob_services_name: str

    """
    return web.Response(status=200)


async def blob_services_list(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """blob_services_list

    List blob services of storage account. It returns a collection of one object named default.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def blob_services_set_service_properties(request: web.Request, resource_group_name, account_name, api_version, subscription_id, blob_services_name, parameters) -> web.Response:
    """blob_services_set_service_properties

    Sets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules. 

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param blob_services_name: The name of the blob Service within the specified storage account. Blob Service Name must be &#39;default&#39;
    :type blob_services_name: str
    :param parameters: The properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.
    :type parameters: dict | bytes

    """
    parameters = BlobServiceProperties.from_dict(parameters)
    return web.Response(status=200)
