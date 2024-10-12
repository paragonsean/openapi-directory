from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.get_ssis_object_metadata_request import GetSsisObjectMetadataRequest
from openapi_server.models.integration_runtime_object_metadata_get200_response import IntegrationRuntimeObjectMetadataGet200Response
from openapi_server.models.ssis_object_metadata_status_response import SsisObjectMetadataStatusResponse
from openapi_server import util


async def integration_runtime_object_metadata_get(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version, get_metadata_request=None) -> web.Response:
    """integration_runtime_object_metadata_get

    Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list.

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
    :param get_metadata_request: The parameters for getting a SSIS object metadata.
    :type get_metadata_request: dict | bytes

    """
    get_metadata_request = GetSsisObjectMetadataRequest.from_dict(get_metadata_request)
    return web.Response(status=200)


async def integration_runtime_object_metadata_refresh(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, api_version) -> web.Response:
    """integration_runtime_object_metadata_refresh

    Refresh a SSIS integration runtime object metadata.

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
