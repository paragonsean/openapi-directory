from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_machine_size_list_result import VirtualMachineSizeListResult
from openapi_server import util


async def virtual_machine_sizes_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """virtual_machine_sizes_list

    Returns supported VM Sizes in a location

    :param location: The location upon which virtual-machine-sizes is queried.
    :type location: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)
