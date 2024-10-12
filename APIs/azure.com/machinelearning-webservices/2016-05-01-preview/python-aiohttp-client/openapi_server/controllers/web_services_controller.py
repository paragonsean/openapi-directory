from typing import List, Dict
from aiohttp import web

from openapi_server.models.paginated_web_services_list import PaginatedWebServicesList
from openapi_server.models.web_service import WebService
from openapi_server.models.web_service_keys import WebServiceKeys
from openapi_server import util


async def web_services_create_or_update(request: web.Request, resource_group_name, web_service_name, api_version, subscription_id, create_or_update_payload) -> web.Response:
    """web_services_create_or_update

    Create or update a web service. This call will overwrite an existing web service. Note that there is no warning or confirmation. This is a nonrecoverable operation. If your intent is to create a new web service, call the Get operation first to verify that it does not exist.

    :param resource_group_name: Name of the resource group in which the web service is located.
    :type resource_group_name: str
    :param web_service_name: The name of the web service.
    :type web_service_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param create_or_update_payload: The payload that is used to create or update the web service.
    :type create_or_update_payload: dict | bytes

    """
    create_or_update_payload = WebService.from_dict(create_or_update_payload)
    return web.Response(status=200)


async def web_services_get(request: web.Request, resource_group_name, web_service_name, api_version, subscription_id) -> web.Response:
    """web_services_get

    Gets the Web Service Definition as specified by a subscription, resource group, and name. Note that the storage credentials and web service keys are not returned by this call. To get the web service access keys, call List Keys.

    :param resource_group_name: Name of the resource group in which the web service is located.
    :type resource_group_name: str
    :param web_service_name: The name of the web service.
    :type web_service_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def web_services_list(request: web.Request, api_version, subscription_id, skiptoken=None) -> web.Response:
    """web_services_list

    Gets the web services in the specified subscription.

    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def web_services_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, skiptoken=None) -> web.Response:
    """web_services_list_by_resource_group

    Gets the web services in the specified resource group.

    :param resource_group_name: Name of the resource group in which the web service is located.
    :type resource_group_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def web_services_list_keys(request: web.Request, resource_group_name, web_service_name, api_version, subscription_id) -> web.Response:
    """web_services_list_keys

    Gets the access keys for the specified web service.

    :param resource_group_name: Name of the resource group in which the web service is located.
    :type resource_group_name: str
    :param web_service_name: The name of the web service.
    :type web_service_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def web_services_patch(request: web.Request, resource_group_name, web_service_name, api_version, subscription_id, patch_payload) -> web.Response:
    """web_services_patch

    Modifies an existing web service resource. The PATCH API call is an asynchronous operation. To determine whether it has completed successfully, you must perform a Get operation.

    :param resource_group_name: Name of the resource group in which the web service is located.
    :type resource_group_name: str
    :param web_service_name: The name of the web service.
    :type web_service_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param patch_payload: The payload to use to patch the web service.
    :type patch_payload: dict | bytes

    """
    patch_payload = WebService.from_dict(patch_payload)
    return web.Response(status=200)


async def web_services_remove(request: web.Request, resource_group_name, web_service_name, api_version, subscription_id) -> web.Response:
    """web_services_remove

    Deletes the specified web service.

    :param resource_group_name: Name of the resource group in which the web service is located.
    :type resource_group_name: str
    :param web_service_name: The name of the web service.
    :type web_service_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)
