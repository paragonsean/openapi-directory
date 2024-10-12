from typing import List, Dict
from aiohttp import web

from openapi_server.models.external_security_solution import ExternalSecuritySolution
from openapi_server.models.external_security_solution_list import ExternalSecuritySolutionList
from openapi_server.models.external_security_solutions_list_default_response import ExternalSecuritySolutionsListDefaultResponse
from openapi_server import util


async def external_security_solutions_get(request: web.Request, subscription_id, resource_group_name, asc_location, external_security_solutions_name, api_version) -> web.Response:
    """external_security_solutions_get

    Gets a specific external Security Solution.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param external_security_solutions_name: Name of an external security solution.
    :type external_security_solutions_name: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def external_security_solutions_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """external_security_solutions_list

    Gets a list of external security solutions for the subscription.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def external_security_solutions_list_by_home_region(request: web.Request, subscription_id, asc_location, api_version) -> web.Response:
    """external_security_solutions_list_by_home_region

    Gets a list of external Security Solutions for the subscription and location.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)
