from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.data_box_edge_device import DataBoxEdgeDevice
from openapi_server.models.data_box_edge_device_extended_info import DataBoxEdgeDeviceExtendedInfo
from openapi_server.models.data_box_edge_device_list import DataBoxEdgeDeviceList
from openapi_server.models.data_box_edge_device_patch import DataBoxEdgeDevicePatch
from openapi_server.models.network_settings import NetworkSettings
from openapi_server.models.security_settings import SecuritySettings
from openapi_server.models.update_summary import UpdateSummary
from openapi_server.models.upload_certificate_request import UploadCertificateRequest
from openapi_server.models.upload_certificate_response import UploadCertificateResponse
from openapi_server import util


async def devices_create_or_update(request: web.Request, device_name, subscription_id, resource_group_name, api_version, data_box_edge_device) -> web.Response:
    """devices_create_or_update

    Creates or updates a Data Box Edge/Data Box Gateway resource.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param data_box_edge_device: The resource object.
    :type data_box_edge_device: dict | bytes

    """
    data_box_edge_device = DataBoxEdgeDevice.from_dict(data_box_edge_device)
    return web.Response(status=200)


async def devices_create_or_update_security_settings(request: web.Request, device_name, subscription_id, resource_group_name, api_version, security_settings) -> web.Response:
    """devices_create_or_update_security_settings

    Updates the security settings on a Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param security_settings: The security settings.
    :type security_settings: dict | bytes

    """
    security_settings = SecuritySettings.from_dict(security_settings)
    return web.Response(status=200)


async def devices_delete(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """devices_delete

    Deletes the Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def devices_download_updates(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Downloads the updates on a Data Box Edge/Data Box Gateway device.

    

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def devices_get(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """devices_get

    Gets the properties of the Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def devices_get_extended_information(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """devices_get_extended_information

    Gets additional information for the specified Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def devices_get_network_settings(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """devices_get_network_settings

    Gets the network settings of the specified Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def devices_get_update_summary(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.

    

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def devices_install_updates(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Installs the updates on the Data Box Edge/Data Box Gateway device.

    

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def devices_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, expand=None) -> web.Response:
    """devices_list_by_resource_group

    Gets all the Data Box Edge/Data Box Gateway devices in a resource group.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param expand: Specify $expand&#x3D;details to populate additional fields related to the resource or Specify $skipToken&#x3D;&lt;token&gt; to populate the next page in the list.
    :type expand: str

    """
    return web.Response(status=200)


async def devices_list_by_subscription(request: web.Request, subscription_id, api_version, expand=None) -> web.Response:
    """devices_list_by_subscription

    Gets all the Data Box Edge/Data Box Gateway devices in a subscription.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: The API version.
    :type api_version: str
    :param expand: Specify $expand&#x3D;details to populate additional fields related to the resource or Specify $skipToken&#x3D;&lt;token&gt; to populate the next page in the list.
    :type expand: str

    """
    return web.Response(status=200)


async def devices_scan_for_updates(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Scans for updates on a Data Box Edge/Data Box Gateway device.

    

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def devices_update(request: web.Request, device_name, subscription_id, resource_group_name, api_version, parameters) -> web.Response:
    """devices_update

    Modifies a Data Box Edge/Data Box Gateway resource.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param parameters: The resource parameters.
    :type parameters: dict | bytes

    """
    parameters = DataBoxEdgeDevicePatch.from_dict(parameters)
    return web.Response(status=200)


async def devices_upload_certificate(request: web.Request, device_name, subscription_id, resource_group_name, api_version, parameters) -> web.Response:
    """devices_upload_certificate

    Uploads registration certificate for the device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param parameters: The upload certificate request.
    :type parameters: dict | bytes

    """
    parameters = UploadCertificateRequest.from_dict(parameters)
    return web.Response(status=200)
