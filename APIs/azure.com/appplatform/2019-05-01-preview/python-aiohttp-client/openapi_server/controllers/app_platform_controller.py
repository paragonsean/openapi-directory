from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_resource import AppResource
from openapi_server.models.app_resource_collection import AppResourceCollection
from openapi_server.models.available_operations import AvailableOperations
from openapi_server.models.binding_resource import BindingResource
from openapi_server.models.binding_resource_collection import BindingResourceCollection
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment_resource import DeploymentResource
from openapi_server.models.deployment_resource_collection import DeploymentResourceCollection
from openapi_server.models.log_file_url_response import LogFileUrlResponse
from openapi_server.models.name_availability import NameAvailability
from openapi_server.models.name_availability_parameters import NameAvailabilityParameters
from openapi_server.models.regenerate_test_key_request_payload import RegenerateTestKeyRequestPayload
from openapi_server.models.resource_upload_definition import ResourceUploadDefinition
from openapi_server.models.service_resource import ServiceResource
from openapi_server.models.service_resource_list import ServiceResourceList
from openapi_server.models.test_keys import TestKeys
from openapi_server import util


async def apps_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, app_resource) -> web.Response:
    """apps_create_or_update

    Create a new App or update an exiting App.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param app_resource: Parameters for the create or update operation
    :type app_resource: dict | bytes

    """
    app_resource = AppResource.from_dict(app_resource)
    return web.Response(status=200)


async def apps_delete(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name) -> web.Response:
    """apps_delete

    Operation to delete an App.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str

    """
    return web.Response(status=200)


async def apps_get(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, sync_status=None) -> web.Response:
    """apps_get

    Get an App and its properties.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param sync_status: Indicates whether sync status
    :type sync_status: str

    """
    return web.Response(status=200)


async def apps_get_resource_upload_url(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name) -> web.Response:
    """apps_get_resource_upload_url

    Get an resource upload URL for an App, which may be artifacts or source archive.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str

    """
    return web.Response(status=200)


async def apps_list(request: web.Request, api_version, subscription_id, resource_group_name, service_name) -> web.Response:
    """apps_list

    Handles requests to list all resources in a Service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str

    """
    return web.Response(status=200)


async def apps_update(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, app_resource) -> web.Response:
    """apps_update

    Operation to update an exiting App.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param app_resource: Parameters for the update operation
    :type app_resource: dict | bytes

    """
    app_resource = AppResource.from_dict(app_resource)
    return web.Response(status=200)


async def bindings_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, binding_name, binding_resource) -> web.Response:
    """bindings_create_or_update

    Create a new Binding or update an exiting Binding.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param binding_name: The name of the Binding resource.
    :type binding_name: str
    :param binding_resource: Parameters for the create or update operation
    :type binding_resource: dict | bytes

    """
    binding_resource = BindingResource.from_dict(binding_resource)
    return web.Response(status=200)


async def bindings_delete(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, binding_name) -> web.Response:
    """bindings_delete

    Operation to delete a Binding.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param binding_name: The name of the Binding resource.
    :type binding_name: str

    """
    return web.Response(status=200)


async def bindings_get(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, binding_name) -> web.Response:
    """bindings_get

    Get a Binding and its properties.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param binding_name: The name of the Binding resource.
    :type binding_name: str

    """
    return web.Response(status=200)


async def bindings_list(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name) -> web.Response:
    """bindings_list

    Handles requests to list all resources in an App.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str

    """
    return web.Response(status=200)


async def bindings_update(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, binding_name, binding_resource) -> web.Response:
    """bindings_update

    Operation to update an exiting Binding.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param binding_name: The name of the Binding resource.
    :type binding_name: str
    :param binding_resource: Parameters for the update operation
    :type binding_resource: dict | bytes

    """
    binding_resource = BindingResource.from_dict(binding_resource)
    return web.Response(status=200)


async def deployments_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, deployment_name, deployment_resource) -> web.Response:
    """deployments_create_or_update

    Create a new Deployment or update an exiting Deployment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param deployment_name: The name of the Deployment resource.
    :type deployment_name: str
    :param deployment_resource: Parameters for the create or update operation
    :type deployment_resource: dict | bytes

    """
    deployment_resource = DeploymentResource.from_dict(deployment_resource)
    return web.Response(status=200)


async def deployments_delete(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, deployment_name) -> web.Response:
    """deployments_delete

    Operation to delete a Deployment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param deployment_name: The name of the Deployment resource.
    :type deployment_name: str

    """
    return web.Response(status=200)


async def deployments_get(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, deployment_name) -> web.Response:
    """deployments_get

    Get a Deployment and its properties.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param deployment_name: The name of the Deployment resource.
    :type deployment_name: str

    """
    return web.Response(status=200)


async def deployments_get_log_file_url(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, deployment_name) -> web.Response:
    """deployments_get_log_file_url

    Get deployment log file URL

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param deployment_name: The name of the Deployment resource.
    :type deployment_name: str

    """
    return web.Response(status=200)


async def deployments_list(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, version=None) -> web.Response:
    """deployments_list

    Handles requests to list all resources in an App.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param version: Version of the deployments to be listed
    :type version: List[str]

    """
    return web.Response(status=200)


async def deployments_list_cluster_all_deployments(request: web.Request, api_version, subscription_id, resource_group_name, service_name, version=None) -> web.Response:
    """deployments_list_cluster_all_deployments

    List deployments for a certain service

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param version: Version of the deployments to be listed
    :type version: List[str]

    """
    return web.Response(status=200)


async def deployments_restart(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, deployment_name) -> web.Response:
    """deployments_restart

    Restart the deployment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param deployment_name: The name of the Deployment resource.
    :type deployment_name: str

    """
    return web.Response(status=200)


async def deployments_start(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, deployment_name) -> web.Response:
    """deployments_start

    Start the deployment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param deployment_name: The name of the Deployment resource.
    :type deployment_name: str

    """
    return web.Response(status=200)


async def deployments_stop(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, deployment_name) -> web.Response:
    """deployments_stop

    Stop the deployment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param deployment_name: The name of the Deployment resource.
    :type deployment_name: str

    """
    return web.Response(status=200)


async def deployments_update(request: web.Request, api_version, subscription_id, resource_group_name, service_name, app_name, deployment_name, deployment_resource) -> web.Response:
    """deployments_update

    Operation to update an exiting Deployment.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param app_name: The name of the App resource.
    :type app_name: str
    :param deployment_name: The name of the Deployment resource.
    :type deployment_name: str
    :param deployment_resource: Parameters for the update operation
    :type deployment_resource: dict | bytes

    """
    deployment_resource = DeploymentResource.from_dict(deployment_resource)
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available REST API operations of the Microsoft.AppPlatform provider.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_check_name_availability(request: web.Request, location, api_version, subscription_id, availability_parameters) -> web.Response:
    """services_check_name_availability

    Checks that the resource name is valid and is not already in use.

    :param location: the region
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param availability_parameters: Parameters supplied to the operation.
    :type availability_parameters: dict | bytes

    """
    availability_parameters = NameAvailabilityParameters.from_dict(availability_parameters)
    return web.Response(status=200)


async def services_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, service_name, resource) -> web.Response:
    """services_create_or_update

    Create a new Service or update an exiting Service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param resource: Parameters for the create or update operation
    :type resource: dict | bytes

    """
    resource = ServiceResource.from_dict(resource)
    return web.Response(status=200)


async def services_delete(request: web.Request, api_version, subscription_id, resource_group_name, service_name) -> web.Response:
    """services_delete

    Operation to delete a Service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str

    """
    return web.Response(status=200)


async def services_disable_test_endpoint(request: web.Request, api_version, subscription_id, resource_group_name, service_name) -> web.Response:
    """services_disable_test_endpoint

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str

    """
    return web.Response(status=200)


async def services_enable_test_endpoint(request: web.Request, api_version, subscription_id, resource_group_name, service_name) -> web.Response:
    """services_enable_test_endpoint

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str

    """
    return web.Response(status=200)


async def services_get(request: web.Request, api_version, subscription_id, resource_group_name, service_name) -> web.Response:
    """services_get

    Get a Service and its properties.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str

    """
    return web.Response(status=200)


async def services_list(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """services_list

    Handles requests to list all resources in a resource group.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def services_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """services_list_by_subscription

    Handles requests to list all resources in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def services_list_test_keys(request: web.Request, api_version, subscription_id, resource_group_name, service_name) -> web.Response:
    """services_list_test_keys

    List test keys for a Service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str

    """
    return web.Response(status=200)


async def services_regenerate_test_key(request: web.Request, api_version, subscription_id, resource_group_name, service_name, regenerate_test_key_request) -> web.Response:
    """services_regenerate_test_key

    Regenerate a test key for a Service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param regenerate_test_key_request: Parameters for the operation
    :type regenerate_test_key_request: dict | bytes

    """
    regenerate_test_key_request = RegenerateTestKeyRequestPayload.from_dict(regenerate_test_key_request)
    return web.Response(status=200)


async def services_update(request: web.Request, api_version, subscription_id, resource_group_name, service_name, resource) -> web.Response:
    """services_update

    Operation to update an exiting Service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param service_name: The name of the Service resource.
    :type service_name: str
    :param resource: Parameters for the update operation
    :type resource: dict | bytes

    """
    resource = ServiceResource.from_dict(resource)
    return web.Response(status=200)
