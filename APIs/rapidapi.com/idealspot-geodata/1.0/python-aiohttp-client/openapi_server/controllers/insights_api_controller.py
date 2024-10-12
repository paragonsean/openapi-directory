from typing import List, Dict
from aiohttp import web

from openapi_server.models.describe_occupation_insight import DescribeOccupationInsight
from openapi_server.models.homevalueswithin1mi_radiusof_location import Homevalueswithin1miRadiusofLocation
from openapi_server.models.list_all_local_insights import ListAllLocalInsights
from openapi_server import util


async def fetch_available_insights(request: web.Request, x_rapid_api_key, x_rapid_api_host) -> web.Response:
    """Fetch Available Insights

    List all insights that the user has access to. This includes population, household income, crime statistics, walking traffic, vehicle traffic counts, employment, and much more,

    :param x_rapid_api_key: (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    :type x_rapid_api_key: str
    :param x_rapid_api_host: 
    :type x_rapid_api_host: str

    """
    return web.Response(status=200)


async def fetch_insight_query_parameters(request: web.Request, insight_id, x_rapid_api_key, x_rapid_api_host) -> web.Response:
    """Fetch Insight Query Parameters

    Fetch request/response structure metadata for a given Insight. This provides you the periods of data available as well as any other parameters you may want to query the Insight by. Example Insights include population and market data such as: age, daytime population, avg. home value, crime indexes, foot traffic, employment, income, occupation, etc.  For the full-list see the developer documentation.

    :param insight_id: Insight ID. See developer documentation for full list.
    :type insight_id: str
    :param x_rapid_api_key: (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    :type x_rapid_api_key: str
    :param x_rapid_api_host: 
    :type x_rapid_api_host: str

    """
    return web.Response(status=200)


async def query_insightat_location(request: web.Request, version, location, insight_id, x_rapid_api_key, x_rapid_api_host) -> web.Response:
    """Query Insight at Location

    Execute a query for a given insight and location(s). Some Insights may require you to provide required options. ie., when querying &#x60;occupation&#x60; for White-Collar Workers, you can filter by opt&#x3D;&#x60;{\&quot;data\&quot;:{\&quot;category\&quot;:[2469]}}&#x60;  For examples of &#x60;locations&#x60;, please see [Location API Documentation](https://idealspot.gitlab.io/developer-docs/#location)

    :param version: (Required) Insight version. Insight versions are incremented when a response format changes in any way, including the addition of new groups. Old versions are retained, unmodified, for backwards compatibility.
    :type version: str
    :param location: (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used. For more detail, see https://idealspot.gitlab.io/developer-docs/#location
    :type location: str
    :param insight_id: Insight ID. See https://developer.idealspot.com/data for full list.
    :type insight_id: str
    :param x_rapid_api_key: (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    :type x_rapid_api_key: str
    :param x_rapid_api_host: 
    :type x_rapid_api_host: str

    """
    return web.Response(status=200)
