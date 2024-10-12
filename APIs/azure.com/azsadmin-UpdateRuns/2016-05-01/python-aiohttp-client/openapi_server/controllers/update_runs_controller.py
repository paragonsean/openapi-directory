from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_run import UpdateRun
from openapi_server.models.update_run_list import UpdateRunList
from openapi_server import util


async def update_runs_get(request: web.Request, subscription_id, resource_group_name, update_location, update_name, run_name, api_version) -> web.Response:
    """update_runs_get

    Get an instance of update run using the ID.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param update_location: The name of the update location.
    :type update_location: str
    :param update_name: Name of the update.
    :type update_name: str
    :param run_name: Update run identifier.
    :type run_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def update_runs_get_top_level(request: web.Request, subscription_id, resource_group_name, update_location, run_name, api_version) -> web.Response:
    """update_runs_get_top_level

    Get an instance of update run using the ID.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param update_location: The name of the update location.
    :type update_location: str
    :param run_name: Update run identifier.
    :type run_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def update_runs_list(request: web.Request, subscription_id, resource_group_name, update_location, update_name, api_version) -> web.Response:
    """update_runs_list

    Get the list of update runs.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param update_location: The name of the update location.
    :type update_location: str
    :param update_name: Name of the update.
    :type update_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def update_runs_list_top_level(request: web.Request, subscription_id, resource_group_name, update_location, api_version) -> web.Response:
    """update_runs_list_top_level

    Get the list of update runs.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param update_location: The name of the update location.
    :type update_location: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def update_runs_rerun(request: web.Request, subscription_id, resource_group_name, update_location, update_name, run_name, api_version) -> web.Response:
    """update_runs_rerun

    Resume a failed update.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param update_location: The name of the update location.
    :type update_location: str
    :param update_name: Name of the update.
    :type update_name: str
    :param run_name: Update run identifier.
    :type run_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
