from typing import List, Dict
from aiohttp import web

from openapi_server.models.solution import Solution
from openapi_server.models.solution_config import SolutionConfig
from openapi_server.models.solutions_collection import SolutionsCollection
from openapi_server import util


async def solutions_cleanup_solution_data(request: web.Request, subscription_id, resource_group_name, migrate_project_name, solution_name, api_version) -> web.Response:
    """Cleanup the solution data in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param solution_name: Unique name of a migration solution within a migrate project.
    :type solution_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str

    """
    return web.Response(status=200)


async def solutions_delete_solution(request: web.Request, subscription_id, resource_group_name, migrate_project_name, solution_name, api_version, accept_language=None) -> web.Response:
    """Delete the solution

    Delete the solution. Deleting non-existent project is a no-operation.

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param solution_name: Unique name of a migration solution within a migrate project.
    :type solution_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def solutions_enumerate_solutions(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version) -> web.Response:
    """Gets the list of solutions in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str

    """
    return web.Response(status=200)


async def solutions_get_config(request: web.Request, subscription_id, resource_group_name, migrate_project_name, solution_name, api_version) -> web.Response:
    """Gets the config for the solution in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param solution_name: Unique name of a migration solution within a migrate project.
    :type solution_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str

    """
    return web.Response(status=200)


async def solutions_get_solution(request: web.Request, subscription_id, resource_group_name, migrate_project_name, solution_name, api_version) -> web.Response:
    """Gets a solution in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param solution_name: Unique name of a migration solution within a migrate project.
    :type solution_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str

    """
    return web.Response(status=200)


async def solutions_patch_solution(request: web.Request, subscription_id, resource_group_name, migrate_project_name, solution_name, api_version, solution_input) -> web.Response:
    """Update solution.

    Update a solution with specified name. Supports partial updates, for example only tags can be provided.

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param solution_name: Unique name of a migration solution within a migrate project.
    :type solution_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param solution_input: The input for the solution.
    :type solution_input: dict | bytes

    """
    solution_input = Solution.from_dict(solution_input)
    return web.Response(status=200)


async def solutions_put_solution(request: web.Request, subscription_id, resource_group_name, migrate_project_name, solution_name, api_version, solution_input) -> web.Response:
    """Creates a solution in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param solution_name: Unique name of a migration solution within a migrate project.
    :type solution_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param solution_input: The input for the solution.
    :type solution_input: dict | bytes

    """
    solution_input = Solution.from_dict(solution_input)
    return web.Response(status=200)
