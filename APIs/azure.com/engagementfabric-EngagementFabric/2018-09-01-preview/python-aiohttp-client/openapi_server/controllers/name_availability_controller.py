from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_parameter import CheckNameAvailabilityParameter
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def check_name_availability(request: web.Request, subscription_id, resource_group_name, api_version, parameters) -> web.Response:
    """Check availability of EngagementFabric resource

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param api_version: API version
    :type api_version: str
    :param parameters: Parameter describing the name to be checked
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailabilityParameter.from_dict(parameters)
    return web.Response(status=200)
