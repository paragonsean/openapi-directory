from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_recommendation_base import ResourceRecommendationBase
from openapi_server.models.resource_recommendation_base_list_result import ResourceRecommendationBaseListResult
from openapi_server import util


async def recommendations_get(request: web.Request, resource_uri, recommendation_id, api_version) -> web.Response:
    """recommendations_get

    Obtains details of a cached recommendation.

    :param resource_uri: The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    :type resource_uri: str
    :param recommendation_id: The recommendation ID.
    :type recommendation_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_list(request: web.Request, subscription_id, api_version, filter=None, top=None, skip_token=None) -> web.Response:
    """recommendations_list

    Obtains cached recommendations for a subscription. The recommendations are generated or computed by invoking generateRecommendations.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The filter to apply to the recommendations.
    :type filter: str
    :param top: The number of recommendations per page if a paged version of this API is being used.
    :type top: int
    :param skip_token: The page-continuation token to use with a paged version of this API.
    :type skip_token: str

    """
    return web.Response(status=200)
