from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_operation_result import AsyncOperationResult
from openapi_server.models.certificate_list_description import CertificateListDescription
from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.iot_dps_sku_definition_list_result import IotDpsSkuDefinitionListResult
from openapi_server.models.provisioning_service_description import ProvisioningServiceDescription
from openapi_server.models.provisioning_service_description_list_result import ProvisioningServiceDescriptionListResult
from openapi_server import util


async def dps_certificate_get(request: web.Request, certificate_name, subscription_id, resource_group_name, provisioning_service_name, api_version, if_match=None) -> web.Response:
    """dps_certificate_get

    Get the certificate from the provisioning service.

    :param certificate_name: Name of the certificate to retrieve.
    :type certificate_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param provisioning_service_name: Name of the provisioning service the certificate is associated with.
    :type provisioning_service_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param if_match: ETag of the certificate.
    :type if_match: str

    """
    return web.Response(status=200)


async def dps_certificate_list(request: web.Request, subscription_id, resource_group_name, provisioning_service_name, api_version) -> web.Response:
    """dps_certificate_list

    Get all the certificates tied to the provisioning service.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of resource group.
    :type resource_group_name: str
    :param provisioning_service_name: Name of provisioning service to retrieve certificates for.
    :type provisioning_service_name: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)


async def iot_dps_resource_get(request: web.Request, provisioning_service_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Get the non-security related metadata of the provisioning service.

    Get the metadata of the provisioning service without SAS keys.

    :param provisioning_service_name: Name of the provisioning service to retrieve.
    :type provisioning_service_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)


async def iot_dps_resource_get_operation_result(request: web.Request, operation_id, subscription_id, resource_group_name, provisioning_service_name, asyncinfo, api_version) -> web.Response:
    """iot_dps_resource_get_operation_result

    Gets the status of a long running operation, such as create, update or delete a provisioning service.

    :param operation_id: Operation id corresponding to long running operation. Use this to poll for the status.
    :type operation_id: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param provisioning_service_name: Name of provisioning service that the operation is running on.
    :type provisioning_service_name: str
    :param asyncinfo: Async header used to poll on the status of the operation, obtained while creating the long running operation.
    :type asyncinfo: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)


async def iot_dps_resource_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """iot_dps_resource_list_by_resource_group

    Get a list of all provisioning services in the given resource group.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)


async def iot_dps_resource_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get all the provisioning services in a subscription.

    List all the provisioning services for a given subscription id.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)


async def iot_dps_resource_list_valid_skus(request: web.Request, provisioning_service_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Get the list of valid SKUs for a provisioning service.

    Gets the list of valid SKUs and tiers for a provisioning service.

    :param provisioning_service_name: Name of provisioning service.
    :type provisioning_service_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of resource group.
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)
