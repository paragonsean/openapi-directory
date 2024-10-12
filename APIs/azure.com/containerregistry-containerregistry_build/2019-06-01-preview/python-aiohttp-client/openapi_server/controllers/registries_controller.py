from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.run import Run
from openapi_server.models.run_request import RunRequest
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


async def registries_schedule_run(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, run_request) -> web.Response:
    """registries_schedule_run

    Schedules a new run based on the request parameters and add it to the run queue.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param run_request: The parameters of a run that needs to scheduled.
    :type run_request: dict | bytes

    """
    run_request = RunRequest.from_dict(run_request)
    return web.Response(status=200)
