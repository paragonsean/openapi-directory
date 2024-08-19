from typing import List, Dict
from aiohttp import web

from openapi_server.models.orchestrator_version_profile_list_result import OrchestratorVersionProfileListResult
from openapi_server import util


async def container_services_list_orchestrators(request: web.Request, api_version, subscription_id, location, resource_type=None) -> web.Response:
    """Gets a list of supported orchestrators in the specified subscription.

    Gets a list of supported orchestrators in the specified subscription. The operation returns properties of each orchestrator including version and available upgrades.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The name of a supported Azure region.
    :type location: str
    :param resource_type: resource type for which the list of orchestrators needs to be returned
    :type resource_type: str

    """
    return web.Response(status=200)
