from typing import List, Dict
from aiohttp import web

from openapi_server.models.recommendation import Recommendation
from openapi_server.models.recommendation_rule import RecommendationRule
from openapi_server import util


async def recommendations_get_recommendation_by_subscription(request: web.Request, subscription_id, api_version, featured=None, filter=None) -> web.Response:
    """Gets a list of recommendations associated with the specified subscription.

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param featured: If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available
    :type featured: bool
    :param filter: Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;channels eq &#39;Api&#39; or channel eq &#39;Notification&#39;
    :type filter: str

    """
    return web.Response(status=200)


async def recommendations_get_recommendation_history_for_site(request: web.Request, resource_group_name, site_name, subscription_id, api_version, start_time=None, end_time=None) -> web.Response:
    """Gets the list of past recommendations optionally specified by the time range.

    

    :param resource_group_name: Resource group name
    :type resource_group_name: str
    :param site_name: Site name
    :type site_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: The start time of a time range to query, e.g. $filter&#x3D;startTime eq &#39;2015-01-01T00:00:00Z&#39; and endTime eq &#39;2015-01-02T00:00:00Z&#39;
    :type start_time: str
    :param end_time: The end time of a time range to query, e.g. $filter&#x3D;startTime eq &#39;2015-01-01T00:00:00Z&#39; and endTime eq &#39;2015-01-02T00:00:00Z&#39;
    :type end_time: str

    """
    return web.Response(status=200)


async def recommendations_get_recommended_rules_for_site(request: web.Request, resource_group_name, site_name, subscription_id, api_version, featured=None, site_sku=None, num_slots=None) -> web.Response:
    """Gets a list of recommendations associated with the specified web site.

    

    :param resource_group_name: Resource group name
    :type resource_group_name: str
    :param site_name: Site name
    :type site_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param featured: If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available
    :type featured: bool
    :param site_sku: The name of site SKU.
    :type site_sku: str
    :param num_slots: The number of site slots associated to the site
    :type num_slots: int

    """
    return web.Response(status=200)


async def recommendations_get_rule_details_by_site_name(request: web.Request, resource_group_name, site_name, name, subscription_id, api_version) -> web.Response:
    """Gets the detailed properties of the recommendation object for the specified web site.

    

    :param resource_group_name: Resource group name
    :type resource_group_name: str
    :param site_name: Site name
    :type site_name: str
    :param name: Recommendation rule name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
