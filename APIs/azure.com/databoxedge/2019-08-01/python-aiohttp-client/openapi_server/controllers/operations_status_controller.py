from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.job import Job
from openapi_server import util


async def operations_status_get(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Gets the details of a specified job on a Data Box Edge/Data Box Gateway device.

    

    :param device_name: The device name.
    :type device_name: str
    :param name: The job name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
