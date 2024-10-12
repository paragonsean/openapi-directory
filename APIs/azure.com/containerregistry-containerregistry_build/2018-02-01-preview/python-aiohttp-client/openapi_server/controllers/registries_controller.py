from typing import List, Dict
from aiohttp import web

from openapi_server.models.build import Build
from openapi_server.models.queue_build_request import QueueBuildRequest
from openapi_server.models.source_upload_definition import SourceUploadDefinition
from openapi_server import util


async def registries_get_build_source_upload_url(request: web.Request, subscription_id, resource_group_name, registry_name, api_version) -> web.Response:
    """registries_get_build_source_upload_url

    Get the upload location for the user to be able to upload the source.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registries_queue_build(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_request) -> web.Response:
    """registries_queue_build

    Creates a new build based on the request parameters and add it to the build queue.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_request: The parameters of a build that needs to queued.
    :type build_request: dict | bytes

    """
    build_request = QueueBuildRequest.from_dict(build_request)
    return web.Response(status=200)
