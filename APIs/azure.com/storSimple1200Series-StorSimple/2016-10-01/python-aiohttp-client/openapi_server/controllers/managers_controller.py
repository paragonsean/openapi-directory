from typing import List, Dict
from aiohttp import web

from openapi_server.models.encryption_settings import EncryptionSettings
from openapi_server.models.error import Error
from openapi_server.models.manager import Manager
from openapi_server.models.manager_extended_info import ManagerExtendedInfo
from openapi_server.models.manager_list import ManagerList
from openapi_server.models.manager_patch import ManagerPatch
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server.models.symmetric_encrypted_secret import SymmetricEncryptedSecret
from openapi_server.models.upload_certificate_request import UploadCertificateRequest
from openapi_server.models.upload_certificate_response import UploadCertificateResponse
from openapi_server import util


async def managers_create_extended_info(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, manager_extended_info) -> web.Response:
    """managers_create_extended_info

    Creates the extended info of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param manager_extended_info: The manager extended information.
    :type manager_extended_info: dict | bytes

    """
    manager_extended_info = ManagerExtendedInfo.from_dict(manager_extended_info)
    return web.Response(status=200)


async def managers_create_or_update(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, manager) -> web.Response:
    """managers_create_or_update

    Creates or updates the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param manager: The manager.
    :type manager: dict | bytes

    """
    manager = Manager.from_dict(manager)
    return web.Response(status=200)


async def managers_delete(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_delete

    Deletes the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_delete_extended_info(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_delete_extended_info

    Deletes the extended info of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get

    Returns the properties of the specified manager name.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get_encryption_key(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get_encryption_key

    Returns the symmetric encryption key of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get_encryption_settings(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get_encryption_settings

    Returns the encryption settings of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get_extended_info(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get_extended_info

    Returns the extended information of the specified manager name.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """managers_list

    Retrieves all the managers in a subscription.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """managers_list_by_resource_group

    Retrieves all the managers in a resource group.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_list_metric_definition(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_list_metric_definition

    Retrieves metric definition of all metrics aggregated at manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_list_metrics(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """managers_list_metrics

    Gets the  manager metrics

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def managers_update(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """managers_update

    Updates the StorSimple Manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The manager update parameters.
    :type parameters: dict | bytes

    """
    parameters = ManagerPatch.from_dict(parameters)
    return web.Response(status=200)


async def managers_update_extended_info(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, if_match, manager_extended_info) -> web.Response:
    """managers_update_extended_info

    Updates the extended info of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param if_match: Pass the ETag of ExtendedInfo fetched from GET call
    :type if_match: str
    :param manager_extended_info: The manager extended information.
    :type manager_extended_info: dict | bytes

    """
    manager_extended_info = ManagerExtendedInfo.from_dict(manager_extended_info)
    return web.Response(status=200)


async def managers_upload_registration_certificate(request: web.Request, certificate_name, subscription_id, resource_group_name, manager_name, api_version, upload_certificate_requestrequest) -> web.Response:
    """managers_upload_registration_certificate

    Upload Vault Cred Certificate.  Returns UploadCertificateResponse

    :param certificate_name: Certificate Name
    :type certificate_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param upload_certificate_requestrequest: UploadCertificateRequest Request
    :type upload_certificate_requestrequest: dict | bytes

    """
    upload_certificate_requestrequest = UploadCertificateRequest.from_dict(upload_certificate_requestrequest)
    return web.Response(status=200)
