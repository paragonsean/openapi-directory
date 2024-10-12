from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.create_linked_integration_runtime_request import CreateLinkedIntegrationRuntimeRequest
from openapi_server.models.integration_runtime_list_response import IntegrationRuntimeListResponse
from openapi_server.models.integration_runtime_resource import IntegrationRuntimeResource
from openapi_server.models.integration_runtime_status_response import IntegrationRuntimeStatusResponse
from openapi_server.models.integration_runtimes_get_connection_info200_response import IntegrationRuntimesGetConnectionInfo200Response
from openapi_server.models.integration_runtimes_get_monitoring_data200_response import IntegrationRuntimesGetMonitoringData200Response
from openapi_server.models.integration_runtimes_list_auth_keys200_response import IntegrationRuntimesListAuthKeys200Response
from openapi_server.models.integration_runtimes_regenerate_auth_key_request import IntegrationRuntimesRegenerateAuthKeyRequest
from openapi_server.models.linked_integration_runtime_request import LinkedIntegrationRuntimeRequest
from openapi_server.models.update_integration_runtime_request import UpdateIntegrationRuntimeRequest
from openapi_server import util


async def integration_runtimes_create_linked_integration_runtime(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version, create_linked_integration_runtime_request) -> web.Response:
    """integration_runtimes_create_linked_integration_runtime

    Create a linked integration runtime entry in a shared integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str
    :param create_linked_integration_runtime_request: The linked integration runtime properties.
    :type create_linked_integration_runtime_request: dict | bytes

    """
    create_linked_integration_runtime_request = CreateLinkedIntegrationRuntimeRequest.from_dict(create_linked_integration_runtime_request)
    return web.Response(status=200)


async def integration_runtimes_create_or_update(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version, integration_runtime, if_match=None) -> web.Response:
    """integration_runtimes_create_or_update

    Creates or updates an integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str
    :param integration_runtime: Integration runtime resource definition.
    :type integration_runtime: dict | bytes
    :param if_match: ETag of the integration runtime entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    :type if_match: str

    """
    integration_runtime = IntegrationRuntimeResource.from_dict(integration_runtime)
    return web.Response(status=200)


async def integration_runtimes_delete(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_delete

    Deletes an integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_get(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version, if_none_match=None) -> web.Response:
    """integration_runtimes_get

    Gets an integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str
    :param if_none_match: ETag of the integration runtime entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def integration_runtimes_get_connection_info(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_get_connection_info

    Gets the on-premises integration runtime connection information for encrypting the on-premises data source credentials.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_get_monitoring_data(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_get_monitoring_data

    Get the integration runtime monitoring data, which includes the monitor data for all the nodes under this integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_get_status(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_get_status

    Gets detailed status information for an integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_list_auth_keys(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_list_auth_keys

    Retrieves the authentication keys for an integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_list_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """integration_runtimes_list_by_factory

    Lists integration runtimes.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_regenerate_auth_key(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version, regenerate_key_parameters) -> web.Response:
    """integration_runtimes_regenerate_auth_key

    Regenerates the authentication key for an integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str
    :param regenerate_key_parameters: The parameters for regenerating integration runtime authentication key.
    :type regenerate_key_parameters: dict | bytes

    """
    regenerate_key_parameters = IntegrationRuntimesRegenerateAuthKeyRequest.from_dict(regenerate_key_parameters)
    return web.Response(status=200)


async def integration_runtimes_remove_links(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version, linked_integration_runtime_request) -> web.Response:
    """integration_runtimes_remove_links

    Remove all linked integration runtimes under specific data factory in a self-hosted integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str
    :param linked_integration_runtime_request: The data factory name for the linked integration runtime.
    :type linked_integration_runtime_request: dict | bytes

    """
    linked_integration_runtime_request = LinkedIntegrationRuntimeRequest.from_dict(linked_integration_runtime_request)
    return web.Response(status=200)


async def integration_runtimes_start(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_start

    Starts a ManagedReserved type integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_stop(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_stop

    Stops a ManagedReserved type integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_sync_credentials(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_sync_credentials

    Force the integration runtime to synchronize credentials across integration runtime nodes, and this will override the credentials across all worker nodes with those available on the dispatcher node. If you already have the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime node than using this API directly.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtimes_update(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version, update_integration_runtime_request) -> web.Response:
    """integration_runtimes_update

    Updates an integration runtime.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str
    :param update_integration_runtime_request: The parameters for updating an integration runtime.
    :type update_integration_runtime_request: dict | bytes

    """
    update_integration_runtime_request = UpdateIntegrationRuntimeRequest.from_dict(update_integration_runtime_request)
    return web.Response(status=200)


async def integration_runtimes_upgrade(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtimes_upgrade

    Upgrade self-hosted integration runtime to latest version if availability.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
