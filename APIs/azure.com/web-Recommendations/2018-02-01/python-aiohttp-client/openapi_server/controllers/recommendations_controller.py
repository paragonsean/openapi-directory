from typing import List, Dict
from aiohttp import web

from openapi_server.models.recommendation_collection import RecommendationCollection
from openapi_server.models.recommendation_rule import RecommendationRule
from openapi_server.models.recommendations_list_default_response import RecommendationsListDefaultResponse
from openapi_server import util


async def recommendations_disable_all_for_hosting_environment(request: web.Request, resource_group_name, environment_name, hosting_environment_name, subscription_id, api_version) -> web.Response:
    """Disable all recommendations for an app.

    Disable all recommendations for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param environment_name: Name of the app.
    :type environment_name: str
    :param hosting_environment_name: 
    :type hosting_environment_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_disable_all_for_web_app(request: web.Request, resource_group_name, site_name, subscription_id, api_version) -> web.Response:
    """Disable all recommendations for an app.

    Disable all recommendations for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Name of the app.
    :type site_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_disable_recommendation_for_hosting_environment(request: web.Request, resource_group_name, environment_name, name, hosting_environment_name, subscription_id, api_version) -> web.Response:
    """Disables the specific rule for a web site permanently.

    Disables the specific rule for a web site permanently.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param environment_name: Site name
    :type environment_name: str
    :param name: Rule name
    :type name: str
    :param hosting_environment_name: 
    :type hosting_environment_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_disable_recommendation_for_site(request: web.Request, resource_group_name, site_name, name, subscription_id, api_version) -> web.Response:
    """Disables the specific rule for a web site permanently.

    Disables the specific rule for a web site permanently.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site name
    :type site_name: str
    :param name: Rule name
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_disable_recommendation_for_subscription(request: web.Request, name, subscription_id, api_version) -> web.Response:
    """Disables the specified rule so it will not apply to a subscription in the future.

    Disables the specified rule so it will not apply to a subscription in the future.

    :param name: Rule name
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_get_rule_details_by_hosting_environment(request: web.Request, resource_group_name, hosting_environment_name, name, subscription_id, api_version, update_seen=None, recommendation_id=None) -> web.Response:
    """Get a recommendation rule for an app.

    Get a recommendation rule for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param hosting_environment_name: Name of the hosting environment.
    :type hosting_environment_name: str
    :param name: Name of the recommendation.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param update_seen: Specify &lt;code&gt;true&lt;/code&gt; to update the last-seen timestamp of the recommendation object.
    :type update_seen: bool
    :param recommendation_id: The GUID of the recommendation object if you query an expired one. You don&#39;t need to specify it to query an active entry.
    :type recommendation_id: str

    """
    return web.Response(status=200)


async def recommendations_get_rule_details_by_web_app(request: web.Request, resource_group_name, site_name, name, subscription_id, api_version, update_seen=None, recommendation_id=None) -> web.Response:
    """Get a recommendation rule for an app.

    Get a recommendation rule for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Name of the app.
    :type site_name: str
    :param name: Name of the recommendation.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param update_seen: Specify &lt;code&gt;true&lt;/code&gt; to update the last-seen timestamp of the recommendation object.
    :type update_seen: bool
    :param recommendation_id: The GUID of the recommendation object if you query an expired one. You don&#39;t need to specify it to query an active entry.
    :type recommendation_id: str

    """
    return web.Response(status=200)


async def recommendations_list(request: web.Request, subscription_id, api_version, featured=None, filter=None) -> web.Response:
    """List all recommendations for a subscription.

    List all recommendations for a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param featured: Specify &lt;code&gt;true&lt;/code&gt; to return only the most critical recommendations. The default is &lt;code&gt;false&lt;/code&gt;, which returns all recommendations.
    :type featured: bool
    :param filter: Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39; and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[PT1H|PT1M|P1D]
    :type filter: str

    """
    return web.Response(status=200)


async def recommendations_list_history_for_hosting_environment(request: web.Request, resource_group_name, hosting_environment_name, subscription_id, api_version, expired_only=None, filter=None) -> web.Response:
    """Get past recommendations for an app, optionally specified by the time range.

    Get past recommendations for an app, optionally specified by the time range.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param hosting_environment_name: Name of the hosting environment.
    :type hosting_environment_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param expired_only: Specify &lt;code&gt;false&lt;/code&gt; to return all recommendations. The default is &lt;code&gt;true&lt;/code&gt;, which returns only expired recommendations.
    :type expired_only: bool
    :param filter: Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39; and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[PT1H|PT1M|P1D]
    :type filter: str

    """
    return web.Response(status=200)


async def recommendations_list_history_for_web_app(request: web.Request, resource_group_name, site_name, subscription_id, api_version, expired_only=None, filter=None) -> web.Response:
    """Get past recommendations for an app, optionally specified by the time range.

    Get past recommendations for an app, optionally specified by the time range.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Name of the app.
    :type site_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param expired_only: Specify &lt;code&gt;false&lt;/code&gt; to return all recommendations. The default is &lt;code&gt;true&lt;/code&gt;, which returns only expired recommendations.
    :type expired_only: bool
    :param filter: Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39; and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[PT1H|PT1M|P1D]
    :type filter: str

    """
    return web.Response(status=200)


async def recommendations_list_recommended_rules_for_hosting_environment(request: web.Request, resource_group_name, hosting_environment_name, subscription_id, api_version, featured=None, filter=None) -> web.Response:
    """Get all recommendations for an app.

    Get all recommendations for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param hosting_environment_name: Name of the app.
    :type hosting_environment_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param featured: Specify &lt;code&gt;true&lt;/code&gt; to return only the most critical recommendations. The default is &lt;code&gt;false&lt;/code&gt;, which returns all recommendations.
    :type featured: bool
    :param filter: Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39;
    :type filter: str

    """
    return web.Response(status=200)


async def recommendations_list_recommended_rules_for_web_app(request: web.Request, resource_group_name, site_name, subscription_id, api_version, featured=None, filter=None) -> web.Response:
    """Get all recommendations for an app.

    Get all recommendations for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Name of the app.
    :type site_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param featured: Specify &lt;code&gt;true&lt;/code&gt; to return only the most critical recommendations. The default is &lt;code&gt;false&lt;/code&gt;, which returns all recommendations.
    :type featured: bool
    :param filter: Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39;
    :type filter: str

    """
    return web.Response(status=200)


async def recommendations_reset_all_filters(request: web.Request, subscription_id, api_version) -> web.Response:
    """Reset all recommendation opt-out settings for a subscription.

    Reset all recommendation opt-out settings for a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_reset_all_filters_for_hosting_environment(request: web.Request, resource_group_name, environment_name, hosting_environment_name, subscription_id, api_version) -> web.Response:
    """Reset all recommendation opt-out settings for an app.

    Reset all recommendation opt-out settings for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param environment_name: Name of the app.
    :type environment_name: str
    :param hosting_environment_name: 
    :type hosting_environment_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_reset_all_filters_for_web_app(request: web.Request, resource_group_name, site_name, subscription_id, api_version) -> web.Response:
    """Reset all recommendation opt-out settings for an app.

    Reset all recommendation opt-out settings for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Name of the app.
    :type site_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
