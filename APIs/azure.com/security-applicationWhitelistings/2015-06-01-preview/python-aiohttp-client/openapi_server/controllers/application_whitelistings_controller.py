from typing import List, Dict
from aiohttp import web

from openapi_server.models.adaptive_application_controls_list_default_response import AdaptiveApplicationControlsListDefaultResponse
from openapi_server.models.app_whitelisting_group import AppWhitelistingGroup
from openapi_server.models.app_whitelisting_groups import AppWhitelistingGroups
from openapi_server.models.app_whitelisting_put_group_data import AppWhitelistingPutGroupData
from openapi_server import util


async def adaptive_application_controls_get(request: web.Request, subscription_id, asc_location, group_name, api_version) -> web.Response:
    """adaptive_application_controls_get

    Gets an application control VM/server group.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param group_name: Name of an application control VM/server group
    :type group_name: str
    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def adaptive_application_controls_list(request: web.Request, subscription_id, api_version, include_path_recommendations=None, summary=None) -> web.Response:
    """adaptive_application_controls_list

    Gets a list of application control VM/server groups for the subscription.

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param api_version: API version for the operation
    :type api_version: str
    :param include_path_recommendations: Include the policy rules
    :type include_path_recommendations: bool
    :param summary: Return output in a summarized form
    :type summary: bool

    """
    return web.Response(status=200)


async def adaptive_application_controls_put(request: web.Request, subscription_id, asc_location, group_name, api_version, body) -> web.Response:
    """adaptive_application_controls_put

    Update an application control VM/server group

    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str
    :param group_name: Name of an application control VM/server group
    :type group_name: str
    :param api_version: API version for the operation
    :type api_version: str
    :param body: The updated VM/server group data
    :type body: dict | bytes

    """
    body = AppWhitelistingPutGroupData.from_dict(body)
    return web.Response(status=200)
