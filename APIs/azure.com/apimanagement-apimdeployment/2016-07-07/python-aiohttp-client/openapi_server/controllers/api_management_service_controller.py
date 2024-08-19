from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_management_service_backup_restore_parameters import ApiManagementServiceBackupRestoreParameters
from openapi_server.models.api_management_service_base_parameters import ApiManagementServiceBaseParameters
from openapi_server.models.api_management_service_check_name_availability_parameters import ApiManagementServiceCheckNameAvailabilityParameters
from openapi_server.models.api_management_service_get_sso_token_result import ApiManagementServiceGetSsoTokenResult
from openapi_server.models.api_management_service_list_result import ApiManagementServiceListResult
from openapi_server.models.api_management_service_manage_deployments_parameters import ApiManagementServiceManageDeploymentsParameters
from openapi_server.models.api_management_service_name_availability_result import ApiManagementServiceNameAvailabilityResult
from openapi_server.models.api_management_service_resource import ApiManagementServiceResource
from openapi_server.models.api_management_service_update_hostname_parameters import ApiManagementServiceUpdateHostnameParameters
from openapi_server.models.api_management_service_upload_certificate_parameters import ApiManagementServiceUploadCertificateParameters
from openapi_server.models.certificate_information import CertificateInformation
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def api_management_services_backup(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """api_management_services_backup

    Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the ApiManagementServices_Backup operation.
    :type parameters: dict | bytes

    """
    parameters = ApiManagementServiceBackupRestoreParameters.from_dict(parameters)
    return web.Response(status=200)


async def api_management_services_check_name_availability(request: web.Request, api_version, subscription_id, parameters) -> web.Response:
    """api_management_services_check_name_availability

    Checks availability and correctness of a name for an API Management service.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CheckNameAvailability operation.
    :type parameters: dict | bytes

    """
    parameters = ApiManagementServiceCheckNameAvailabilityParameters.from_dict(parameters)
    return web.Response(status=200)


async def api_management_services_create_or_update(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """api_management_services_create_or_update

    Creates or updates an API Management service. This is long running operation and could take several minutes to complete.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate API Management service operation.
    :type parameters: dict | bytes

    """
    parameters = ApiManagementServiceResource.from_dict(parameters)
    return web.Response(status=200)


async def api_management_services_delete(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """api_management_services_delete

    Deletes an existing API Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_management_services_get(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """api_management_services_get

    Gets an API Management service resource description.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_management_services_get_sso_token(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """api_management_services_get_sso_token

    Gets the Single-Sign-On token for the API Management Service which is valid for 5 Minutes.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_management_services_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """api_management_services_list

    Lists all API Management services within an Azure subscription.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_management_services_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """api_management_services_list_by_resource_group

    List all API Management services within a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_management_services_manage_deployments(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """api_management_services_manage_deployments

    Manages deployments of an API Management service. This operation can be used to do the following: Change SKU, Change SKU Units, Change Service Tier (Developer/Standard/Premium) and Manage VPN Configuration. This is a long running operation and can take several minutes to complete.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the ManageDeployments operation.
    :type parameters: dict | bytes

    """
    parameters = ApiManagementServiceManageDeploymentsParameters.from_dict(parameters)
    return web.Response(status=200)


async def api_management_services_restore(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """api_management_services_restore

    Restores a backup of an API Management service created using the ApiManagementServices_Backup operation on the current service. This is a long running operation and could take several minutes to complete.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Restore API Management service from backup operation.
    :type parameters: dict | bytes

    """
    parameters = ApiManagementServiceBackupRestoreParameters.from_dict(parameters)
    return web.Response(status=200)


async def api_management_services_update(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """api_management_services_update

    Updates an existing API Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate API Management service operation.
    :type parameters: dict | bytes

    """
    parameters = ApiManagementServiceBaseParameters.from_dict(parameters)
    return web.Response(status=200)


async def api_management_services_update_hostname(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """api_management_services_update_hostname

    Creates, updates, or deletes the custom hostnames for an API Management service. The custom hostname can be applied to the Proxy and Portal endpoint. This is a long running operation and could take several minutes to complete.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the UpdateHostname operation.
    :type parameters: dict | bytes

    """
    parameters = ApiManagementServiceUpdateHostnameParameters.from_dict(parameters)
    return web.Response(status=200)


async def api_management_services_upload_certificate(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """api_management_services_upload_certificate

    Upload Custom Domain SSL certificate for an API Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Upload SSL certificate for an API Management service operation.
    :type parameters: dict | bytes

    """
    parameters = ApiManagementServiceUploadCertificateParameters.from_dict(parameters)
    return web.Response(status=200)
