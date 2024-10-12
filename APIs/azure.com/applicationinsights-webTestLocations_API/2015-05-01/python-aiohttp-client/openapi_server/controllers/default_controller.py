from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_insights_web_test_locations_list_result import ApplicationInsightsWebTestLocationsListResult
from openapi_server import util


async def web_test_locations_list(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """web_test_locations_list

    Gets a list of web test locations available to this Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str

    """
    return web.Response(status=200)
