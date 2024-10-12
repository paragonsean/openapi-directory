from typing import List, Dict
from aiohttp import web

from openapi_server.models.discovered_security_solution import DiscoveredSecuritySolution
from openapi_server.models.discovered_security_solution_list import DiscoveredSecuritySolutionList
from openapi_server.models.discovered_security_solutions_list_default_response import DiscoveredSecuritySolutionsListDefaultResponse
from openapi_server import util


async def discovered_security_solutions_get(request: web.Request, subscription_id, resource_group_name, asc_location, discovered_security_solution_name, api_version) -> web.Response:
    """discovered_security_solutions_get

    Gets a specific discovered Security Solution.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param discovered_security_solution_name: Name of a discovered security solution.
    :type discovered_security_solution_name: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def discovered_security_solutions_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """discovered_security_solutions_list

    Gets a list of discovered Security Solutions for the subscription.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def discovered_security_solutions_list_by_home_region(request: web.Request, subscription_id, asc_location, api_version) -> web.Response:
    """discovered_security_solutions_list_by_home_region

    Gets a list of discovered Security Solutions for the subscription and location.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)
