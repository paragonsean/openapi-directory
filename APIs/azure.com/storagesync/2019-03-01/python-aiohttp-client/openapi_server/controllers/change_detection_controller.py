from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.trigger_change_detection_parameters import TriggerChangeDetectionParameters
from openapi_server import util


async def cloud_endpoints_trigger_change_detection_1(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_trigger_change_detection_1

    Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str
    :param parameters: Trigger Change Detection Action parameters.
    :type parameters: dict | bytes

    """
    parameters = TriggerChangeDetectionParameters.from_dict(parameters)
    return web.Response(status=200)
