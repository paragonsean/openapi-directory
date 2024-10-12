from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_image_upload_url_input import GetImageUploadUrlInput
from openapi_server.models.image_definition import ImageDefinition
from openapi_server import util


async def images_get_upload_url_for_data(request: web.Request, resource_group_name, hub_name, api_version, subscription_id, parameters) -> web.Response:
    """images_get_upload_url_for_data

    Gets data image upload URL.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the GetUploadUrlForData operation.
    :type parameters: dict | bytes

    """
    parameters = GetImageUploadUrlInput.from_dict(parameters)
    return web.Response(status=200)


async def images_get_upload_url_for_entity_type(request: web.Request, resource_group_name, hub_name, api_version, subscription_id, parameters) -> web.Response:
    """images_get_upload_url_for_entity_type

    Gets entity type (profile or interaction) image upload URL.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the GetUploadUrlForEntityType operation.
    :type parameters: dict | bytes

    """
    parameters = GetImageUploadUrlInput.from_dict(parameters)
    return web.Response(status=200)
